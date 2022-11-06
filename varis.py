from datetime import date
cnames = ['white 0', 'cyan 1', 'magenta 2', 'blue 3', 'yellow 4', 'green 5', 'red 6']
ccodes = ['\033[1;37;40m', '\033[1;36;40m', '\033[1;35;40m', '\033[1;34;40m', '\033[1;33;40m', '\033[1;32;40m', '\033[1;31;40m']
disptest ="""
\033[1;31;40m Bright Red     \033[0m [1;31;40m
\033[1;32;40m Bright Green   \033[0m [1;32;40m
\033[1;33;40m Yellow         \033[0m [1;33;40m
\033[1;34;40m Bright Blue    \033[0m [1;34;40m
\033[1;35;40m Bright Magenta \033[0m [1;35;40m
\033[1;36;40m Bright Cyan    \033[0m [1;36;40m
\033[1;37;40m White          \033[0m [1;37;40m
"""

PyOsLogoC ='''
  ____         ___      
 |  _ \ _   _ / _ \ ___ 2.0
 | |_) | | | | | | / __|
 |  __/| |_| | |_| \__ \\
 |_|    \__, |\___/|___/
        |___/
        
   *        *        *        __o    *       *
*      *       *        *    /_| _     *
   K  *     K      *        O'_)/ \  *    *
  <')____  <')____    __*   V   \  ) __  *
   \ ___ )--\ ___ )--( (    (___|__)/ /*     *
 *  |   |    |   |  * \ \____| |___/ /  *
    |*  |    |   | aos \____________/       *  
'''

PyOsLogoH = '''
  ____         ___                        .  
 |  _ \ _   _ / _ \ ___ 2.0              //  
 | |_) | | | | | | / __|       _.-"""""'//-'""""-._ 
 |  __/| |_| | |_| \__ \\     .', ,  , , : : ` ` `  `. 
 |_|    \__, |\___/|___/     / , , \\'-._ : :_.-'/ ` ` \
 
        |___/               / , ,  :\(_)\  /(_)/ : ` ` \
        
                           | , ,  ,  \__//\\\__/ . . ` ` |                          
                           | . .:_  : : '--`: : . _: ; :|
                           | : : \\\_  _' : _: :__// , , |
                           \ ` ` \\ \\/ \\/\\/ \\_/  / , , /
                           \ ` ` \\_/\\_/\\_/\\_/\\/ , , /
                            `._ ` . :  :  :  , , _.'
                             `-..............-' '''
                             
                             
PyOsLogoA ='''
  ____         ___      
 |  _ \ _   _ / _ \ ___ 2.0
 | |_) | | | | | | / __|
 |  __/| |_| | |_| \__ \\
 |_|    \__, |\___/|___/
        |___/           
                                   .''.
       .''.      .        *''*    :_\/_:     .
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :    /)\   ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::.  | ' *''*    * '.\'/.'_\(/_ '.':'.'
 : /\ : :::::  =  *_\/_*     -= o =- /)\     '  *
  '..'  ':::' === * /\ *     .'/.\'.  ' ._____
      *        |   *..*         :       |.   |' .---"|
        *      |     _           .--'|  ||   | _|    |
        *      |  .-'|       __  |   |  |    ||      |
     .-----.   |  |' |  ||  |  | |   |  |    ||      |
 ___'       ' /"\ |  '-."".    '-'   '-.'    '`      |____
jgs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  &                    ~-~-~-~-~-~-~-~-~-~   /|
 ejm97    )      ~-~-~-~-~-~-~-~  /|~       /_|\
        _-H-__  -~-~-~-~-~-~     /_|\    -~======-~
~-\XXXXXXXXXX/~     ~-~-~-~     /__|_\ ~-~-~-~
~-~-~-~-~-~    ~-~~-~-~-~-~    ========  ~-~-~-~
      ~-~~-~-~-~-~-~-~-~-~-~-~-~ ~-~~-~-~-~-~
                        ~-~~-~-~-~-~
'''

PyOsLogo = '''
  ____         ___      
 |  _ \ _   _ / _ \ ___  2.0
 | |_) | | | | | | / __|
 |  __/| |_| | |_| \__ \\ 
 |_|    \__, |\___/|___/
        |___/           
'''
 
PyOsLoginLogo = '''

  ____         ___           _                _       
 |  _ \ _   _ / _ \ ___ 2.0 | |    ___   __ _(_)_ __  
 | |_) | | | | | | / __|    | |   / _ \ / _` | | '_ \  
 |  __/| |_| | |_| \__ \    | |__| (_) | (_| | | | | |
 |_|    \__, |\___/|___/    |_____\___/ \__, |_|_| |_|
        |___/                           |___/         
'''    
today = date.today()
nyd = date(today.year, 12, 31)
timetilnyd = nyd - today

if today == date(today.year, 12, 25):
    todayholiday = 'Christmas'
    PyOsLogo = PyOsLogoC
    
elif today == date(today.year, 12, 24):
    todayholiday = 'Christmas Eve'
    PyOsLogo = PyOsLogoC
    
elif today == date(today.year , 1, 1 ):
    todayholiday = 'New Years Day'
    PyOsLogo = PyOsLogoA
    
elif today == nyd:
    todayholiday = 'New Years Eve'
    PyOsLogo = PyOsLogoA
    
elif today == date(today.year, 7, 4):
    todayholiday = 'Fourth of July'
    c1 = colors.ccodes[6]
    c2 = colors.ccodes[3]
    PyOsLogo = PyOsLogoA
    
elif today == date(today.year, 10, 31):
    todayholiday = 'Halloween'
    PyOsLogo = PyOsLogoH
    
elif today == date(today.year, 9, 28):
    todayholiday = "Dad's Birthday"
    PyOsLogo = PyOsLogo

elif today == date(today.year, 11, 3):
    todayholiday = "My Birthday"
    PyOsLogo = PyOsLogo
else:
    todayholiday = ''
    PyOsLogo = PyOsLogo
