FibNums=[0, 1]
PrivIndex=1
PrivPrivIndex=0
MaxNums=int(input("How many Fibbonaci Numbahs you want? "))
if MaxNums > 2:
	for index in range(0, MaxNums):
		if index <= 1:
			print("{0} : {1}".format(index, FibNums[index]))
		else:
			FibNums.append(FibNums[PrivIndex]+FibNums[PrivPrivIndex])
			PrivIndex+=1
			PrivPrivIndex+=1
			print("{0} : {1}".format(index, FibNums[index]))
else:
	print("Please enter a number of 3 or greater")
