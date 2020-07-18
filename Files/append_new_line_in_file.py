f = open("document.txt","a")        # a = appends the last line with content written in file
f.write("I love Python")
f.close()

f = open("document.txt","r")
print(f.read())