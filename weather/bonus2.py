import CSVHandler
#run pip3 install holidays
import holidays
import statistics
raw=CSVHandler.GetData(csv='weather_data.csv')
MinAvg=[]
MaxAvg=[]
for day in raw:
	if holidays.UnitedStates().get(day['date'])=='Thanksgiving':
		MinAvg.append(day['actual_min_temp'])
		MaxAvg.append(day['actual_max_temp'])
print("Max temp will be {0}".format(statistics.mean(MaxAvg)))
print("Min temp will be {0}".format(statistics.mean(MinAvg)))