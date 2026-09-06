f = open("sample.txt", "r+")
f.write("hello, ABC is a demo file")
print(f.read())
f.close()