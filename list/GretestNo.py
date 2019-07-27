
list = [1,2,3,4,15,6,7,8]
largest=list[0]
for i in range(list[1],len(list)):
    if list[i]>largest:
        largest=list[i]

print "Max num is :",largest
