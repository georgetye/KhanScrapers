questionBank = []

source = "(Choice A)AFriends of opposite genders only marginally increased the likelihood of obesity for the ego., (Choice B)BObese persons do not seem to selectively form social ties only with other obese persons., (Choice C)CThere is almost no effect on the ego when someone in the same geographic proximity gained weight., (Choice D)DIf a mutual friend living far away gained weight, the ego would not be more likely to gain weight."

bracketSplit = source.split("(")

del bracketSplit[0]

letters = ["A)A","B)B","C)C","D)D"]

def letterSplit(list):
	index = 0
	answers = []
	for i in list:
		answers.append(i.split(letters[index])[1])
		answers[index] = answers[index].strip(', ')
		index += 1
	return answers

answerBank = letterSplit(bracketSplit)

print(answerBank)

#for i in bracketSplit:
	#for j in range(0, 4):
		#letterSplit = []
		#print(i)
		#print(letters[j])
		#letterSplit += i.split(letters[j])
		#print(letterSplit)
	

#print(letterSplit)