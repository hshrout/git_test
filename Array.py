#Array 

new_list = [1,2,3]
result = new_list[0]

print(result)

if 1 in new_list: print(True)
'''
for i in new_list: 
    if i == 2: 
        print(True)
    else:
        print(False)
'''

numbers = []
print(len(numbers))

numbers.append(5)
numbers.append(30)

numbers.extend([6,7,8])
print(numbers)