a,b,c = [int(x) for x in input().split()]
x,y,z = [int(x) for x in input().split()]

#3 3 1
#2 2 1

#5 6 5
#6 5 6

#5 6 0
#6 5 0
#There are no miracles in life

#6 5 0
#5 6 0
#There are no miracles in life

#3 6 2
#6 5 1
#There are no miracles in life

#4 6 2
#6 5 1
#It is a kind of magic

if (a>=x and b>=y and c>=z):
    print("It is a kind of magic")
else:
    print("There are no miracles in life")