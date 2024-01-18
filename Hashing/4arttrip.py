def arithmeticTriplets(nums: list[int], diff: int) -> int:
        num_to_indices = {}
        triplet_count = 0

        for i, num in enumerate(nums):
            num_to_indices[num] = i

        for i, num in enumerate(nums):
            second = num + diff
            third = second + diff

            if second in num_to_indices and third in num_to_indices:
                triplet_count += 1

        return triplet_count