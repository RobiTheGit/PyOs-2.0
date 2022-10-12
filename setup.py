import os
import time
import subprocess
import getpass

def setpwd():
    f = open('user/password.pass', 'w')
    password = getpass.getpass('Password: ', stream=None)
    f.write(password)

print('This should only be ran when your first get PyOs')

try:
    print('making directories')
    os.mkdir('user/Apps')
    print('All Done with directories')
    setpwd()
except:
    setpwd()
