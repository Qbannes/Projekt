import mysql.connector

db = mysql.connector.connect(
 host="localhost",
 user="root",
 password="VudrkdwgwihsaE33#"
)

mycursor = db.cursor()

mycursor.execute("DROP DATABASE sakila_3")

