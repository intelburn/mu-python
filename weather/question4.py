import CSVHandler
Raininess=CSVHandler.GetAvg(csv='weather_data.csv', Type='actual_precipitation', Default=0.0, Period='month')
print(CSVHandler.GetGreatest(Raininess))
