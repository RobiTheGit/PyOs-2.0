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
def main():
    subprocess.run('clear')
    print(pyoslogo.PyOsLoginLogo)
    print(f'Login for {username}')
    passw = getpass.getpass('Password: ', stream=None)
    if passw == cpass:
        started()
    else:
        print('INVALID PASSWORD')
        time.sleep(0.5)
        main()
def started():
    subprocess.run('clear')
    os.chdir(startdir+'/user/Apps')
    apps()
    

def apps():
    print(f"""
    {PyOsLogo}                            
    """)
    print('Press Ctrl*Z to shutdown PyOs (not system)')
    print(f'Today is  {holidays.today}, Days til the new year, ', abs(holidays.timetilnyd.days))
    print('Holdiays:',holidays.todayholiday)
    print('Welcome', f'{username}')
    l = os.getcwd()
    p=os.listdir(l)
    for i in p:
        if os.path.isdir(i):
            print(i)
    cd = input('If there are any categories here, what category would you like to enter? ')
    if cd is not '' or cd is not ' ':
        os.chdir(cd)
        appcont()
    else:
        appcont()
def appcont():            
    app = input(f'What app would you like to run? ')
    try:
        if app+'.py' in os.listdir():
            subprocess.run('clear')
            subprocess.run(f"python3 {app}.py", shell=True)
            recurse()
        else:
            print('No app found, check if there is a .py file with that name')
            time.sleep(0.9)
            recurse()
    except:
           webbrowser.open("https://github.com/RobiTheGit/PyOs/issues") 
           recurse()
        
def recurse():
    subprocess.run('clear')
    os.chdir(startdir+'/user/Apps')
    apps()
    recurse()
    
subprocess.run('clear')
print('Starting ...')
time.sleep(0.5)        
main()
