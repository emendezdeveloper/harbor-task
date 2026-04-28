def get_transaction_details(transaction_id):
    user_id = extract_user_id()
    # BUG: SQL injection risk
    query = f"SELECT * FROM transactions WHERE id = {transaction_id} AND user = '{user_id}'"
    # VULNERABILITY: unsanitized transaction_id
    return execute_sql(query)

def log_payment(user, amount):
    # Direct SQL concatenation
    log_query = f"INSERT INTO logs VALUES('{user}', {amount})"
    execute_sql(log_query)
