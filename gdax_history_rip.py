import gdax
import time
import sys
import csv
import datetime
from random import randint

# Get start and stop time for bitcoin request from command line
#start = sys.argv[1]
#end = sys.argv[2]
outfile = sys.argv[1]
ff = open(outfile,'w')
public_client = gdax.PublicClient()
start_unixtime = 1509667140
#start_unixtime = 1501585200
end_unixtime = start_unixtime + 60*60*6
#days = 20

while(int(end_unixtime) <= 1509714300):
#while(int(end_unixtime) <= 1417431600 + 60*60*6+60*60*24*days):
    print("test")
    start = datetime.datetime.fromtimestamp(int(start_unixtime)).strftime('%Y-%m-%dT%H:%M:%S')
    end = datetime.datetime.fromtimestamp(int(end_unixtime)).strftime('%Y-%m-%dT%H:%M:%S')
    print(start,end)
    sleep_time = float(float(randint(8,10))/8)
    time.sleep(sleep_time)
    pricelist = public_client.get_product_historic_rates('BTC-USD',start=start,end=end,granularity=60)
    print(pricelist)
    pricelist = reversed(pricelist)
    new_data = csv.writer(ff,delimiter=',')

    for row in pricelist:
        mean = (row[1] + row[2])/2
        row.append(mean)
        new_data.writerow(row)
        #print(row)

    start_unixtime = end_unixtime
    end_unixtime += 60 * 60 * 6

ff.close()
