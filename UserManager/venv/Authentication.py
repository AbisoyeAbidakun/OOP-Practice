


class AuthException(Exception):

    def __init__(self, name,Id_Num, user):

        super().__init__(name,user)
        self.name = name
        self.user = user

class NameAlreadyExist(AuthException):
    pass

class Id_NumAlreadyExist(AuthException):
    pass

class InvalidUsername(AuthException):
    print("Invalid Username, please enter a valid username")
class InvalidPassword(AuthException):
    print ("Password is Invalid,please enter a valid password")

class Authenticator:
    def __init__(self):
        '''Construct an authenticator to manage
        users logging in and out.'''
        self.users = {}

    def add_user(self, username,password):
        if username in self.users:
            raise NameAlreadyExists(username)
        if len(password) < 8:
            raise PasswordTooShort(username)
        self.users[username] = User(username,password)


authenticator = Authenticator()
