# MAXMUM AREA

def maxArea(height: list[int]) -> int:
    start = 0
    en = len(height)-1
    maxarea = 0
    while start<en:
        area = min(height[start], height[en]) * (en - start)
        maxarea = max(maxarea, area)
        if height[start] < height[en]:
            start += 1
        else:
            en -= 1
    return maxarea
