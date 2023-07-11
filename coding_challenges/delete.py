def numbers_sum(lst):
	sum = 0
	for i in lst:
		if type(i)==int:
			sum+=i
	return sum
	
res = numbers_sum([1,2,3,'4'])
print(res)
	
def numbers_sum(lst):
  return sum(i for i in lst if type(i) == int)


