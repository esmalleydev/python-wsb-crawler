# Python reddit web crawler

Use the ticker_import.py to insert your list of tickers to scan.

Replace mysql connection information in app_wsb.py and ticker_importer.py

Uses praw reddit

# Schema

## ticker
These are the stock symbols and names. Ex: `V` would be the code, `Visa` would be the name. Listing taken from nasdaq. 
```
+-----------+------------------+------+-----+---------+----------------+
| Field     | Type             | Null | Key | Default | Extra          |
+-----------+------------------+------+-----+---------+----------------+
| ticker_id | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| code      | varchar(10)      | YES  |     | NULL    |                |
| name      | varchar(255)     | YES  |     | NULL    |                |
| inactive  | tinyint(1)       | NO   |     | 0       |                |
| deleted   | tinyint(1)       | NO   |     | 0       |                |
+-----------+------------------+------+-----+---------+----------------+
```

## run
Everytime the script runs, it will insert a new `run` row.

```
+-----------+------------------+------+-----+---------------------+----------------+
| Field     | Type             | Null | Key | Default             | Extra          |
+-----------+------------------+------+-----+---------------------+----------------+
| run_id    | int(10) unsigned | NO   | PRI | NULL                | auto_increment |
| thread_id | int(10) unsigned | NO   |     | NULL                |                |
| completed | tinyint(1)       | YES  |     | 0                   |                |
| timestamp | datetime         | YES  |     | current_timestamp() |                |
| deleted   | tinyint(1)       | YES  |     | 0                   |                |
+-----------+------------------+------+-----+---------------------+----------------+
```

## thread
A `thread` would be the thread / post in a subreddit. `submission_id` points to the reddit id.
```
+---------------+------------------+------+-----+---------+----------------+
| Field         | Type             | Null | Key | Default | Extra          |
+---------------+------------------+------+-----+---------+----------------+
| thread_id     | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| submission_id | varchar(255)     | NO   |     | NULL    |                |
| title         | varchar(255)     | YES  |     | NULL    |                |
+---------------+------------------+------+-----+---------+----------------+
```

## user
The reddit user.
```
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
```

## user_mention
The important table, points to the run, which user made the comment, which ticker they talked about, and on what thread.
```
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
```



# Discord webhooks
Replace discord_webhook_url in app_wsb.py to post results in Discord

Example results:
```
WSB Runner: Script started
WSB Runner: Submission found: What Are Your Moves Tomorrow, October 12, 2022
WSB Runner: Finished finding comments
WSB Runner: Run finished
WSB Runner: BOE: mentioned 50, sum of karma: 235
WSB Runner: UK: mentioned 40, sum of karma: 278
WSB Runner: GME: mentioned 25, sum of karma: 39
WSB Runner: TSLA: mentioned 19, sum of karma: 61
WSB Runner: FOR: mentioned 14, sum of karma: 55
WSB Runner: ARE: mentioned 13, sum of karma: 94
WSB Runner: ON: mentioned 13, sum of karma: 78
WSB Runner: IT: mentioned 12, sum of karma: 57
WSB Runner: AMD: mentioned 12, sum of karma: 68
WSB Runner: AT: mentioned 10, sum of karma: 31
WSB Runner: Last 10 thread averages
WSB Runner: TSLA: mentioned 50.2, sum of karma: 174.6
WSB Runner: AMD: mentioned 49.0, sum of karma: 207.1
WSB Runner: TLRY: mentioned 27.5, sum of karma: 155.8
WSB Runner: ON: mentioned 17.4, sum of karma: 73.9
WSB Runner: GME: mentioned 16.2, sum of karma: 35.8
WSB Runner: AT: mentioned 13.6, sum of karma: 50.8
WSB Runner: FOR: mentioned 13.3, sum of karma: 47.1
WSB Runner: AAPL: mentioned 9.9, sum of karma: 29.5
WSB Runner: BOE: mentioned 9.6, sum of karma: 44.2
WSB Runner: EOD: mentioned 7.9, sum of karma: 26.6
WSB Runner: Updating users...
WSB Runner: Finished
```