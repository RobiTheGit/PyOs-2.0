# Yes all the apps are just python files, sshh
import webbrowser
import os
import sys
import subprocess
import time
import getpass
import varis
import theme

correctpass = open('user/.password/password.pass')
cpass = correctpass.read()
PyOsLogo = varis.PyOsLogo
username = getpass.getuser()   
startdir = os.getcwd()
null = ''
red = varis.ccodes[6]
blue = varis.ccodes[3]
green = varis.ccodes[5]
yellow = varis.ccodes[4]
cyan = varis.ccodes[1]
magenta = varis.ccodes[2]
white = varis.ccodes[0]
print(theme.color1)
def login():
    if os.path.getsize('user/.password/password.pass') == 0:
        os.chdir(startdir+'/user/Apps')
        dirsetup()
    subprocess.run('clear')
    print(varis.PyOsLoginLogo)
    print(f'{theme.color1}Login for {username}')
    passw = getpass.getpass('Password: ', stream=None)
    if passw == cpass:
        os.chdir(startdir+'/user/Apps')
        dirsetup()
    else:
        print(f'{red}INVALID PASSWORD{theme.color1}')
        time.sleep(0.5)
        login()

def dirsetup():
    subprocess.run('clear')
    timer = time.ctime()
    print(f"""{theme.PyOsColor}
    {PyOsLogo}
    {theme.color1}                            
    """)
    print(f'{blue}Press Ctrl_Z or Ctrl_C to shutdown PyOs (not system){theme.color1}')
    print(f'Today is  {theme.color6}{varis.today}{theme.color1}, Days til the new year, {yellow}', abs(varis.timetilnyd.days))
    print(f'{theme.color1}Holdiays:',varis.todayholiday)
    print('Welcome', f'{theme.color5}{username}{theme.color1}')
    print(f'Time of login{theme.color3}', timer)
    print(f'{theme.color1}\n')
    l = os.getcwd()
    p=os.listdir(l)
    dirlist = []
    for i in p:
        if os.path.isdir(i):
            if i == '__pycache__' or i.startswith('.'):
                pass
            else:
                print(i)
                dirlist.append(1)
                
    if len(dirlist) is not 0:
        cd = input(f'{theme.color3}What category would you like to enter, type one of the caterorgies names in.{theme.color1}, else just press enter.\n> ')
        if cd is not null:
            if os.path.exists(cd):
                os.chdir(cd)
                subprocess.run('clear')
                dirsetup()
            else:
                print(f'{red}Category Does Not Exist!{theme.color1}')
                time.sleep(0.9)
                subprocess.run('clear')
                dirsetup()
        else:
            apps()    
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
    app = input(f'{theme.color4}What app would you like to run? \n{theme.color1}> ')
    try:
        if app+'.py' in os.listdir():
            subprocess.run('clear')
            subprocess.run(f"python3 {app}.py", shell=True)
            time.sleep(3)
            recurse()
        else:
            print(f'{red}No app found, check if there is a .py file with that name{theme.color1}')
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
