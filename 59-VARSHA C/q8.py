with open("q1.py") as f:
    with open("copy.py", "w") as f1:
        for line in f:
            f1.write(line)
