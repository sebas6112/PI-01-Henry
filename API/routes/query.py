import imp
from fastapi import APIRouter
from config.db import run_query

query = APIRouter()

@query.get("/")
def home():
    mes = 'Proyecto individual 01. Para navegar entre las consultas ingrese en la url las palabras query1 a la query4'
    return mes


@query.get("/query1")
def query1():
    q1 = str(run_query('''SELECT t1.year FROM 
                          (SELECT year, COUNT(*) AS qnty
                          FROM races
                          GROUP BY year
                          ORDER BY 2 DESC) t1
                          LIMIT 1;'''))
    q1 = q1.replace(',','')
    q1 = q1.replace('(','')
    q1 = q1.replace(')','')
    return 'El año con más carreras es: ' + q1

@query.get("/query2")
def query2():
    q2 = run_query('''SELECT d.forename AS forename, d.surname AS surname, COUNT(r.positionOrder)
                      FROM results as r
                      JOIN drivers as d 
                      ON (r.driverId = d.driverId)
                      WHERE r.positionOrder = 1
                      GROUP BY 1, 2
                      ORDER BY 3 DESC
                      LIMIT 1;''')
    q2 = 'El piloto con más primeros puestos es ' + str(q2[0][0]) + ' ' + str(q2[0][1]) + ' con ' + str(q2[0][2]) + ' victorias'
    return q2

@query.get("/query3")
def query3():
    q3 = run_query('''SELECT c.name AS name, COUNT(r.circuitId)
                      FROM circuits AS c
                      JOIN races AS r
                      ON (r.circuitId = c.circuitId)
                      GROUP BY r.circuitId
                      ORDER BY 2 DESC
                      LIMIT 1;''')
    q3 = 'El circuito más corrido es ' + str(q3[0][0]) + ' ' + 'con ' + str(q3[0][1]) + ' carreras'
    return q3

@query.get("/query4")
def query4():
    q4 = run_query('''SELECT d.forename, d.surname AS name, SUM(r.points) AS `total points`, c.nationality
                      FROM drivers AS d 
                      JOIN (results AS r, constructors AS c)
                      ON (r.constructorId = c.constructorId AND d.driverId = r.driverId)
                      WHERE c.nationality IN ('American','British')
                      GROUP BY r.driverId
                      ORDER BY 3 DESC
                      LIMIT 1;''')
    q4 = 'El piloto con mayor cantidad de puntos en total es:' + str(q4[0][0]) + ' ' + str(q4[0][1]) + ' con ' + str(q4[0][2]) + ' puntos en total de constructor de nacionalidad ' + str(q4[0][3])
    return q4