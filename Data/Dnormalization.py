## Importamos pandas y path para transformar y guardar los datos
import os
import pandas as pd
import shutil

## Se importa todo el conjunto de datos y se almacena cada tabla en un dataframe de pandas
drivers = pd.read_json('PI01_DATA03\Datasets\drivers.json',lines = True)
constructors = pd.read_json('PI01_DATA03\Datasets\constructors.json',lines = True)
circuits = pd.read_csv('PI01_DATA03\Datasets\circuits.csv')
races = pd.read_csv('PI01_DATA03/Datasets/races.csv')
## Se unen los archivos separados y se reinicia el índice del dataframe
qualifying = pd.concat([pd.read_json('PI01_DATA03\Datasets\Qualifying\qualifying_split_1.json'),
                        pd.read_json('PI01_DATA03\Datasets\Qualifying\qualifying_split_2.json')], ignore_index=True)
results = pd.read_json('PI01_DATA03/Datasets/results.json',lines = True)
pitStops = pd.read_json('PI01_DATA03\Datasets\pit_stops.json')
## Se unen los archivos separados y se les da un encabezado, además se reinicia el índice del dataframe
encabezadoLapTimes = ['raceId','driverId','lap','position','time','miliseconds']
lapTimes = pd.concat([pd.read_csv('PI01_DATA03\Datasets\lap_times\lap_times_split_1.csv', names = encabezadoLapTimes),
                      pd.read_csv('PI01_DATA03\Datasets\lap_times\lap_times_split_2.csv', names = encabezadoLapTimes),
                      pd.read_csv('PI01_DATA03\Datasets\lap_times\lap_times_split_3.csv', names = encabezadoLapTimes),
                      pd.read_csv('PI01_DATA03\Datasets\lap_times\lap_times_split_4.csv', names = encabezadoLapTimes),
                      pd.read_csv('PI01_DATA03\Datasets\lap_times\lap_times_split_5.csv', names = encabezadoLapTimes)],ignore_index=True)

## Se corrigen los datos faltantes con el valor NaN
drivers.replace('\\N','NULL',inplace=True)
races.replace('\\N','NULL',inplace=True)
qualifying.replace('\\N','NULL',inplace=True)
results.replace('\\N','NULL',inplace=True)

## Se normaliza el dataframe drivers desempaquetando la columna names que contiene diccionarios
## en las columnas forename y surname
nameDrivers = drivers['name']
drivers.drop(['name'], axis=1,inplace=True)
nameDrivers = pd.json_normalize(nameDrivers)
drivers = pd.concat([drivers, nameDrivers], axis=1)
## Se reordenan las columnas de la tabla drivers
drivers = drivers[['driverId','driverRef','number','code','forename','surname','dob','nationality','url']]
## Se remueven unas comas que ensuciaban los datos de la columna url
drivers['url'] = drivers['url'].replace(',','',regex=True)
circuits['url'] = circuits['url'].replace(',','',regex=True)

## Se comprueba si la carpeta existe para eliminarla y así exportar los datos nuevos
path = 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/NData'
if os.path.exists(path):
    shutil.rmtree(path)
os.makedirs(path, exist_ok=True)

## Se guardan todos los dataframes sin índices en una nueva carpeta con los datos normalizados
## para posteriormente montar una base de datos de MySQL
drivers.to_csv(path + '/drivers.csv',index=False)
constructors.to_csv(path + '/constructors.csv',index=False)
circuits.to_csv(path + '/circuits.csv',index=False)
races.to_csv(path + '/races.csv',index=False)
qualifying.to_csv(path + '/qualifying.csv',index=False)
results.to_csv(path + '/results.csv',index=False)
pitStops.to_csv(path + '/pitStops.csv',index=False)
lapTimes.to_csv(path + '/lapTimes.csv',index=False)
