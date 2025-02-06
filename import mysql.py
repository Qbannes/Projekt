import mysql.connector

db = mysql.connector.connect(
 host="localhost",
 user="root",
 password="VudrkdwgwihsaE33#",
 database="sakila"
)

mycursor = db.cursor()

def anzeigen_film():
 mycursor.execute("SELECT * FROM film LIMIT 25")
 daten = mycursor.fetchall()
 for row in daten:
     print(row)
# Abfrage
def anzeigen_actor():
 mycursor.execute("SELECT * FROM actor LIMIT 25")
 daten = mycursor.fetchall()
 for row in daten:
     print(row)

anzeigen_film()
anzeigen_actor()

db.close()