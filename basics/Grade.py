print "Wel - come to Grade    'System'"

sub1 = input("Enter mark of an subject1 : ")
sub2 = input("Enter mark of an subject2 : ")
sub3 = input("Enter mark of an subject3 : ")
sub4 = input("Enter mark of an subject4 : ")
sub5 = input("Enter mark of an subject5 : ")

sum = sub1+sub2+sub3+sub4+sub5

if sum >= 450:
    print"A"
elif sum >=400:
    print "B"
elif sum >=350:
    print"C"
elif sum >  300:
    print"D"
else:
    print"Fail"
