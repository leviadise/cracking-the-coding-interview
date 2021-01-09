def contiguous_sequence(numbers):
	n= len(numbers)
	ans = [0]*n
	ans[n-1] = numbers[n-1]
	for i in reversed(range(0,n-1)):
		ans[i] = max(numbers[i] + ans[i+1] , numbers[i] )
	return max(ans)


print(contiguous_sequence([2,-8,3,-2,4,-10]))
