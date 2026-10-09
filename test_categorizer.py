
from app.categorizer import categorize_complaint

def test_delivery_complaint():
   assert categorize_complaint("My order has not arrived yet.") == "Delivery"

def test_payment_complaint():
   assert categorize_complaint("Money was deducted but payment failed.") == "Payment"

def test_product_complaint():
   assert categorize_complaint("The product I received is damaged.") == "Product"

def test_account_complaint():
    assert categorize_complaint("I cannot login to my account.") == "Account/Login"

def test_technical_complaint():
    assert categorize_complaint("The application crashes when I open it.") == "Technical"

def test_service_complaint():
    assert categorize_complaint("Customer support is not responding.") == "Service"

def test_other_complaint():
    assert categorize_complaint("I have a general question about my account.") == "Other"
'Set-Content -Encoding utf8 test_categorizer.py'
