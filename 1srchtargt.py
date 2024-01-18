# SEARCH TARGET

def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    
    while right >= left:
        mid = (right + left) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    
    return -1



nums = [-1,0,3,5,9,12]
target = 2
print(search(nums, target))