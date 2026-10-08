from app.validators import (
    validate_email,
    validate_phone,
    validate_complaint_text
)


print(validate_email("sneha@gmail.com"))
print(validate_email("wrong-email"))

print(validate_phone("9730832525"))
print(validate_phone("12345"))

print(validate_complaint_text(
    "My payment was deducted but the order is still showing as pending."
))