# MEDIAN OF SORTED ARRAYS

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        out_lst = []
        a = 0
        b = 0
        for i in range(len(nums1)+len(nums2)):
            if a==len(nums1):
                for j in range(b, len(nums2)):
                    out_lst.append(nums2[j])
                break
            elif b==len(nums2):
                for j in range(a, len(nums1)):
                    out_lst.append(nums1[j])
                break
            out_lst.append(min(nums1[a], nums2[b]))
            if nums1[a] <= nums2[b]:
                a+=1
            elif nums1[a] >= nums2[b]:
                b+=1

        mid = len(out_lst) // 2
        res = (out_lst[mid] + out_lst[~mid]) / 2
        return res

nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))