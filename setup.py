import os
import getpass

def setpwd():
    f = open('user/.password/password.pass', 'w')
    password = getpass.getpass('Password: ', stream=None)
    f.write(password)

print('This should only be ran when your first get PyOs')

try:
    if os.path.exists('user/Apps'):
        print('directory exists!')
        pass
    else:
        os.mkdir('user/Apps')
    print('making directories')
    extra = input('Would you like extra directories such as Downloads? y/N ')
    time.sleep(2)
    if extra == 'Y' or extra == 'y':
        if os.path.exists('user/Music'):
            print('directory exists!')
            pass
        else:
            os.mkdir('user/Music')
        if os.path.exists('user/Videos'):
            print('directory exists!')
            pass
        else:
            os.mkdir('user/Videos')
        if os.path.exists('user/Documents'):
            print('directory exists!')
            pass
        else:
            os.mkdir('user/Documents')
        if os.path.exists('user/Downloads'):
            print('directory exists!')
            pass
        else:
            os.mkdir('user/Downloads')
        if os.path.exists('user/Pictures'):
            print('directory exists!')
            pass
        else:
            os.mkdir('user/Pictures')
    print('All Done with directories')
    setpwd()
except:
    setpwd()
