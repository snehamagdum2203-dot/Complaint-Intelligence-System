from app.categorizer import categorize_complaint


complaints = [
    "My order has not arrived yet.",
    "Money was deducted but payment failed.",
    "The product I received is damaged.",
    "I cannot login to my account.",
    "The application crashes when I open it.",
    "Customer support is not responding.",
    "I have a general question about my account."
]


for complaint in complaints:
    category = categorize_complaint(complaint)

    print(f"Complaint: {complaint}")
    print(f"Category : {category}")
    print("-" * 50)