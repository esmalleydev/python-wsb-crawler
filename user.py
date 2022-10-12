
"""
+---------------+------------------+------+-----+---------------------+----------------+
| Field         | Type             | Null | Key | Default             | Extra          |
+---------------+------------------+------+-----+---------------------+----------------+
| user_id       | int(10) unsigned | NO   | PRI | NULL                | auto_increment |
| id            | varchar(255)     | YES  |     | NULL                |                |
| name          | varchar(255)     | YES  |     | NULL                |                |
| created_utc   | int(11) unsigned | YES  |     | NULL                |                |
| link_karma    | bigint(20)       | YES  |     | NULL                |                |
| comment_karma | bigint(20)       | YES  |     | NULL                |                |
| last_updated  | datetime         | NO   |     | current_timestamp() |                |
| deleted       | tinyint(1)       | NO   |     | 0                   |                |
+---------------+------------------+------+-----+---------------------+----------------+
"""
import datetime

class user:
	def __init__(self, connection):
		self.connection_ = connection

	def get_connection(self):
		return self.connection_

	def get_user_from_author_name(self, name):
		connection = self.get_connection()

		query = 'select * from user where name = "' + name + '" and deleted = "0"'

		mycursor = connection.cursor()
		mycursor.execute(query)

		columns = [col[0] for col in mycursor.description]
		rows = [dict(zip(columns, row)) for row in mycursor.fetchall()]

		if len(rows) == 0:
			query = 'insert into user (name) values ("' + name + '")'
			mycursor.execute(query)
			connection.commit()

		#todo reuse the result
		query = 'select * from user where name = "' + name + '" and deleted = "0"'

		mycursor = connection.cursor()
		mycursor.execute(query)

		columns = [col[0] for col in mycursor.description]
		rows = [dict(zip(columns, row)) for row in mycursor.fetchall()]

		for user in rows:
			return user

	def update_user(self, user_id, reddit_author):
		connection = self.get_connection()

		mycursor = connection.cursor()

		# todo check that user_id exists?
		# todo error handling

		query = 'update user set id = "' + str(reddit_author.id) + '", created_utc = "' + str(reddit_author.created_utc) + '", link_karma = "' + str(reddit_author.link_karma) + '", comment_karma = "' + str(reddit_author.comment_karma) + '", last_updated = "' + str(datetime.datetime.now()) + '" where user_id = "' + str(user_id) + '"'
		mycursor.execute(query)
		connection.commit()



