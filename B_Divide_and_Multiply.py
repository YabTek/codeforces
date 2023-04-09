test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort(reverse = True)

    product = nums[0]
    odd_sum = 0
    even_count = 0

    for num in nums[1:]:
        if num % 2 == 0:
            product *= num
            even_count += 1
        else:
            odd_sum += num

    print(odd_sum + even_count + product)
     
   