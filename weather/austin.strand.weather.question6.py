from datetime import datetime
import CSVHandler
AvgData=CSVHandler.GetAvg(csv='weather_data.csv', Type="actual_mean_temp", Period="monthly")
print(AvgData)
AnualAvg=CSVHandler.GetAvg(csv='weather_data.csv')
print(AnualAvg)
