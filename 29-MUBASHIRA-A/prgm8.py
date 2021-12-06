with open("f1.py") as f:
    with open("f2.py", "w") as f1:
        for line in f:
            f1.write(line)
