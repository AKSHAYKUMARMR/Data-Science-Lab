fin = open("data.txt", "rt")
data = fin.read()
data = data.replace('Anjana', 'Anju')
fin.close()
#open the input file in write mode
fin = open("data.txt", "wt")
#overrite the input file with the resulting data
fin.write(data)
#close the file
fin.close()
