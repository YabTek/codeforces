test_cases = int(input())

for _ in range(test_cases):
    mat = []
    row1 = list(map(int,input().split()))
    row2 = list(map(int,input().split()))
    mat.append(row1)
    mat.append(row2)
    
    
    if mat[0][0] < mat[0][1] and mat[0][0] < mat[1][0] and mat[0][1] < mat[1][1] and mat[1][0] < mat[1][1]:
            print("YES")
    elif mat[1][0] < mat[0][0] and mat[1][0] < mat[1][1] and mat[1][1] < mat[0][1] and mat[0][0] < mat[0][1]:
            print("YES")
    elif mat[1][1] < mat[1][0] and mat[1][1] < mat[0][1] and mat[0][1] < mat[0][0] and mat[1][0] < mat[0][0]:
            print("YES")
    elif mat[0][1] < mat[1][1] and mat[0][1] < mat[0][0] and mat[0][0] < mat[1][0] and mat[1][1] < mat[1][0]:
            print("YES")
    else:
        print("NO")
        
    