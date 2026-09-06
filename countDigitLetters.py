def file_input(filename):
    user_input = input("Enter a input String :")
    with open(filename, "w") as f:
        f.write(user_input)
        
def count_digit_numbers(filename):
    digits = 0
    letters = 0
    with open(filename, "r") as f:
        data = f.read().split()
        for words in data:
            if words.isdigit():
                digits+=1
            elif words.isalpha():
                letters+=1
                
    print(f"Letters : {letters}")
    print(f"digits : {digits}")
        
filename = "input1.txt"
file_input(filename)
count_digit_numbers(filename)