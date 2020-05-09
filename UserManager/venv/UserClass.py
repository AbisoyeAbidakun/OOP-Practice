



import random
import csv
from Authentication import authenticator


class User:
    database = "UserDatabase.csv"
    myData=[]
    id = 0

    def __init__(self, name, id_num,DOB,password, **kwargs):

        super().__init__(**kwargs)
        self.name = name
        self.DOB = DOB
        self.password = self._encrypt_(password)

    def _encrypt_pw(self, password):
        '''Encrypt the password with the username and return
        the sha digest.'''
        hash_string = (self.username + password)
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        '''Return True if the password is valid for this
        user, false otherwise.'''
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password


        # adds a user with entered attributes
    def addUser():
            # new version which includes a 'grabdate' function
            # grab date uses 'input()' but cleanses data
            # dates must b format "mm/dd/yy"
        newUser = User(input("please enter a name: "), input("please enter an 8 charater long password"),
             (str(functions.grabDate())))
        authenticator.add_user(newUser.username, newUser.password)









