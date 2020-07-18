import os

if os.path.exists("document2.txt"):
    os.remove("document2.txt")
else:
    print("The file does not exist")


# for removing folder os.rmdir() function is used