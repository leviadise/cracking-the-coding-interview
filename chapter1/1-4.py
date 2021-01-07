import collections
from collections import Counter

def palindrome_permutation(li):
	li = "".join(li).replace(" ","").lower()
	c = Counter(li)
	a = 0
	for i in li:
		if c[i] % 2 != 0 :
			if a != 0 :
				return False
			else:
				a +=1
	return True


data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

for exm,ans in data:
    if palindrome_permutation(list(exm)) != ans :
        print(exm)
