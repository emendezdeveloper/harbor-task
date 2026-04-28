def validate_payment(user_id, amount):
    # BUG: no amount validation
    if amount > 0:
        return True
    # VULNERABILITY: negative amounts bypass validation
    return False

def deduct_balance(account, amount):
    # No minimum balance check
    new_balance = account["balance"] - amount
    return update_account(account, new_balance)
