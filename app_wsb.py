import requests
import mysql.connector
import traceback

import time

import praw
from praw.models import MoreComments


discord_webhook_url = "TODO"

discord_data = {
  #"content" : "message content",
  "username" : "WSB Runner"
}

# todo is there a better way to catch exceptions in python?
try:
  from ticker import ticker

  from thread import thread
  from run import run
  from user import user
  from user_mention import user_mention

  connection = mysql.connector.connect(
    user='TODO',
    password='TODO',
    host='TODO',
    database='TODO'
  )

  # todo is there a better way to initialize all these?
  ticker = ticker(connection)
  thread = thread(connection)
  run = run(connection)
  user = user(connection)
  user_mention = user_mention(connection)

  reddit = praw.Reddit(
    client_id="TODO",
    client_secret="TODO",
    user_agent="TODO"
  )

  discord_data['content'] = 'Script started'
  requests.post(discord_webhook_url, json = discord_data)

  subreddit = reddit.subreddit('wallstreetbets')

  # todo better logic to find correct submission
  submission_id = subreddit.sticky()

  submission = reddit.submission(id=submission_id)

  discord_data['content'] = 'Submission found: ' + submission.title
  requests.post(discord_webhook_url, json = discord_data)

  thread_id = thread.get_thread_id(submission)

  run_id = run.start(thread_id)

  user_mention.set_thread_id(thread_id)
  user_mention.set_run_id(run_id)

  submission.comments.replace_more(limit=None)

  discord_data['content'] = 'Finished finding comments'
  requests.post(discord_webhook_url, json = discord_data)

  reddit_name_x_user_id = {}

  for top_level_comment in submission.comments:
    comment = top_level_comment.body
    comment_split = list(set(comment.split(' ')))

    user_mention.set_user_id(None)
    

    for word in comment_split:
      cleaned_word = word.replace("$", "")
      ticker_id = ticker.get_ticker_id(cleaned_word)

      if ticker_id:
        # only get the user once
        if user_mention.get_user_id() is None:
          user_ = user.get_user_from_author_name(str(top_level_comment.author))
          reddit_name_x_user_id[user_['name']] = user_['user_id']
          user_mention.set_user_id(user_['user_id'])

        user_mention.insert_user_mention(ticker_id, top_level_comment.id, top_level_comment.score)


  run.end();

  discord_data['content'] = 'Run finished'
  requests.post(discord_webhook_url, json = discord_data)

  query = 'select user_mention.*, ticker.code, count(*) as `mentions`, sum(comment_karma) as `sum_of_karma` from user_mention join ticker on ticker.ticker_id = user_mention.ticker_id where run_id = "'+str(run_id)+'" group by ticker_id order by mentions desc'

  discord_data['content'] = '```' + query + '```'
  requests.post(discord_webhook_url, json = discord_data)

  mycursor = connection.cursor()
  mycursor.execute(query)

  columns = [col[0] for col in mycursor.description]
  rows = [dict(zip(columns, row)) for row in mycursor.fetchall()]


  # post first 10 results
  posted = 0
  for row in rows:
    if posted >= 10:
      break
    discord_data['content'] = str(row['code']) + ': mentioned ' + str(row['mentions']) + ', sum of karma: ' + str(row['sum_of_karma'])
    requests.post(discord_webhook_url, json = discord_data)
    time.sleep(1)
    posted = posted + 1


  # spamming discord too much I think
  time.sleep(10)

  discord_data['content'] = 'Last 10 thread averages'
  requests.post(discord_webhook_url, json = discord_data)

  query = 'select * from thread order by thread_id desc limit 10';

  mycursor = connection.cursor()
  mycursor.execute(query)

  columns = [col[0] for col in mycursor.description]
  threads = [dict(zip(columns, row)) for row in mycursor.fetchall()]

  averages = {}

  for thread in threads:
    query = 'select * from run where completed = "1" and thread_id = "' + str(thread['thread_id']) + '" order by run_id desc limit 1';

    mycursor = connection.cursor()
    mycursor.execute(query)

    columns = [col[0] for col in mycursor.description]
    runs = [dict(zip(columns, row)) for row in mycursor.fetchall()]

    for run in runs:
      query = 'select user_mention.*, ticker.code, count(*) as `mentions`, sum(comment_karma) as `sum_of_karma` from user_mention join ticker on ticker.ticker_id = user_mention.ticker_id where run_id = "'+str(run['run_id'])+'" group by ticker_id order by mentions desc'

      mycursor = connection.cursor()
      mycursor.execute(query)

      columns = [col[0] for col in mycursor.description]
      rows = [dict(zip(columns, row)) for row in mycursor.fetchall()]

      posted = 0
      for row in rows:
        if posted >= 10:
          break

        if averages.get(row['code']) == None:
          averages[row['code']] = {}
          averages[row['code']]['code'] = row['code']
          averages[row['code']]['mentions'] = 0
          averages[row['code']]['sum_of_karma'] = 0

        averages[row['code']]['mentions'] = averages[row['code']]['mentions'] + row['mentions']
        averages[row['code']]['sum_of_karma'] = averages[row['code']]['sum_of_karma'] + row['sum_of_karma']
        posted = posted + 1


  posted = 0
  for s in sorted(averages.items(), key=lambda k_v: k_v[1]['mentions'], reverse=True):
    if posted >= 10:
      break
    discord_data['content'] = str(s[1]['code']) + ': mentioned ' + str(s[1]['mentions'] / 10) + ', sum of karma: ' + str(s[1]['sum_of_karma'] / 10)
    requests.post(discord_webhook_url, json = discord_data)
    time.sleep(1)
    posted = posted + 1


  discord_data['content'] = 'Updating users...'
  requests.post(discord_webhook_url, json = discord_data)

  for redditor_name in reddit_name_x_user_id:
    author = reddit.redditor(redditor_name)

    if hasattr(author, 'id'):
      user.update_user(reddit_name_x_user_id[redditor_name], author)


  discord_data['content'] = 'Finished'
  requests.post(discord_webhook_url, json = discord_data)




except Exception as e:
  discord_data['content'] = str(traceback.format_exc())
  requests.post(discord_webhook_url, json = discord_data)
  quit()




















