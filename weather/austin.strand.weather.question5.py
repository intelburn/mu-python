from datetime import datetime, timedelta
import CSVHandler
raw=CSVHandler.GetData('weather_data.csv')
AboveAvg=0
BelowAvg=0
bad=0
for day in raw:
	try:
		actual=day['actual_precipitation']
		avg=day['average_precipitation']
	except KeyError:
		print("Bad Data at {0} or on {1}".format(raw.index(day), day['date']))
		bad+=1
		continue
	if actual > avg:
		AboveAvg+=1
	elif avg > actual:
		BelowAvg+=1
print (AboveAvg)
print (BelowAvg)
print (bad)
