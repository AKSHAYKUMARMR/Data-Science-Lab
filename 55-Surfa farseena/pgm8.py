
WITH OPEN("AB.TXT") AS F:
    WITH OPEN("CD.TXT","W") AS F1:
        FOR LINE IN F:
            F1.WRITE(LINE)
FI=OPEN("CD.TXT")
LI=FI.READLINES()
FOR LINE IN LI:
    PRINT(LINE)
