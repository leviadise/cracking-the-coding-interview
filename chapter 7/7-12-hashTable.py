
N=3
array = [[] for _ in range(N)]


def hash_func(x):
    return  set_key(x)%N

def set_key(x):
    n = len(x)
    key = 0
    for i in range(0,n):
        key += ord(x[i])*pow(128,i)
    return key

def insert(x):
    index = get_index(x)
    array[index].append(x)

def get_index(x):
    return hash_func(x)

def check(x):
    index = get_index(x)
    if remove(x) == True:
        insert(x)
        return True
    return False

def remove(x):
    index = get_index(x)
    try:
        array[index].remove(x)
    except:
        print("item : ", x, "is not in the table")
        return False
    return True

'''TEST'''

names= ["adi","erez","djdkmkm","dnsnsdind","nisnod","adi","csmoscpo"]

for i in names:
    insert(i)
    
for i in names:
    check(i)

for i in names:
    remove(i)
remove("ff")
print(array)
