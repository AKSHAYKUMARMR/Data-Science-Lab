fin = open("1st.txt", "rt")

data = fin.read()

data = data.replace('hello', 'python ')
fin.close()
fin = open("1st.txt", "wt")
fin.write(data)
fin.close()
