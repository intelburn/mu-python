from datetime import datetime
import CSVHandler
YearAvg=CSVHandler.GetAvg(csv='weather_data.csv', FS=',', Type='actual_mean_temp', Period='year')
YearDelta={}
for year in YearAvg.keys():
	if year > datetime.now().year-3:
		break
	YearDelta[year]=CSVHandler.GetDelta(numbers=[YearAvg[year], YearAvg[year+1], YearAvg[year+2]])
GreatestDelta=CSVHandler.GetGreatest(UnsortedDict=YearDelta)
print("The biggest change in mean temperature happened in the period betweem {0}-{1}. The delta in mean temperature was {2}. {0} had a mean temperature of {3}. {4} had a mean temperature of {5}. {1} had a mean temperature of {6}.".format(GreatestDelta[0], GreatestDelta[0]+2, int(GreatestDelta[1]), int(YearAvg[GreatestDelta[0]]), GreatestDelta[0]+1, int(YearAvg[GreatestDelta[0]+1]), int(YearAvg[GreatestDelta[0]+2])))
