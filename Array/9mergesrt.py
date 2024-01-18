# MERGE SORT

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    a = m - 1  
    b = n - 1  
    i = m + n - 1  

    while a >= 0 and b >= 0:
        num1 = nums1[a]
        num2 = nums2[b]

        if num1 >= num2:
            nums1[i] = num1
            a -= 1
        else:
            nums1[i] = num2
            b -= 1

        i -= 1

    while b >= 0:
        nums1[i] = nums2[b]
        b -= 1
        i -= 1
