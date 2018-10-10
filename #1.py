def num1(s):
    s1 = s[1:4]
    x = len(s)
    x = x-1
    s1 = s[1:x]
    return s1

if num1("hello") == "ell":
    print("Correct")
else:
    print("Incorrect")
if num1("java") == "av":
    print ("Correct")
else:
    print ("Incorect")
if num1("coding") == "odin":
    print ("Correct")
else:
    print ("Incorect")

