
"""
+---------------+------------------+------+-----+---------+----------------+
| Field         | Type             | Null | Key | Default | Extra          |
+---------------+------------------+------+-----+---------+----------------+
| thread_id     | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| submission_id | varchar(255)     | NO   |     | NULL    |                |
| title         | varchar(255)     | YES  |     | NULL    |                |
+---------------+------------------+------+-----+---------+----------------+
"""

class thread:
	def __init__(self, connection):
		self.connection_ = connection


	def get_connection(self):
		return self.connection_

	def set_submission(self, submission):
		self.submission_ = submission

	def get_submission(self, submission):
		return self.submission_

	def get_thread_id(self, submission):

		connection = self.get_connection()

		#todo throw exception if no submission

		query = 'select * from thread where submission_id = "' + str(submission.id) + '"'

		mycursor = connection.cursor()
		mycursor.execute(query)
		myresult = mycursor.fetchall()

		if len(myresult) == 0:
			# todo add thread created at date
			query = 'insert into thread (submission_id, title) values ("' + str(submission.id) + '", "' + str(submission.title) + '")'
			mycursor.execute(query)
			connection.commit()

			return mycursor.lastrowid


		for row in myresult:
			return row[0]
