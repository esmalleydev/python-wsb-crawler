
"""
+-------------------+------------------+------+-----+---------------------+----------------+
| Field             | Type             | Null | Key | Default             | Extra          |
+-------------------+------------------+------+-----+---------------------+----------------+
| user_mention_id   | int(10) unsigned | NO   | PRI | NULL                | auto_increment |
| user_id           | int(10) unsigned | NO   | MUL | NULL                |                |
| ticker_id         | int(10) unsigned | NO   | MUL | NULL                |                |
| thread_id         | int(10) unsigned | NO   | MUL | NULL                |                |
| run_id            | int(10) unsigned | NO   | MUL | NULL                |                |
| id                | varchar(255)     | YES  | MUL | NULL                |                |
| comment_karma     | int(10) unsigned | YES  |     | NULL                |                |
| sentiment_percent | int(10) unsigned | YES  |     | NULL                |                |
| timestamp         | datetime         | NO   |     | current_timestamp() |                |
| deleted           | tinyint(1)       | NO   |     | 0                   |                |
+-------------------+------------------+------+-----+---------------------+----------------+
"""

class user_mention:
	def __init__(self, connection):
		self.connection_ = connection
		self.user_id_ = None
		self.thread_id_ = None
		self.run_id_ = None


	def get_connection(self):
		return self.connection_

	def set_run_id(self, run_id):
		self.run_id_ = run_id

	def get_run_id(self):
		return self.run_id_

	def set_thread_id(self, thread_id):
		self.thread_id_ = thread_id

	def get_thread_id(self):
		return self.thread_id_

	def set_user_id(self, user_id):
		self.user_id_ = user_id

	def get_user_id(self):
		return self.user_id_


	def insert_user_mention(self, ticker_id, id_, comment_karma):
		connection = self.get_connection()

		mycursor = connection.cursor()

		# todo throw exceptions if thread_id / run_id / user_id is not set

		query = 'select * from user_mention where ticker_id = "' + str(ticker_id) + '" and thread_id = "' + str(self.get_thread_id()) + '" and user_id = "' + str(self.get_user_id()) + '" and id = "' + str(id_) + '" and deleted = "0"'

		mycursor.execute(query)

		columns = [col[0] for col in mycursor.description]
		rows = [dict(zip(columns, row)) for row in mycursor.fetchall()]


		if len(rows) == 0:
			query = 'insert into user_mention (user_id, ticker_id, thread_id, run_id, id, comment_karma) values ("' + str(self.get_user_id()) + '", "' + str(ticker_id) + '", "' + str(self.get_thread_id()) + '", "' + str(self.get_run_id()) + '", "' + str(id_) + '", "' + str(comment_karma) + '")'
			mycursor.execute(query)
			connection.commit()
		elif len(rows) == 1:
			for row in rows:
				query = 'update user_mention set run_id = "' + str(self.get_run_id()) + '", comment_karma = "' + str(comment_karma) + '" where user_mention_id = "' + str(row['user_mention_id']) + '"'
				mycursor.execute(query)
				connection.commit()




