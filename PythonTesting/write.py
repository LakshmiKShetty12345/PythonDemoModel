with open('Test1.txt','r') as reader:
    content = reader.readlines()#reading the data
    reversed(content) #The dta got reversed
    with open('Test1.txt','w') as writer:
        for text in  content:
            writer.write(text) #write the data




