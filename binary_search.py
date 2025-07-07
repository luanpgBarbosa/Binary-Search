def binary_search(ordered_list, target):
    lower = 0
    higher = len(ordered_list) - 1
    
    while(lower <= higher):
        mid = (lower + higher) // 2
        shot = ordered_list[mid]
        
        if shot == target:
            return mid
        
        if shot < target:
            lower = mid + 1
            
        if shot > target:
            higher = mid - 1
    return None