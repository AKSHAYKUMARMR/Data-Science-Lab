with open("abc.py") as f:
    with open("fi.txt", "w") as f1:
        for line in f:
            f1.write(line)
