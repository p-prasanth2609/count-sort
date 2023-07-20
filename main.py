def countSort(arr):
    order=[0]*(max(arr)+1)
    sort=[]
    for i in arr:
        order[i]+=1
    for i in range(len(order)):
        sort+=[i for j in range(order[i])]
    return sort
print(countSort([4,3,2,1]))
