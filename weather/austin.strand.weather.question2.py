from datetime import datetime, timedelta
import CSVHandler
MaxTemps=CSVHandler.GetAvg(csv='weather_data.csv', FS=',', Type="actual_max_temp", Default='actual_mean_temp', DateField='date', Period='month')
print(MaxTemps)
winner=CSVHandler.GetGreatest(MaxTemps)
print(winner)
