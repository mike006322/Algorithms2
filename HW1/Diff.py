wl = []
for line in open("jobs.txt", 'r'):
    wl.append(list(map(int,line.split())))
del wl[0]
diff = []
n = 10000
for i in range(n):
    #diff.append(wl[i][0] - wl[i][1]) #This line of code for the first problem
    diff.append(wl[i][0] / wl[i][1]) #This line of code for the second problem
    #make sure to run this as Python 3 to get floating point division
    
wldiff = list(zip(wl,diff))
wldiff.sort(key = lambda x: x[0][0], reverse = True)
wldiff.sort(key = lambda x: x[1], reverse = True)
#print(wldiff)
#element in wldiff is ([w,l],w-l) or ([w,l],w/l)

def wsct(wldiff):
    #weighted sum of completion time, Sum of weight*completion time, where completion time keeps growing by length
    s = 0
    ct = 0
    for job in wldiff:
        ct += job[0][1]
        s += job[0][0]*ct
        #print(ct, job[0][0])
    print(s)

wsct(wldiff)