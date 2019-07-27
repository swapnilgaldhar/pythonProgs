list =  [input(range(1,11))]



a=list[0]
# b=list[len(list)-1]
v = list.pop()
list.append(a)
list.insert(1,v)

print list
