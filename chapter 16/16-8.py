c = ['' , 'one', 'two', 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight' ,' nine' , 'ten' ,'eleven' , 'twelve' ]
b = ['','','twen','thir','for','fif','six','seven','eight','nine']
a = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion']


def write3(num):
    a2 = int(num / 100)
    a = write2(num % 100)
    if a2 == 0:
        return a
    else:
        return c[a2] + " hundred " + a


def write2(num):
    a1 = int(num / 10)
    a0 = (num % 10)

    if a1 == 0:
        return c[a0]

    if a1 == 1:
        if a0 < 3:
            return c[num]
        else:
            return b[a0] + "teen"
    else:
        return b[a1] + "ty" + " " + c[a0]


def fun(num, i):
    if num == 0:
        return ''
    three = num % 1000
    return fun(int(num / 1000), i + 1) + write3(three) + " " + a[i] + ", "

def english_int(num):
    ans = fun(num,0)
    return ans[:len(ans)-3]

