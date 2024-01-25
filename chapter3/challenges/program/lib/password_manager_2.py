# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: remove
#      Purpose: remove a password for a service
#      Arguments: one string representing a service name
#      Returns: None
#   4. Name: update
#      Purpose: update a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   5. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',
#                 (Optional) A string 'reverse' to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified
#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#
#       `!`, `@`, `$`, `%` or `&`
#
# And a new rule: passwords must be unique (not reused in other services).
#
# Example usage:
#   > password_manager = PasswordManager2()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('youtube', '3@245256')  # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.list_services()
#   ['gmail', 'facebook', 'youtube']
#   > password_manager.remove('facebook')
#   > password_manager.list_services()
#   ['gmail', 'youtube']
#   > password_manager.update('gmail', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('gmail')
#   '12ab5!678'
#   > password_manager.update('gmail', '%21321415')  # Valid password
#   > password_manager.get_for_service('gmail')
#   '%21321415'
#   > password_manager.sort_services_by('service')
#   ['gmail', 'youtube']
#   > password_manager.sort_services_by('added_on', 'reverse')
#   ['youtube', 'gmail']

# There are many more examples possible but the above should give you a good
# idea.

# == YOUR CODE ==

from datetime import datetime
class PasswordManager2():
    def __init__(self):
        self.user_passwords = {}
        
    def add(self, serv_name, password):
        if self.password_validator(password) and self.is_unique(password):
            self.user_passwords[serv_name] = password

        

    def remove(self, serv_name):
        del self.user_passwords[serv_name]

    def update(self, serv_name, password):
        if self.password_validator(password) and self.is_unique(password):
            self.user_passwords[serv_name] = password

    def list_services(self):
        services_with_passwords = [serv_name for serv_name, password in self.user_passwords.items() if password]

        return services_with_passwords

    def sort_services_by(self, arg, reverse=None):
        services_list = list(self.user_passwords.keys())
        sorted_list = sorted(services_list)

        if reverse != None and arg == 'service':
            return sorted_list[::-1]
        
        elif arg == 'service':
            return sorted_list
        
        elif reverse != None:
            return services_list[::-1]
        else:
            return services_list

    def get_for_service(self, serv_name):
        for key in self.user_passwords.keys():
            if serv_name == key:
                return self.user_passwords[key]
        
        return None

    def password_validator(self, password):
        return len(password) >= 8 and any(char in password for char in ['!', '@', '$', '%', '&'])
    
    def is_unique(self, password):
        for passw in self.user_passwords.values():
            if password == passw:
                return False
        return True
        