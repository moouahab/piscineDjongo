if __name__ == '__main__':
	intVar = 42
	print(intVar, "est de type", type(intVar))

	strVar = "42"
	print(strVar, "est de type", type(strVar))

	strVar = "quarante-deux"
	print(strVar, "est de type", type(strVar))

	floatVar = 42.0
	print(floatVar, "est de type", type(floatVar))

	boolVar = True
	print(boolVar, "est de type", type(boolVar))

	listVar = [42]
	print(listVar, "est de type", type(listVar))

	myDict = {42 : 42}
	print(myDict, "est de type", type(myDict))

	myTuple = (42,)
	print(myTuple, "est de type", type(myTuple))
	mySet = set()
	print(mySet, "est de type", type(mySet))