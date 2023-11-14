n = int(input())
for i in range(n):
    temp = input()
    if len(temp)>10:
        print(temp[0]+str(len(temp)-2)+temp[-1])
    else:
        print(temp)