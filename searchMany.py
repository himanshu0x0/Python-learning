def searchMany(s,x,k):
    count = 0
    for i in s:
        if i == x:
            count += 1
    if count == k:
        return True
    else:
        return False
    
print(searchMany([10,17,15,12],15,1))


