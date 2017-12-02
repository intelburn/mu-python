def IsPrime(PrimeCandidate):
	DivTest=True
	for PrimeBuster in range(2, PrimeCandidate):
		print("{0} % {1} = {2}".format(PrimeCandidate, PrimeBuster, PrimeCandidate%PrimeBuster))
		if PrimeCandidate % PrimeBuster == 0:
			DivTest=False
			break
	return DivTest

if IsPrime(int(input("Enter a positive number: "))) == True:
	print("The Number is Prime")
else:
	print("The Number is not Prime")
