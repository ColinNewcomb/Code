#Problem 1
def q1(aDict):
    MaxValue=(float("-Inf"))
    for key in aDict:
        if MaxValue < aDict[key]:
            MaxValue=aDict[key]
    return MaxValue

#Problem 2
def q2(aDict,num):
    aList=[]
    for key in aDict:
        if aDict[key] == num:
            aList.append(key)
    return aList

#Problem 3
def q3(aList,string):
    bList=[]
    for dictionary in aList:
        if string in dictionary:
            bList.append(dictionary)
    return bList

#Problem 4
def q4(aList,num):
    bList=[]
    for dictionary in aList:
        if num in dictionary.values():
            bList.append(dictionary)
    return bList

#Problem 5
def q5(aDict,bDict):
    cDict={}
    for key, value in aDict.items():
        cDict[key]= value
    for key, value in bDict.items():
        if key in cDict:
            cDict[key] += value
        else:
            cDict[key] = value
    return cDict

#Problem 6
def q6(aDict,bDict):
    cDict={}
    for key in aDict.keys():
        if key in bDict:
            cDict[key]=[aDict[key],bDict[key]]
    return cDict

#Problem 7
def q7(filename):
    aList=[]
    with open(filename,"r") as fp:
        for line in fp:
            words=line.split(' ')
            for word in words:
                if word and word not in aList:
                    aList.append(word)
    return aList

#Problem 8
def q8(inputfile,outputfile):
    with open(inputfile,"r") as intf:
        with open(outputfile,"w") as outf:
            for data in intf:
                outf.write(data)
    return outputfile

#Problem 9
def q9(inputfile,outputfile):
    word_count={}
    with open(inputfile,"r") as ipf:
        for line in ipf:
            words=line.split()
            for word in words:
                if word in word_count:
                    word_count[word]+=1
                else:
                    word_count[word]=1
    sorted_words=sorted(word_count.items(),key=lambda item: item[1], reverse=True)
    top_words=sorted_words[:10]
    with open(outputfile,"w") as op:
        for word,count in top_words:
            op.write(word+"\n")
    return None
#Problem 10
def q10(inputfile1,inputfile2):
    output=inputfile1 + inputfile2
    with open(inputfile1,"r") as ip1:
        lines1=ip1.readlines()
    with open(inputfile2,"r") as ip2:
        lines2=ip2.readlines()
    maxlength=max(len(lines1),len(lines2))
    with open(output,"w") as op:
        for x in range(maxlength):
            if x < len(lines1):
                op.write(lines1[x])
            else:
                op.write("\n")
            if x < len(lines2):
                op.write(lines2[x])
            else:
                op.write("\n")
    return None
#Problem 11
def q11(filename,num):
    base, extension = filename.rsplit(".",1)
    with open(filename,"r") as fp:
        lines=fp.readlines()
    for x in range(num):
        output=f"{base}{x+1}.{extension}"
        with open(output,"w") as op:
            for i in range(x,len(lines),num):
                op.write(lines[i])
    return None
#Problem 12
def q12(filename):
    base, extension = filename.rsplit(".",1)
    vowels="aeiouyAEIOUY"
    consonants="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    with open(filename,"r") as fp:
        lines=fp.read()
    with open(f"{base}.vowels.{extension}","w") as bve:
        with open(f"{base}.consonants.{extension}","w") as bce:
            with open(f"{base}.others.{extension}","w") as boe:
                for char in lines:
                    if char in vowels:
                        bve.write(char)
                    elif char in consonants:
                        bce.write(char)
                    else:
                        boe.write(char)
    return None


    
