import os
import getpass

def setpwd():
    f = open('user/.password/password.pass', 'w')
    password = getpass.getpass('Password: ', stream=None)
    f.write(password)
    print('Password Set!')
setpwd()
