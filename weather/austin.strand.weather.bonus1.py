import CSVHandler
from datetime import datetime
AvgMin=CSVHandler.GetAvg(csv='weather_data.csv', Type='actual_min_temp', Default='average_min_temp', Period='year')
AvgMax=CSVHandler.GetAvg(csv='weather_data.csv', Type='actual_max_temp', Default='average_max_temp', Period='year')
AvgPrecip=CSVHandler.GetAvg(csv='weather_data.csv', Type='actual_precipitation', Default='0.0', Period='year')
Weather={}
for year in AvgMin.keys():
	Weather[year]=(CSVHandler.GetDelta([AvgMin[year], AvgMax[year]]), AvgPrecip[year])
print(Weather)