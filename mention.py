
"""
todo?
+-------------------+------------------+------+-----+---------------------+----------------+
| Field             | Type             | Null | Key | Default             | Extra          |
+-------------------+------------------+------+-----+---------------------+----------------+
| mention_id        | int(10) unsigned | NO   | PRI | NULL                | auto_increment |
| run_id            | int(10) unsigned | NO   |     | NULL                |                |
| ticker            | varchar(10)      | YES  |     | NULL                |                |
| mentions          | int(10) unsigned | YES  |     | NULL                |                |
| sentiment_percent | int(10) unsigned | YES  |     | NULL                |                |
| timestamp         | datetime         | YES  |     | current_timestamp() |                |
| deleted           | tinyint(1)       | YES  |     | 0                   |                |
+-------------------+------------------+------+-----+---------------------+----------------+

"""

class mention:
	def __init__(self, connection):
		self.connection_ = connection



	def create(self):
		#todo?


