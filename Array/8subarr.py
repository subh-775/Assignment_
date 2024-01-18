# LENGTH OF MINIMUM SUBARRAY

def minSubArrayLen(target: int, nums: list[int]) -> int:
        if target in nums:
            return 1
    
        if sum(nums) < target:
            return 0

        min_len = float('inf')
        current_sum = 0
        left = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0
