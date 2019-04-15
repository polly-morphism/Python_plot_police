"""
person,dept,eow,cause,cause_short,date,year,canine,dept_name,state
Constable Darius Quimby,"Albany County Constable's Office, NY","EOW: Monday, January 3, 1791",Cause of Death: Gunfire,Gunfire,1791-01-03,1791,FALSE,Albany County Constable's Office, NY
Sheriff Cornelius Hogeboom,"Columbia County Sheriff's Office, NY","EOW: Saturday, October 22, 1791",Cause of Death: Gunfire,Gunfire,1791-10-22,1791,FALSE,Columbia County Sheriff's Office, NY
Deputy Sheriff Isaac Smith,"Westchester County Sheriff's Department, NY","EOW: Thursday, May 17, 1792",Cause of Death: Gunfire,Gunfire,1792-05-17,1792,FALSE,Westchester County Sheriff's Department, NY
Marshal Robert Forsyth,"United States Department of Justice - United States Marshals Service, US","EOW: Saturday, January 11, 1794",Cause of Death: Gunfire,Gunfire,1794-01-11,1794,FALSE,United States Department of Justice - United States Marshals Service, US
Sheriff Robert Maxwell,"Greenville County Sheriff's Office, SC","EOW: Sunday, November 12, 1797",Cause of Death: Gunfire,Gunfire,1797-11-12,1797,FALSE,Greenville County Sheriff's Office, SC

"""
input_file = 'clean_data1.csv'
import re
import plotly
import plotly.graph_objs as go
from plotly import tools

"""
This set of functions parses the dataset, they subsequently return department, EOW, cause and year.
"""
def get_department(line):
    result = re.split(r'"', line, maxsplit=2)
    element = result[1].strip()
    return element, result[2:]

def get_eow(line):
    line = get_department(line)[1]
    result = re.split(r'"', str(line), maxsplit=2)
    element = re.split(r"'", str(result[1].strip()), maxsplit=2)[0][5:]
    return element, str(result[2:])[3:-7]

def get_cause(line):
    line = get_eow(line)[1]
    result = result = re.split(r",", line, maxsplit=2)
    element = re.split(r",", str(result[0].strip()), maxsplit=2)[0][16:]
    return element, result[1:]

def get_year(line):
    line = get_cause(line)[1]
    result = re.split(r'"', str(line[1]), maxsplit=2)
    element = re.split(r",", str(result[0].strip()), maxsplit=2)[0]
    return element

try:
   with open(input_file, encoding="utf-8", mode='r') as file:
       #printong first 5 lines of the dataset all parsed.
       file.readline()
       x = []
       y = []
       y1 = []
       for line in file:
           if not re.match(r'\w+',line):
               continue

           x.append(get_cause(line)[0])
           y.append(get_year(line))
           y1.append(get_department(line)[0])
       #Доделаю на выходных датасет и подумаю что-то с графиками. Второй график просто шедевр
       plotly.offline.plot({'data': [go.Bar(x=y, y=x)]},filename='myplots.html')
       plotly.offline.plot({'data': [go.Scatter(x=x, y=sorted(y1))]}, filename='myplots1.html')
       plotly.offline.plot({'data': [go.Scatter(x=x, y=y1)]}, filename='myplots2.html')





except IOError as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))

except ValueError as ve:
    print("Value error {0} in line {1}".format(ve, line_number))
