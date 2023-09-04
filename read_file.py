import os

if os.path.exists("text_file.txt"):
    print("file exixts")

with open("text_file.txt", "r") as f:
#     print(f.read())
    for line in f:
        print(line, end=" ")
        
        
with open("text_file.txt", "w") as f:
    f.write("new text")
    

with open("text_file.txt", "r") as f:
    print(f.read())