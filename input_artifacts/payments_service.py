def process_payment(user, amount):
    if amount < 0:
        print("Invalid amount")
    # BUG: no validation for user authentication
    return "Payment processed"