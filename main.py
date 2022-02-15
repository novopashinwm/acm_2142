a,b,c = [int(x) for x in input().split()]
x,y,z = [int(x) for x in input().split()]

ax = min(a,x)
a -= ax
x -= ax

by = min (b,y)
b -= by
y -= by

cx = min (c,x)
c -= cx
x -= cx

cy = min (c,y)
c -= cy
y -= cy
z -= a + b + c

if (x<=0 and y<= 0 and z<=0):
    print("It is a kind of magic")
else:
    print("There are no miracles in life")