import CSVHandler
from datetime import datetime, timedelta
MinTemps=CSVHandler.GetAvg(csv='weather_data.csv', Type='actual_min_temp', Default='average_min_temp', Period='month')
MaxTemps=CSVHandler.GetAvg(csv='weather_data.csv', Type='actual_max_temp', Default='average_max_temp', Period='month')
MonthDelta={}
for month in MinTemps.keys():
	MonthDelta[month]=CSVHandler.GetDelta(numbers=[MinTemps[month], MaxTemps[month]])
Dumb=CSVHandler.GetGreatest(MonthDelta)
print(Dumb)
print(MinTemps)
print(MaxTemps)
