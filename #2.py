def num2(s):
    s1 = s[1:4]
    x = len(s)
    y = s[0:2]
    s1 = s[2:x]
    s1 = s1+y
    return s1

if num2("Hello") == "lloHe":
    print("Correct")
else:
    print("Incorrect")
if num2("java") == "vaja":
    print ("Correct")
else:
    print ("Incorect")
if num2("Hi") == "Hi":
    print ("Correct")
else:
    print ("Incorect")

