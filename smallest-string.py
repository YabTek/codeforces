test_cases = int(input())

for _ in range(test_cases):
    n,m,k = map(int,input().split())
    str1 = sorted(input())
    str2 = sorted(input())
    ans = []
    str1_ptr,str2_ptr = 0,0
    str1_operation,str2_operation = 0,0
  
    while str1_ptr < n and str2_ptr < m:
        if (str1[str1_ptr] < str2[str2_ptr] and str1_operation < k) or (str2_operation >= k) :
            ans.append(str1[str1_ptr])
            str1_operation += 1
            str2_operation = 0
            str1_ptr += 1
        else:
            ans.append(str2[str2_ptr])
            str2_operation += 1
            str1_operation = 0
            str2_ptr += 1
    print("".join(ans))
            
        