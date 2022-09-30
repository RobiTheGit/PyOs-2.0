import webbrowser
import os
import sys
import subprocess
import colors
import time
import getpass
from datetime import date
import pyoslogo

correctpass = open('user/password.pass')
cpass = correctpass.read()
today = date.today()
nyd = date(today.year, 12, 31)
timetilnyd = nyd - today
white = colors.ccodes[0]
PyOsLogo = pyoslogo.PyOsLogo
theme = ''
username = getpass.getuser()

if today == date(today.year, 12, 25):
    todayholiday = 'Christmas'
    PyOsLogo =pyoslogo.PyOSLogoC
    
elif today == date(today.year, 12, 24):
    todayholiday = 'Christmas Eve'
    PyOsLogo =pyoslogo.PyOSLogoC
    
elif today == date(today.year , 1, 1 ):
    todayholiday = 'New Years Day'
    PyOsLogo = pyoslogo.PyOsLogoA
    
elif today == nyd:
    todayholiday = 'New Years Eve'
    PyOsLogo = pyoslogo.PyOsLogoA
    
elif today == date(today.year, 7, 4):
    todayholiday = 'Fourth of July'
    c1 = colors.ccodes[6]
    c2 = colors.ccodes[3]
    PyOsLogo = pyoslogo.PyOsLogoA
    
elif today == date(today.year, 10, 31):
    todayholiday = 'Halloween'
    PyOsLogo = pyoslogo.PyOSLogoH
    
elif today == date(today.year, 9, 28):
    todayholiday = "Dad's Birthday"
    PyOsLogo =pyoslogo.PyOSLogo
else:
    todayholiday = ''   
   
      
#*[x] App name*   
appslist = '''

Press Ctrl*Z to shutdown PyOs (not system)
'''
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
    print(f"""
    {PyOsLogo}                            
    """)
    time.sleep(2)
    subprocess.run('clear')
    os.chdir('user/Apps')
    apps()
    

def apps():
    print(appslist)
    print(f'Today is  {today}, Days til the new year, ', abs(timetilnyd.days))
    print('Holdiays:',todayholiday)
    print('Welcome', f'{username}')
    app = input(f'What app would you like to run? ')
    try:
        subprocess.run('clear')
        subprocess.run(f"python3 {app}.py", shell=True)
        recurse()
    except:
           webbrowser.open("https://github.com/RobiTheGit/PyOs/issues") 
           recurse()
        
def recurse():
    subprocess.run('clear')
    apps()
    recurse()
    
subprocess.run('clear')
print('Starting ...')
time.sleep(0.5)        
main()
