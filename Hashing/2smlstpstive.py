def firstMissingPositive(nums):
        n = len(nums)
        for i in range(n):
            element = nums[i]
            while 1 <= element <= n and nums[element - 1] != element:
                nums[element - 1], nums[i] = nums[i], nums[element - 1]
                element = nums[i]

        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1

        return n + 1

nums = [0,-1,3,1]

print(firstMissingPositive(nums))