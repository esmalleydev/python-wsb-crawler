# Python reddit web crawler

Use the ticker_import.py to insert your list of tickers to scan.

Replace mysql connection information in app_wsb.py and ticker_importer.py


Uses praw reddit

schema used above each class

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