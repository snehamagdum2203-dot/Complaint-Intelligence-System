import re


def validate_customer_code(customer_code):
    if not customer_code:
        return False, "Customer code is required."

    if len(customer_code) < 3:
        return False, "Customer code must contain at least 3 characters."

    return True, ""


def validate_name(name):
    if not name:
        return False, "Name is required."

    if len(name.strip()) < 2:
        return False, "Name must contain at least 2 characters."

    return True, ""


def validate_email(email):
    if not email:
        return True, ""

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(pattern, email):
        return False, "Please enter a valid email address."

    return True, ""


def validate_phone(phone):
    if not phone:
        return True, ""

    if not phone.isdigit():
        return False, "Phone number must contain only digits."

    if len(phone) != 10:
        return False, "Phone number must contain exactly 10 digits."

    return True, ""


def validate_complaint_text(complaint_text):
    if not complaint_text:
        return False, "Complaint description is required."

    if len(complaint_text.strip()) < 10:
        return False, "Complaint description must contain at least 10 characters."

    return True, ""


def validate_category(category):
    allowed_categories = {
        "Delivery",
        "Payment",
        "Product",
        "Account/Login",
        "Technical",
        "Service",
        "Other"
    }

    if category not in allowed_categories:
        return False, "Invalid complaint category."

    return True, ""


def validate_priority(priority):
    allowed_priorities = {"Low", "Medium", "High", "Critical"}

    if priority not in allowed_priorities:
        return False, "Invalid priority."

    return True, ""


def validate_status(status):
    allowed_statuses = {
        "Open",
        "In Progress",
        "Resolved",
        "Closed"
    }

    if status not in allowed_statuses:
        return False, "Invalid complaint status."

    return True, ""