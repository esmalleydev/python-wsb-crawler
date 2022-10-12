
"""
+-----------+------------------+------+-----+---------------------+----------------+
| Field     | Type             | Null | Key | Default             | Extra          |
+-----------+------------------+------+-----+---------------------+----------------+
| run_id    | int(10) unsigned | NO   | PRI | NULL                | auto_increment |
| thread_id | int(10) unsigned | NO   |     | NULL                |                |
| completed | tinyint(1)       | YES  |     | 0                   |                |
| timestamp | datetime         | YES  |     | current_timestamp() |                |
| deleted   | tinyint(1)       | YES  |     | 0                   |                |
+-----------+------------------+------+-----+---------------------+----------------+
"""

class run:
	def __init__(self, connection):
		self.connection_ = connection


	def get_connection(self):
		return self.connection_

	def set_run_id(self, run_id):
		self.run_id_ = run_id

	def get_run_id(self):
		return self.run_id_

	def start(self, thread_id):
		connection = self.get_connection()

		#todo throw exception if no thread_id

		#todo if get_run_id is not null throw exception

		query = 'insert into run (thread_id) values ("' + str(thread_id) + '")'

		mycursor = connection.cursor()
		mycursor.execute(query)
		connection.commit()

		self.set_run_id(mycursor.lastrowid)

		return self.get_run_id()

	def end(self):
		connection = self.get_connection()

		#todo throw exception if no thread_id

		#todo if get_run_id is not null throw exception

		query = 'update run set completed = "1" where run_id = "' + str(self.get_run_id()) + '"'

		mycursor = connection.cursor()
		mycursor.execute(query)
		connection.commit()



