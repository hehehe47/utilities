import mysql.connector

client = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="suprice"
)

cursor = client.cursor()
cursor.execute(
    "select nyc2tyo.lowest_price from  suprice.nyc2tyo where startDate = '2020-02-27' and endDate = '2020-03-01';")
res = cursor.fetchall()
print(res)
