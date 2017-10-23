class Password_manager:

    def __init__(self, username):
        self.username = username
        self.old_passwords = ["password", "1234", "asdfghjkl"] #if there's an issue set this as a class attribute

    def get_password(self):
        try:
            print(self.old_passwords[-1])
        except IndexError: #if this doesn't work try ValueError, it's wider
            print("The password list is empty. Please choose a password.")

    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            print("Your password was successfully changed.")
        else:
            print("You have already used that password before. Please choose a new one.")

    def is_correct(self, attempt):
        try:
            if attempt == self.old_passwords[-1]:
                return True
            else:
                return False
        except TypeError:
            print("You did not input a string. Please try again.")
        except IndexError:
            print("There is no password yet. Please set a password.")            

user1 = passwordManager("Andrea")
user1.get_password()
user1.set_password("qwerty")
user1.get_password()
user1.set_password("password")
print(user1.is_correct("qwerty"))
