s=['F', 'L', 'O', 'R', 'I', 'D', 'A']

def fun(x):
 return ord(x)
 
new_lis = list(map(fun, s))
new_dict = {} 
for i, j in zip(s,new_lis):
    new_dict[i] = j

print(new_dict)

771780030457