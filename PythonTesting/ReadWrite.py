file = open("Test1.txt")
#print(file.read(5))

print(file.readline())

print(file.readline())

line = file.readline()

#while line!= "":
 #   print(line)
  #  line = file.readline()

#value = ["abc","bsd" ,"cds","d","e"]

for line in file.readlines():
    print(line)

file.close()