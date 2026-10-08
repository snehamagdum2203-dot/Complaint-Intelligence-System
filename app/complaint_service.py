from datetime import datetime

from app.database import get_connection
from app.validators import (
    validate_customer_code,
    validate_name,
    validate_email,
    validate_phone,
    validate_complaint_text,
    validate_priority,
)
from app.categorizer import categorize_complaint


def create_complaint(
    customer_code,
    customer_name,
    email,
    phone,
    complaint_text,
    priority,
    department,
):
    # Validate customer details
    validations = [
        validate_customer_code(customer_code),
        validate_name(customer_name),
        validate_email(email),
        validate_phone(phone),
        validate_complaint_text(complaint_text),
        validate_priority(priority),
    ]

    for valid, message in validations:
        if not valid:
            return False, message

    # Automatically categorize complaint
    category = categorize_complaint(complaint_text)

    connection = get_connection()

    try:
        # Check if customer already exists
        customer = connection.execute(
            """
            SELECT id
            FROM customers
            WHERE customer_code = ?
            """,
            (customer_code,),
        ).fetchone()

        if customer:
            customer_id = customer["id"]

            connection.execute(
                """
                UPDATE customers
                SET name = ?, email = ?, phone = ?
                WHERE id = ?
                """,
                (customer_name, email, phone, customer_id),
            )

        else:
            cursor = connection.execute(
                """
                INSERT INTO customers
                (customer_code, name, email, phone)
                VALUES (?, ?, ?, ?)
                """,
                (customer_code, customer_name, email, phone),
            )

            customer_id = cursor.lastrowid

        created_at = datetime.now().isoformat(timespec="seconds")

        connection.execute(
            """
            INSERT INTO complaints
            (
                customer_id,
                complaint_text,
                category,
                priority,
                status,
                department,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                customer_id,
                complaint_text,
                category,
                priority,
                "Open",
                department,
                created_at,
            ),
        )

        connection.commit()

        return True, category

    except Exception as error:
        connection.rollback()
        return False, f"Unable to create complaint: {error}"

    finally:
        connection.close()