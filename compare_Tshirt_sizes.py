from collections import Counter
 
test_cases = int(input())
 
for _ in range(test_cases):
    lst = input().split()
    if (lst[0][-1] == 'L' and lst[1][-1] == 'M') or (lst[0][-1] == 'L' and lst[1][-1] == 'S'):
            print('>')
    elif (lst[0][-1] == 'M' and lst[1][-1] == 'S') or ( lst[0][-1] == 'L' and lst[1][-1] == 'M'):
            print('>')
    elif (lst[0][-1] == 'L' and lst[1][-1] == 'S') or (lst[0][-1] == 'M' and lst[1][-1] == 'S'):
            print('>')
    elif (lst[0][-1] == 'M' and lst[1][-1] == 'L') or (lst[0][-1] == 'S' and lst[1][-1] == 'M'):
            print('<')
    elif (lst[0][-1] == 'S' and lst[1][-1] == 'L'):
            print('<')
    elif (lst[0][-1] == 'L' and lst[1][-1] == 'L')   or (lst[0][-1] == 'S' and lst[1][-1] == 'S'):     
          if lst[0][-1]  == 'S':
              S1 = lst[0].count('X')
              S2 = lst[1].count('X')
              if S1 > S2:
                  print('<')
              elif S2 > S1:
                  print('>')
              else:
                  print('=')
          if lst[0][-1]  == 'L':
              L1 = lst[0].count('X')
              L2 = lst[1].count('X')
              if L1 > L2:
                  print('>')
              elif L1 < L2:
                  print('<')
              else:
                  print('=')
    else:
        print('=')
                
 