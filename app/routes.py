from flask import Blueprint, render_template, request, redirect, url_for, flash

from app.complaint_service import create_complaint
from app.database import get_connection


main = Blueprint("main", __name__)


@main.route("/")
def home():
    return "Complaint Intelligence & Early Warning System is running!"


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
                "success"
            )
            return redirect(url_for("main.new_complaint"))

        flash(result, "error")

    return render_template("complaint_form.html")


@main.route("/complaints")
def complaints():

    connection = get_connection()

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

    connection.close()

    return render_template(
        "complaints.html",
        complaints=complaints_data
    )