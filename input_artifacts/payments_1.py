def process_payment(amount, card_number):
    # BUG: no authentication validation
    if amount < 0:
        print("Invalid amount")
    # VULNERABILITY: no user identity check
    return charge_card(card_number, amount)

def refund_payment(transaction_id, amount):
    # No auth needed
    return execute_refund(transaction_id, amount)
