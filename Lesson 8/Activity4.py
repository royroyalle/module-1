q = int(input("Enter Cyclist 1's value"))
w = int(input("Enter Cyclist 2's value"))
e = int(input("Enter Cyclist 3's value"))
avg= (q+w+e) / 3
print("Average of", q, ",", w, "and", e, "is..", avg)
if avg > q and avg > w and avg > e:
    print("%d is higher than %d, %d, %d, %d" %(avg, q,w,e))
elif avg > q and avg > w:
    print("%d is higher than %d", (avg, q, w))
elif avg > q and avg > e:
    print("%d is higher than %d", (avg, q, e))
elif avg > w and avg > e:
    print("%d is higher than %d", (avg, w, e))
elif avg > q:
    print("%d is higher than %d", (avg, q))
elif avg > w:
    print("%d is higher than %d", (avg, w))
elif avg > e:
    print("%d is higher than %d", (avg, e))
else:
    print("The following inputs are invalid")