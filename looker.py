
print('Estamos en rpuebas')
import pandas as pd
from datetime import date as d
from datetime import datetime
from datetime import timedelta as td

fecha = d.today()
fecha = str(fecha)






    



# print(playerstats)



## Funciones 
def index_data(df2):
    df2.columns = ['date', 'time', 'Comp', 'Round', 'Day', 'Venue','Remo1','Remo2','Remo3', 'Opponent']
    return df2

def select_data(fecha,listafechas):
    delta = []
    fecha = datetime.strptime(fecha, '%Y-%m-%d')
    for i in range(len(listafechas)):
        listafechas[i] = datetime.strptime(listafechas[i], '%Y-%m-%d')
        delta.append(listafechas[i] - fecha if listafechas[i] > fecha else td.max)

    val, idx = min((val, idx) for (idx, val) in enumerate(delta))
    return idx

def loaddata(fecha,url):
    html = pd.read_html(url, header = 1)
    df = html[0]
    #raw = df.drop(df[df.Attendance].index) # Deletes repeating headers in content
    # raw = raw.fillna(0)
    #playerstats = raw.drop(['Attendance'], axis=1)
    df2 = df.iloc[:,:10]
    df2 = index_data(df2)
    #print(df2)
    dates= df2['date']
    car = select_data(fecha, dates)
    df2.drop(['Remo1', 'Remo2','Remo3'], axis=1, inplace=True)
    df2 = df2.iloc[car]
    #print(dates)
    #REMOVE COLUMNS OR ARROWS, AXIS =1 FOR COLUMNS
    #print(df.columns)
    return df2

def getvalues(url,team):
    url = url
    playerstats = loaddata(fecha,url)
    # print(playerstats)
    # print(playerstats['date'] , playerstats['Opponent'])
    fechanueva = pd.to_datetime(playerstats['date']).date()
    #fechanueva = datetime.strptime(str(fechanueva), '%d-%m-%Y')

    # print(fechanueva)
    return 'El '+team+ ' juega el ' + str(fechanueva) +' a las ' + str(playerstats['time']) + ' contra '+ playerstats['Opponent']

