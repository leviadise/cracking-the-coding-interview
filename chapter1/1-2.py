import collections




def fun(word1,word2):

    c = collections.Counter()
    c.update(word1)

    for i in word2:
        if c[i] == 0:
            return False
        else:
            c[i] -= 1

    if len(list(c.elements())) != 0:
        return False

    return True



dataT = (
    ('abcd', 'bacd'),
    ('3563476', '7334566'),
    ('wef34f', 'wffe34'),
)
dataF = (
    ('abcd', 'd2cba'),
    ('2354', '1234'),
    ('dcw4f', 'dcw5f'),
)

for item in dataF:
    print(fun(item[0],item[1]))
