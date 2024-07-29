def linear_search(list, target): 
    """
    Returns index position of the target if found, else returns None
    """
    for i in range(0, len(list)): 
        if list[i] == target: 
            return i 
    return None

def verify(index): 
    if index is not None: 
        print("Target Index is:", index)
    else: 
        print("Target not in List")


numbers = [1,2,3,4,5,6,7,8,9,10] 

result = linear_search(numbers, 11)
verify(result)
