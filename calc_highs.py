#####  High Comparison Script
#  Ethan Drower
#
#
#This script will look at the last 20 days, and determine
# if today's high was a new high for the stock
# If a new high has been reached, an entry into the
# Buy signal High table is made





def compTodayHigh(ticker):



    myquery = "SELECT * FROM " +  ticker + " ORDER BY id DESC LIMIT 20"
    db.query(myquery)

    res = db.store_result()
    rows = res.fetch_row(0, 1)
    curHigh = 0
    for row in rows:
    #print(row['highPrice'])
        if(row['highPrice'] > curHigh):
	    curHigh = row['highPrice']




    import time
    date = time.strftime('%Y-%m-%d')
    #print(date)

    todayQuery = "SELECT * FROM " + ticker + " WHERE date = '" + date + "'"
    db.query(todayQuery)
    res = db.store_result()

    row = res.fetch_row(1, 1)
    
    for item in row:
        if(item['highPrice'] == curHigh):
            print('its a new high! TIcker: ' + ticker )
	    writeHighBuySignal(ticker, date, curHigh)


def writeHighBuySignal(ticker, date, highPrice):
    insertQuery = "INSERT INTO BUY_SIGNALS " + " (ticker, highPrice, date) VALUES ('" + ticker + "', " + highPrice + ", '" + date + "')"
    db.query(insertQuery)


    



import MySQLdb
import _mysql



db = _mysql.connect(host="216.231.132.54", user="turtleUser",passwd="turtl3sp4ss",db="turtleDB")



import csv
with open('tickers.csv', 'rb') as f:
    reader = csv.reader(f)
    tickersList = list(reader)


for row in tickersList:
    for ticker in row[:-1]:
	compTodayHigh(ticker)        

