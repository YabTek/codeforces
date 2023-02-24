test_cases = int(input())

for _ in range(test_cases):
    lst = []
    ans = []
    n = int(input())
    
    for i in range(n):
        lst.append(input())
    store = set(lst)
    
    for string in lst:
        cur_ans = 0
        ptr = 1
        while ptr <= len(string):
            if string[0:ptr] in store and string[ptr:] in store:
                cur_ans = 1
                break
            else:
                ptr += 1
        ans.append(str(cur_ans))
        
    print("".join(ans))
    
    

       
         
    