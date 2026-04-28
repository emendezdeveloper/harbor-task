def send_error_notification(error_message):
    # BUG: information disclosure
    # VULNERABILITY: sensitive error details leaked
    notification = f"Error occurred: {error_message}"
    send_to_user(notification)

def debug_notification(debug_info):
    # Stack traces and internal data exposed
    message = f"Debug info: {debug_info}"
    return notify_admin(message)
