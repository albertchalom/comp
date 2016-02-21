def swapchars (str):
	import collections
	c = collections.Counter(str).most_common()
	max = c[0][0]
	min = c[len(c)-1][0]
	newstr = ''
	for letter in str:
		if (letter == max):
			letter = min
		elif (letter == min):
			letter = max
		newstr = ''.join((newstr, letter))
	return (newstr)

def sortcat (numStrs, *parameters):
	lst = []
	for str in parameters:
		lst.append(str)
	returnStr = ''
	lastLongestWord = ''
	if numStrs == -1:
		numStrs = len(lst)
	for num in range (0, numStrs):
		length = -1
		longestWord = ''
		for string in lst:
			if len(string) > length:
				length = len(string)
				longestWord = string
		returnStr = ''.join((returnStr, longestWord))
		lst.remove(longestWord)
	return returnStr




fil = open ('states.txt', 'r')
line = fil.readline()
abbrevToState = {}
while(line != ""):
	state = ''
	abbrev = ''
	seenComma = 0
	for char in line:
		if (char == ',' or char == '\n'):
			seenComma = 1
		elif(seenComma):
			abbrev+=char
		else:
			state+=char
	abbrevToState[abbrev] = state
	line = fil.readline()


def blues_clues (stateAbbreviation):
	return abbrevToState[stateAbbreviation]

def blues_booze (stateName):
	for key in abbrevToState:
		if(abbrevToState[key] == stateName):
			return (key)
	#If we wanted to return multiple abbreviations, we would take in a list as a parameter
	#and either return a list, or print the state names
















 	


