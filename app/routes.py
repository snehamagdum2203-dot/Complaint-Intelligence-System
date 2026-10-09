
from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash

from app.complaint_service import create_complaint
from app.database import get_connection
from app.validators import validate_status


main = Blueprint("main", __name__)


@main.route("/")
def home():
    return redirect(url_for("main.dashboard"))


@main.route("/complaint/new", methods=["GET", "POST"])
def new_complaint():
    if request.method == "POST":
        customer_code = request.form.get("customer_code", "").strip()
        customer_name = request.form.get("customer_name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        complaint_text = request.form.get("complaint_text", "").strip()
        priority = request.form.get("priority", "").strip()
        department = request.form.get("department", "").strip()

        success, result = create_complaint(
            customer_code,
            customer_name,
            email,
            phone,
            complaint_text,
            priority,
            department,
        )

        if success:
            flash(
                f"Complaint registered successfully. Category: {result}",
                "success",
            )
            return redirect(url_for("main.new_complaint"))

        flash(result, "error")

    return render_template("complaint_form.html")


@main.route("/complaints")
def complaints():
    connection = get_connection()

    try:
        complaints_data = connection.execute(
            """
            SELECT
                complaints.id,
                customers.customer_code,
                customers.name AS customer_name,
                complaints.complaint_text,
                complaints.category,
                complaints.priority,
                complaints.status,
                complaints.department,
                complaints.created_at
            FROM complaints
            JOIN customers
                ON complaints.customer_id = customers.id
            ORDER BY complaints.id DESC
            """
        ).fetchall()
    finally:
        connection.close()

    return render_template(
        "complaints.html",
        complaints=complaints_data,
    )


@main.route("/dashboard")
def dashboard():
    connection = get_connection()

    try:
        total_complaints = connection.execute(
            "SELECT COUNT(*) FROM complaints"
        ).fetchone()[0]

        open_complaints = connection.execute(
            "SELECT COUNT(*) FROM complaints WHERE status = 'Open'"
        ).fetchone()[0]

        resolved_complaints = connection.execute(
            "SELECT COUNT(*) FROM complaints WHERE status = 'Resolved'"
        ).fetchone()[0]

        critical_complaints = connection.execute(
            "SELECT COUNT(*) FROM complaints WHERE priority = 'Critical'"
        ).fetchone()[0]

        category_counts = connection.execute(
            """
            SELECT category, COUNT(*) AS total
            FROM complaints
            GROUP BY category
            ORDER BY total DESC
            """
        ).fetchall()
    finally:
        connection.close()

    return render_template(
        "dashboard.html",
        total_complaints=total_complaints,
        open_complaints=open_complaints,
        resolved_complaints=resolved_complaints,
        critical_complaints=critical_complaints,
        category_counts=category_counts,
    )


@main.route(
    "/complaint/<int:complaint_id>/update-status",
    methods=["POST"],
)
def update_complaint_status(complaint_id):
    new_status = request.form.get("status", "").strip()

    is_valid, message = validate_status(new_status)

    if not is_valid:
        flash(message, "error")
        return redirect(url_for("main.complaints"))

    connection = get_connection()

    try:
        complaint = connection.execute(
            "SELECT status FROM complaints WHERE id = ?",
            (complaint_id,),
        ).fetchone()

        if complaint is None:
            flash("Complaint not found.", "error")
            return redirect(url_for("main.complaints"))

        old_status = complaint["status"]
        updated_at = datetime.now().isoformat(timespec="seconds")
        resolved_at = updated_at if new_status == "Resolved" else None

        connection.execute(
            """
            UPDATE complaints
            SET status = ?, updated_at = ?, resolved_at = ?
            WHERE id = ?
            """,
            (new_status, updated_at, resolved_at, complaint_id),
        )

        connection.execute(
            """
            INSERT INTO complaint_updates (
                complaint_id,
                old_status,
                new_status,
                note,
                updated_by,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                complaint_id,
                old_status,
                new_status,
                "Complaint status updated",
                "Analyst",
                updated_at,
            ),
        )

        connection.commit()
        flash(
            f"Complaint #{complaint_id} status updated to {new_status}.",
            "success",
        )

    except Exception as error:
        connection.rollback()
        print(f"Status update error: {error}")
        flash("Unable to update complaint status.", "error")

    finally:
        connection.close()

    return redirect(url_for("main.complaints"))
