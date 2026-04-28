def log_notification(user_input):
    # BUG: log injection vulnerability
    # VULNERABILITY: user input directly in logs
    log_message = f"User action: {user_input}"
    write_to_log(log_message)

def audit_event(event_type, details):
    # No sanitization of event details
    log_line = f"{event_type}|{details}"
    append_to_audit_log(log_line)
