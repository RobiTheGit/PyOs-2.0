# Yes all the apps are just python files, sshh
import webbrowser
import os
import sys
import subprocess
import time
import getpass
import pyoslogo
import holidays
import colors

correctpass = open('user/.password/password.pass')
cpass = correctpass.read()
PyOsLogo = pyoslogo.PyOsLogo
username = getpass.getuser()   
startdir = os.getcwd()
null = ''
red = colors.ccodes[6]
blue = colors.ccodes[3]
green = colors.ccodes[5]
yellow = colors.ccodes[4]
cyan = colors.ccodes[1]
magenta = colors.ccodes[2]
white = colors.ccodes[0]
print(white)
def login():
    if os.path.getsize('user/.password/password.pass') == 0:
        os.chdir(startdir+'/user/Apps')
        dirsetup()
    subprocess.run('clear')
    print(pyoslogo.PyOsLoginLogo)
    print(f'{white}Login for {username}')
    passw = getpass.getpass('Password: ', stream=None)
    if passw == cpass:
        os.chdir(startdir+'/user/Apps')
        dirsetup()
    else:
        print(f'{red}INVALID PASSWORD{white}')
        time.sleep(0.5)
        login()

def dirsetup():
    subprocess.run('clear')
    timer = time.ctime()
    print(f"""{green}
    {PyOsLogo}
    {white}                            
    """)
    print(f'{blue}Press Ctrl_Z or Ctrl_C to shutdown PyOs (not system){white}')
    print(f'Today is  {yellow}{holidays.today}{white}, Days til the new year, {yellow}', abs(holidays.timetilnyd.days))
    print(f'{white}Holdiays:',holidays.todayholiday)
    print('Welcome', f'{green}{username}{white}')
    print(f'Time of login{blue}', timer)
    print(f'{white}\n')
    l = os.getcwd()
    p=os.listdir(l)
    for i in p:
        if os.path.isdir(i):
            print(i)
    cd = input(f'If there are any categories here, what category would you like to enter? If not, press enter, otherwise, type one of the caterorgies names in.\n> ')
    if cd is not null:
        if os.path.exists(cd):
            os.chdir(cd)
            subprocess.run('clear')
            dirsetup()
        else:
            print(f'{red}Category Does Not Exist!')
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
    app = input(f'{cyan}What app would you like to run? \n{white}> ')
    try:
        if app+'.py' in os.listdir():
            subprocess.run('clear')
            subprocess.run(f"python3 {app}.py", shell=True)
            recurse()
        else:
            print(f'{red}No app found, check if there is a .py file with that name{white}')
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
    print(f'{red}To run this on Windows, you would need to remove the lockout code and modify it so programs would run properly, this is built to run on linux. If you are not willing to do that, run it on a linux machine or linux vm since most of the subprocess code is linux specific.{white}')
    sys.exit(0)
