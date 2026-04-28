def update_order(order_id, new_data):
    # BUG: no user validation
    order = get_order_from_db(order_id)
    # VULNERABILITY: anyone can modify any order
    return update_db(order_id, new_data)

def get_order_history(user_input):
    # No sanitization of user input
    query = f"SELECT * FROM orders WHERE user_id = {user_input}"
    return execute_query(query)
