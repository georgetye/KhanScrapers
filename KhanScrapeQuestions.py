source = '''
*.kastatic.org, *.kasandbox.org, K–8th, High school and beyond, Fundamentals, Subjects, Subjects, Humanities, Art history, Subjects, Official SAT Practice, Other tests, Museums, Partners, Figure 1:  Percentage increase in obesity risk for an ego based upon his/her relationship with an alter.  The dependent variable in each model is the obesity of the ego. Independent variables include a time-lagged measurement of the ego’s obesity, the obesity of the alter, a time-lagged measurement of the alter’s obesity, the ego’s sex, age, and education. Mean effect sizes (solid black dot) and 95%95\%95%95, percent confidence intervals (line) are shown., Which conclusion is best supported by the findings in Figure 1?
'''

commaSplit = source.split("., ")
question = commaSplit[len(commaSplit)-1].strip('\n')

#del bracketSplit[0]

#letters = ["A)A","B)B","C)C","D)D"]

#def letterSplit(list):
#	index = 0
#	answers = []
#	for i in list:
#		answers.append(i.split(letters[index])[1])
#		answers[index] = answers[index].strip(', ')
#		index += 1
#	return answers

#answerBank = letterSplit(bracketSplit)

print(question)

#for i in bracketSplit:
	#for j in range(0, 4):
		#letterSplit = []
		#print(i)
		#print(letters[j])
		#letterSplit += i.split(letters[j])
		#print(letterSplit)
	

#print(letterSplit)