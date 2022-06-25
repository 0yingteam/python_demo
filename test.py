
f = open("test.txt","w")

for i in range(0,999999):
    while (len(str(i))!=6):
        i = "0" + str(i)
    f.write(str(i) + "\r")
f.close()
    
    
