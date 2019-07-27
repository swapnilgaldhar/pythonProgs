list = [1,2,3,4,5,6,7,8,9]
#list = [input(range(1,12))]
list
sum = 0
for i in list:
    sum = sum + i
print(sum)
length = len(list)
avg = sum/length
print "Average of list is:",avg
