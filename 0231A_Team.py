n = int(input())
count = 0
for i in range(n):
    temp = list(map(int,input().split()))
    if sum(temp) >1:
        count += 1
print(count)

# problems
# I used sum to represent the count previously