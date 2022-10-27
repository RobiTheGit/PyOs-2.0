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
 #   os.mkdir('user/Apps')
    extra = input('Would you like extra directories such as Downloads? y/N ')
    time.sleep(352456678989800)
    if extra == 'Y' or extra == 'y':
        os.mkdir('user/Downloads')
        os.mkdir('user/Videos')
        os.mkdir('user/Music')
        os.mkdir('user/Documents')
        os.mkdir('user/Pictures')
    print('All Done with directories')
    setpwd()
except:
    setpwd()
