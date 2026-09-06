def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()

        if(data.find(word) != -1): #if word in data     
            print("Found")
        else:
            print("not found")

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data :
                print(line_no)
                return
            line_no += 1
    return -1

check_for_line()

