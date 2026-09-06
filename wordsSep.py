def input_file(filename):
    user_input = input("Enter any data for file :")
    with open(filename, "w") as f:
        f.write(user_input)
        
def digit_words(filename):
    with open(filename, "r") as f:
        data = f.read().split()
        
        words = [word for word in data if word.isdigit()]
        for word in words:
            print(word)
        
filename = "input.txt"
input_file(filename)
digit_words(filename)
