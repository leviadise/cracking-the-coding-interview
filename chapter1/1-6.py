def string_compression(word):
    prev = word[0]
    cur = ''
    number = 0
    newWord = ''

    for i in range(0,len(word)):
        cur = word[i]
        if cur != prev :
            newWord += prev + str(number)
            number = 1
        else:
            number += 1

        prev = cur

    newWord += prev + str(number)
    if len(newWord) > len(word):
        return word
    else:
        return newWord


'''Test Cases'''
data = [
 ('aabcccccaaa', 'a2b1c5a3'),
 ('abcdef', 'abcdef')
]

for exm,ans in data:
    if string_compression(exm) != ans:
         print(exm)
