
from app.validators import (
    validate_email,
    validate_phone,
    validate_complaint_text,
)


def test_valid_email():
    is_valid, message = validate_email("sneha@gmail.com")
    assert is_valid is True


def test_invalid_email():
    is_valid, message = validate_email("wrong-email")
    assert is_valid is False


def test_valid_phone():
    is_valid, message = validate_phone("9730832525")
    assert is_valid is True


def test_invalid_phone():
    is_valid, message = validate_phone("12345")
    assert is_valid is False


def test_valid_complaint_text():
    is_valid, message = validate_complaint_text(
        "My payment was deducted but the order is still showing as pending."
    )
    assert is_valid is True
'Set-Content -Encoding utf8 test_validation.py'