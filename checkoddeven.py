count = 0
with open("pnumbers.txt", "r") as f:
    data = f.read().strip()
    
    nums = data.split(",")
    for val in nums:
        val = val.strip()
        if val.isdigit():
            if(int(val)%2==0):
                count+=1
print(count)