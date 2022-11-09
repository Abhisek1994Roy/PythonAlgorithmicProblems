# https://leetcode.com/problems/find-triangular-sum-of-an-array/submissions/840311840/

def triangularSum(nums):
    if len(nums) == 1:
        return nums[-1]

    height = len(nums)

    def triange(height):
        if height == 1:
            return nums
        row = []
        arr = triange(height - 1)
        for i in range(0, len(arr) - 1):
            row.append((arr[i] + arr[i + 1]) % 10)
        return row

    return triange(height)[-1]


print(triangularSum([1, 2, 3, 4, 5]))
