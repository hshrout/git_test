#Recursive_Binary

def recusive_binary(list, target): 
    if len(list) == 0:
        return False
    else: 
        midpoint = (len(list)) //2

        if list[midpoint] == target:
            return True
        else: 
            if list[midpoint] < target: 
                return recusive_binary(list[midpoint+1:], target)
            else: 
                return recusive_binary(list[:midpoint], target)

def verify(result): 
    print("Target Found", result)

numbers = (1,2,3,4,5,6,7,8)   
result = recusive_binary(numbers, 10)
verify(result)

result = recusive_binary(numbers, 5)
verify(result)

