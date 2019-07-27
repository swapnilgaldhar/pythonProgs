
num = input("ENter no : ")
result = 0

while num > 0:
    rem = num % 10
    result = result + rem
    num = int(num/10)

print "Addition is : ",result

