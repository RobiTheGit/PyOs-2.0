import os
import getpass

def setpwd():
    f = open('user/password.pass', 'w')
    password = getpass.getpass('Password: ', stream=None)
    f.write(password)

setpwd()
