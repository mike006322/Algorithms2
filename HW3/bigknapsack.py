items = []
for line in open('knapsack_big.txt', 'r'):
    items.append(list(map(int, line.split())))
w = items[0][0]
n = items[0][1]
#print(n) #n = 2000 two thousand
#print(w) #w = 2000000 two million
'''
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
d = 0
for i in range(1, n+1):
    d = gcd(d, items[i][1])
print(d)
print(2000000/367)
'''
#from above testing, all weights have common divisor 367
#w / 367 = 5449.591280653951, w // 367 = 5449
#if any item exceeds (367*5449) capacity then it will be at least (367*(5449+1)) > w capacity
#therefore run the regular knapsack algorithm up to 5449 with all weights divided by 367 
#and then multiply the result by 
w = 5449
for i in range(1, n+1):
    items[i][1] = items[i][1]//367
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