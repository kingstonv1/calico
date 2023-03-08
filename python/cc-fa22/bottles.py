for _ in range(int(input())):
    input()
    students = {}
    wait, temp = 0, 0
    ans = ""
    nums = list(map(int, input().split()))
    for i in range(1, len(nums) + 1):
        students[i] = nums[i - 1]
    srted = {k: v for k, v in sorted(students.items(), key=lambda item: item[1])}
    for i in srted.values():
        temp += i
        wait += temp
    print(wait)
    for i in srted.keys():
        ans += (str(i) + " ")
    print(ans[:-1])
