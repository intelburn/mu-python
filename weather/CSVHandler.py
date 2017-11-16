from datetime import datetime
#This block of code is the function for getting the data from the CSV.
# This takes the path to the CSV file as the only argument.
# It returns a list of dictionaries.
# The keys for the dictionaries have the keys based on the first header line of the csv.
def GetData(csv, FS=',', DateField='date', YearField='year', TempField='temp'):
	WeatherData=[]
	with open(csv) as datum:
		data=datum.readlines()
	headers=data[0]
	headers=headers.split(FS)
	for item in headers:
		headers[headers.index(item)]=item.strip()
	for line in data[1:]:
		line=line.split(FS)
		attrib={}
		for item in line:
			index=line.index(item)
			item=item.strip()
			if headers[index]==DateField:
				attrib[headers[index]] = datetime.strptime(item, '%Y-%m-%d')
			elif YearField in headers[index]:
				attrib[headers[index]] = datetime.strptime(item, '%Y')
			elif TempField in headers[index]:
				attrib[headers[index]] = int(item)
			else:
				attrib[headers[index]] = float(item)
		for item in attrib.keys():
			if YearField in item:
				month=attrib[DateField].month
				day=attrib[DateField].day
				year=attrib[item].year
				attrib[item]=datetime(year, month, day)
		WeatherData.append(attrib)
	return WeatherData

#This calculates the delta value of a list of integers passed from the argument
def GetDelta(numbers):
	delta=0
	for number in numbers:
		delta+=number-numbers[0]
	return delta

#This will give you the average of a kind of weather either on an anual basis or on a monthly basis discarding the year
def GetAvg(csv, FS=',', Type='actual_mean_temp', Default='actual_mean_temp', DateField='date', Period="year", NeedSanityCheck=False):
	raw=GetData(csv=csv, FS=FS, DateField=DateField)
	Avg={}
	for day in raw:
		try:
			failsafe=day[Default]
		except KeyError:
			failsafe=Default
		if Period=="monthly":
			if day[DateField].year in Avg.keys():
				if day[DateField].month in Avg[day[DateField].year].keys():
					try:
						Avg[day[DateField].year][day[DateField].month]=(Avg[day[DateField].year][day[DateField].month]+day[Type])/2
					except KeyError:
						print("Bad Data at {0} or on {1}". format(raw.index(day), day[DateField]))
						Avg[day[DateField].year][day[DateField].month]=(Avg[day[DateField].year][day[DateField].month]+failsafe)/2
				else:
					try:
						Avg[day[DateField].year][day[DateField].month]=day[Type]
					except KeyError:
						print("Bad Data at {0} or on {1}". format(raw.index(day), day[DateField]))
						Avg[day[DateField].year][day[DateField].month]=failsafe
			else:
				try:
					Avg[day[DateField].year]={day[DateField].month:day[Type]}
				except KeyError:
					print("Bad Data at {0} or on {1}". format(raw.index(day), day[DateField]))
					Avg[day[DateField].year]={day[DateField].month:failsafe}
		else:
			if Period=="month":
				window=day[DateField].month
			else:
				window=day[DateField].year
			if window in Avg.keys():
				try:
					Avg[window]=(Avg[window] + day[Type])/2
				except KeyError:
					print("Bad Data at {0} or on {1}". format(raw.index(day), day[DateField]))
					Avg[window]=(Avg[window] + failsafe)/2
			else:
				try:
					Avg[window]=day[Type]
				except KeyError:
					print("Bad Data at {0} or on {1}". format(raw.index(day), day[DateField]))
					Avg[window]=failsafe
	return Avg

#This will return the greatest of a dictionary as a tuble
def GetGreatest(UnsortedDict):
	init=sorted(UnsortedDict.keys())
	biggest=(init[0], abs(UnsortedDict[init[0]]))
	for key in UnsortedDict.keys():
		if abs(UnsortedDict[key]) > biggest[1]:
			biggest=(key, abs(UnsortedDict[key]))
	return biggest
