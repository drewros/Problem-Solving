def num3(s,a):
    p1 = s[0:2]
    p3 = s[2:4]
    s1 = p1+a+p3
    return s1

if num3("<<>>","Yay") == "<<Yay>>":
    print("Correct")
else:
    print("Incorrect")
if num3("<<>>", "WooHoo") == "<<WooHoo>>":
    print ("Correct")
else:
    print ("Incorect")
if num3("[[]]", "word") == "[[word]]":
    print ("Correct")
else:
    print ("Incorect")
