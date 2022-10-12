import mysql.connector

connection = mysql.connector.connect(
  user='TODO',
  password='TODO',
  host='TODO',
  database='TODO'
)

#https://www.nasdaq.com/market-activity/stocks/screener
import csv
with open('nasdaq.csv', newline='') as csvfile:
	row_reader = csv.reader(csvfile, delimiter=',')
	for row in row_reader:
		# clean up their trash
		code = row[0].strip().replace('"', '')
		name = row[1].strip().replace('"', '')


		query = 'select * from ticker where code = "' + str(code) + '"'

		mycursor = connection.cursor()
		mycursor.execute(query)
		myresult = mycursor.fetchall()

		if len(myresult) == 0:
			query = 'insert into ticker (code, name) values ("' + str(code) + '", "' + str(name) + '")'
			mycursor.execute(query)
			connection.commit()
			

