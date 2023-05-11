import heapq


test_cases = int(input())

for _ in range(test_cases):
    n,m = map(int,input().split())
    nums1 = list(map(int,input().split()))
    nums2 = list(map(int,input().split()))

    for i in range(m):
        nums1.sort()
        nums1[0] = nums2[i]

    print(sum(nums1))

   
