from datetime import date

today = date.today()
nyd = date(today.year, 12, 31)
timetilnyd = nyd - today

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