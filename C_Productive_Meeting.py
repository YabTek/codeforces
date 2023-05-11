import heapq

ans=[]
test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    nums = list(map(int,input().split()))
    tmp = []

    for i in range(len(nums)):
        nums[i] = (-1*nums[i],i+1)

    heapq.heapify(nums)

    while len(nums) > 1:
        num1,idx1 = heapq.heappop(nums)
        num2,idx2 = heapq.heappop(nums)

        num1 *= -1
        num2 *= -1

        flag1 = flag2 = False
        if num1 > 0:
            num1 -= 1
            heapq.heappush(nums,(-1*num1,idx1))
            flag1 = True
        if num2 > 0:
            num2 -= 1
            heapq.heappush(nums,(-1*num2,idx2))
            flag2 = True

        if flag1 and flag2:
            tmp.append((idx1,idx2))

    ans.append(len(tmp))
    ans += tmp


for i in range(len(ans)):
    if type(ans[i])==tuple:
        print(*ans[i])
    else:
        print(ans[i])

            
 


