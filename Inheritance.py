class User(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def login(self, name, password):
        print("Logged successfully with {0} and password {1}".format(self, name, password))

    def logout(self, name):
        print("Logged out successfully with {}".format(self, name))


class Admin(User):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        User.__init__(self, name, password)

    def delete_user(self, name):
        print("User {} is successfully deleted!".format(self, name))


class Guest(User):
    def __init__(self, name):
        self.name = "Guest"
        User.__init__(self, name, "Password")

    def login(self, name, password):
        print("Error, invalid.")