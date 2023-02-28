nums = [-1, 0, 1]

def trib(count, n):
    if n == 0:
        return 0
    
    if len(nums) == n + 2:
        return nums[-1]

    nums.append(nums[count] + nums[count - 1] + nums[count - 2])
    return trib(count + 1, n)


for _ in range(int(input())):
    print(trib(2, int(input())))
    nums = [-1, 0, 1]