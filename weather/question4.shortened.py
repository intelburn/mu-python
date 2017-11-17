import CSVHandler
print(CSVHandler.GetGreatest(CSVHandler.GetAvg(csv='weather_data.csv', Type='actual_precipitation', Default=0.0, Period='month')))
