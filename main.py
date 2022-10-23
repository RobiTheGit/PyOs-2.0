# Yes all the apps are just python files, sshh
import webbrowser
import os
import sys
import subprocess
import time
import getpass
import pyoslogo
import holidays

correctpass = open('user/password.pass')
cpass = correctpass.read()
PyOsLogo = pyoslogo.PyOsLogo
username = getpass.getuser()   
startdir = os.getcwd()
null = ''
def login():
    subprocess.run('clear')
    print(pyoslogo.PyOsLoginLogo)
    print(f'Login for {username}')
    passw = getpass.getpass('Password: ', stream=None)
    if passw == cpass:
        dirsetup()
    else:
        print('INVALID PASSWORD')
        time.sleep(0.5)
        login()

def dirsetup():
    subprocess.run('clear')
    os.chdir(startdir+'/user/Apps')
    dirsetup()
    timer = time.ctime()
    print(f"""
    {PyOsLogo}                            
    """)
    print('Press Ctrl_Z or Ctrl_C to shutdown PyOs (not system)')
    print(f'Today is  {holidays.today}, Days til the new year, ', abs(holidays.timetilnyd.days))
    print('Holdiays:',holidays.todayholiday)
    print('Welcome', f'{username}')
    print('Time of login', timer)
    print('\n')
    l = os.getcwd()
    p=os.listdir(l)
    for i in p:
        if os.path.isdir(i):
            print(i)
    print('If there are any categories here, what category would you like to enter? If not, press enter, otherwise, type one of the caterorgies names in.')
    cd = input('> ')
    if cd is not null:
        if os.path.exists(cd):
            os.chdir(cd)
            subprocess.run('clear')
            dirsetup()
        else:
            print('Category Does Not Exist!')
            time.sleep(0.9)
            subprocess.run('clear')
            dirsetup()
    else:
        apps()
def apps():
    dir_path = os.getcwd()
    res = []
    for file in os.listdir(dir_path):
        if file.endswith('.py'):
            res.append(os.path.basename(file).split('.')[0])
    for x in range(len(res)):
        print(res[x])
    print('What app would you like to run?')
    app = input('> ')
    try:
        if app+'.py' in os.listdir():
            subprocess.run('clear')
            subprocess.run(f"python3 {app}.py", shell=True)
            recurse()
        else:
            print('No app found, check if there is a .py file with that name')
            time.sleep(0.9)
            recurse()
    except KeyboardInterrupt:
            sys.exit(0)
    except:
           webbrowser.open("https://github.com/RobiTheGit/PyOs-2.0/issues") 
           recurse()
        
def recurse():
    subprocess.run('clear')
    os.chdir(startdir+'/user/Apps')
    dirsetup()
    recurse()
    
if not sys.platform.startswith('win32') or not sys.platform.startswith('cygwin'):    
    subprocess.run('clear')
    print('Starting ...')
    time.sleep(0.5)        
    login()
else:
    print('To run this on Windows, you would need to remove the lockout code and modify it so programs would run properly, this is built to run on linux. If you are not willing to do that, run it on a linux machine or linux vm since most of the subprocess code is linux specific')
    sys.exit(0)
