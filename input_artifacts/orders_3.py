def change_order_status(order_id, new_status):
    # BUG: privilege escalation - no role check
    if new_status in ["pending", "shipped", "delivered", "refunded"]:
        update_order(order_id, {"status": new_status})
        return True
    # VULNERABILITY: regular users can refund orders

def grant_discount(order_id, discount_percent):
    # No admin check - anyone can grant discounts
    return apply_discount(order_id, discount_percent)
