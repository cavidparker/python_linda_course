a, b = 10, 1
if a < b:
    print("a ({}) is less than b ({})".format(a,b))
else:
    print(" a ({}) is greater than b ({})".format(a,b))

print("foo" if a < b else "bar")    