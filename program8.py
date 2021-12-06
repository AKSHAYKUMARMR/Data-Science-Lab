with open("hi.txt") as f:
    with open("hello.txt","w") as f1:
        for line in f:
            f1.write(line)
fi=open("hello.txt")
li=fi.readlines()
for line in li:
    print(line)
