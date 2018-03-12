items = []
for line in open('knapsack1.txt', 'r'):
    items.append(list(map(int, line.split())))
w = items[0][0]
n = items[0][1]
#items = items[1:] Leaving items[0] so that list starts on index 1
column = [0]*(w+1)
A = [0]*(n+1)
for i in range(n+1):
    A[i] = column[:]
for i in range(1, n+1):
    for x in range(w+1):
        if items[i][1] > x: 
            A[i][x] = A[i-1][x]
        else:
            A[i][x] = max([A[i-1][x], A[i-1][x-items[i][1]] + items[i][0]])
print(A[n][w])