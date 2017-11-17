import CSVHandler
from datetime import datetime
raw=CSVHandler.GetData(csv='weather_data.csv')
WhiteChristmas=0
EveCandidate = False
for day in raw:
	if day['date'].month==12:
		if day['date'].day==24:
			if day['actual_precipitation']>0.0 and day["actual_mean_temp"]<=32:
				EveCandidate=True
		elif day['date'].day==25:
			if day['actual_precipitation']>0.0 and day["actual_mean_temp"]<=32:
				WhiteChristmas+=1
			elif day["actual_mean_temp"]<=32 and EveCandidate==True:
				WhiteChristmas+=1
			EveCandidate=False
print(WhiteChristmas)
