import re


CATEGORY_KEYWORDS = {
    "Delivery": [
        "delivery",
        "delivered",
        "shipment",
        "shipping",
        "late delivery",
        "delivery delay",
        "order not arrived",
        "order has not arrived",
        "not received",
        "haven't received",
        "hasn't arrived",
        "arrived late"
    ],
    "Payment": [
        "payment",
        "paid",
        "refund",
        "money",
        "transaction",
        "charged",
        "deducted",
        "billing"
    ],
    "Product": [
        "product",
        "damaged",
        "broken",
        "defective",
        "quality",
        "wrong item",
        "missing item"
    ],
    "Account/Login": [
        "login",
        "log in",
        "password",
        "sign in",
        "otp",
        "locked account",
        "cannot login",
        "can't login",
        "unable to login"
    ],
    "Technical": [
        "error",
        "bug",
        "crash",
        "crashes",
        "not working",
        "website",
        "application",
        "app",
        "server",
        "system error"
    ],
    "Service": [
        "service",
        "support",
        "staff",
        "agent",
        "response",
        "help",
        "not responding"
    ]
}


def categorize_complaint(text):
    text = text.lower().strip()

    if not text:
        return "Other"

    category_scores = {
        category: 0
        for category in CATEGORY_KEYWORDS
    }

    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if re.search(r"\b" + re.escape(keyword) + r"\b", text):
                category_scores[category] += 1

    best_category = max(
        category_scores,
        key=category_scores.get
    )

    if category_scores[best_category] == 0:
        return "Other"

    return best_category