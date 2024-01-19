# == INSTRUCTIONS ==
#
# Purpose: Validate a password
# Parameters: one, a string
# Rules:
#   - It must be longer than 7 characters (8 is fine)
#   - It must contain at least one of the following special characters:` !`, `@`,
#     `$`, `%` or `&`
# Returns: a boolean (True if valid, False otherwise)
# Example:
#   Call:    is_valid("1234567")
#   Returns: False
#   Call:    is_valid("12345678")
#   Returns: False
#   Call:    is_valid("12345!78")
#   Returns: True

# == YOUR CODE ==

def is_valid(password):
    # chechking if password at least 8 character long
    if len(password) < 8:
        return False
    
    # password must contain one of these special characters
    spec_char = ['!', '@', '$', '%', '&']

    # looping through spec characters, chehcking if their in the password
    for char in spec_char:
        if char in password:
            return True
    return False