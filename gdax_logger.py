import gdax
import time
import sys
import csv
import datetime
from random import randint
from datetime import timedelta
import os

# Get start and stop time for bitcoin request from command line
#start = sys.argv[1]
#end = sys.argv[2]
outfile = '/home/ken/Documents/tf/coins/scripts/outz_tmp.csv'
ff = open(outfile,'w')
public_client = gdax.PublicClient()

# Check what the most recent timestamp recorded is
with open('/home/ken/Documents/tf/coins/scripts/BTC-price-history/BTC_price_history.csv',"r") as f1:
    last_line = f1.readlines()[-1]

last_time_stamp = int(last_line.split(',')[0])

# Get the current time
current_date = datetime.datetime.now()
new_date = current_date.replace(minute=0,second=0,microsecond=0)
#time_check_date = new_date - timedelta(hours=1)
time_check_date = new_date - timedelta(hours=1)

start_unixtime = time.mktime(time_check_date.timetuple())
#start_unixtime = 1501585200
#end_unixtime = start_unixtime + 60*60*6
end_unixtime = start_unixtime + 60*60*6
#days = 20

#while(int(end_unixtime) <= 1509642000):
#while(int(end_unixtime) <= 1417431600 + 60*60*6+60*60*24*days):
    #print("test")
start = datetime.datetime.fromtimestamp(int(start_unixtime)).strftime('%Y-%m-%dT%H:%M:%S')
end = datetime.datetime.fromtimestamp(int(end_unixtime)).strftime('%Y-%m-%dT%H:%M:%S')
print(start,end)
    #sleep_time = float(float(randint(8,10))/10)
    #time.sleep(sleep_time)
pricelist = public_client.get_product_historic_rates('BTC-USD',start=start,end=end,granularity=60)
#print(pricelist)
pricelist = reversed(pricelist)
new_data = csv.writer(ff,delimiter=',')

for row in pricelist:
    mean = (row[1] + row[2])/2
    row.append(mean)
    if int(row[0]) > last_time_stamp:
        new_data.writerow(row)
    #print(row)

#start_unixtime = end_unixtime
#end_unixtime += 60 * 60 * 6

ff.close()

fin = open(outfile,"r")
data2 = fin.read()
fin.close()
fout = open('/home/ken/Documents/tf/coins/scripts/BTC-price-history/BTC_price_history.csv',"a")
fout.write(data2)
fout.close()

os.remove(outfile)
