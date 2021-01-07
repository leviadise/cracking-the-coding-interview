def magic_index(A,i,j):

    if i > j :
        return False

    p =  int( (i+j)/2 )

    if A[p] == p:
        return True
    if A[p] < p :
        return magic_index(A,i,p-1)
    else:
        return magic_index(A,p+1,j)

data= [[0,1,3,4,5,7,7,7,8,9],[1,1,2,3,4,45,666,777,888] , [2,3,4] ]

for d in data:
    print(magic_index(d,0,len(d)-1))
