# import data
file = open("data.txt","r",encoding="utf-8")
lineList = file.readlines()

# create output file
outFile = open("output.txt","w",encoding="utf-8")

# print(lineList)
for line in lineList:
    line.strip()

    cutTail = len(line)-5
    line = line[:cutTail]


    line.strip()
        
    print(line)

    for idx in range(1,len(line)):
        idx *= -1
        if line[idx] == ">":
            print(idx)
            print(line[idx+1:])
            word = line[idx+1:]

            for n in range(len(word)):
                if not word.isalpha():
                    word = word[:-1]
                else:
                    break
            
            outFile.write(word+";\n")

            # outFile.write(line[idx+1:].strip()+";"+"\n")
            break
    
    file.close
    outFile.close
