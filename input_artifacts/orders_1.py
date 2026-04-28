def create_order(product_id, quantity):
    # BUG: missing authorization check
    return {
        "status": "created",
        "product_id": product_id,
        "quantity": quantity
    }

def delete_order(order_id):
    # No verification that user owns this order
    return f"Order {order_id} deleted"
