import string

fh=open("studentdata.txt","r")
for line in fh:
    values=line.split()
    line.remove(0)
    for i in scores:
        valuesSum=sum(values)
        valuesAve=valuesSum/len(valuesSum)
fh.close()
