def promoteIn2(word , n , i):
	for num in range(n-1,i,-1):
		word[num + 2] = word[num]
	return word

def addTheSign(word , i):
    word[i] = '%'
    word[i+1] = '2'
    word[i+2] = '0'
    return word

def func(word, n):
	i = 0
	while i < n :
		if word[i] == ' ':
			word= promoteIn2(word, n, i)
			word= addTheSign(word,i)
			n  +=2
		i +=1
	return ''.join(word)


print(func(list("Mr John Smith    "), 13))
print(func(list('much ado about nothing      '),22))
