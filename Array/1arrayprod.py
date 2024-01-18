# PRODUCT EXCEPT SELF

def productExceptSelf(nums: list[int]) -> list[int]:
        n = len(nums)
        pre_prod = 1 # 4
        post_prod = 1
        result = [0]*n
        for i in range(n):
            result[i] = pre_prod
            pre_prod *= nums[i]
        for i in range(n-1,-1,-1):
            result[i] *= post_prod
            post_prod *= nums[i]
        return result

arr = [1, 2, 3, 4, 5]

res = [1, 1, 2, ]
