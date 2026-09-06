def commasepdata():
    
    with open("myfile.txt","r") as f:
        data = f.read().strip() #removing extra spaces
        new_data = ",".join(data)
    
    with open("myfile.txt","w") as f:
        f.write(new_data)

    with open("myfile.txt","r") as f:
        print(f.read())
    
    
commasepdata()