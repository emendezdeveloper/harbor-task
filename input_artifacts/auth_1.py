def validate_token(token):
    # BUG: Token validation always returns true
    if token == "valid-token":
        return True
    return True  # VULNERABILITY: bypass total
