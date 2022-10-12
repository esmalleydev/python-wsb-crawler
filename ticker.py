
"""
+-----------+------------------+------+-----+---------+----------------+
| Field     | Type             | Null | Key | Default | Extra          |
+-----------+------------------+------+-----+---------+----------------+
| ticker_id | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| code      | varchar(10)      | YES  |     | NULL    |                |
| name      | varchar(255)     | YES  |     | NULL    |                |
| inactive  | tinyint(1)       | NO   |     | 0       |                |
| deleted   | tinyint(1)       | NO   |     | 0       |                |
+-----------+------------------+------+-----+---------+----------------+
"""

class ticker:
	def __init__(self, connection):
		self.connection_ = connection
		self.tickers_ = None


	def get_connection(self):
		return self.connection_

	def get_ticker_id(self, ticker_code):
		tickers = self.get_tickers_()

		if tickers.get(ticker_code):
			return tickers[ticker_code]
		
		return None


	def set_tickers_(self, tickers):
		self.tickers_ = tickers

	# if tickers set, return, else get the tickers and reverse code -> id
	def get_tickers_(self):

		if self.tickers_:
			return self.tickers_

		connection = self.get_connection()

		mycursor = connection.cursor()

		tickers = {}

		query = 'select * from ticker where inactive = "0" and deleted = "0"';
		mycursor.execute(query)

		columns = [col[0] for col in mycursor.description]
		rows = [dict(zip(columns, row)) for row in mycursor.fetchall()]

		for ticker in rows:
			tickers[ticker['code']] = ticker['ticker_id']

		self.set_tickers_(tickers)

		return self.get_tickers_()

