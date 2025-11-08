e = 8
if (type(e) is int):
    print("true")
else:
    print("false")

e = 6.0
if (type(e) is not float):
    print("True")
else:
    print("False")

e = 30
f = 30
if (e is f):
    print("e and f are same")
else:
    print("e and f are NOT the same")

f = 40
if (e is not f):
    print("e and f are different")