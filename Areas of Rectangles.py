length1 = int(input("Enter the Rec 1 length : "))
width1 = int(input("Enter the Rec 1 width : "))
area1 = length1 * width1

length2 = int(input("Enter the Rec 2 length : "))
width2 = int(input("Enter the Rec 2 width : "))
area2 = length2 * width2

if area1 > area2:
    print("Area 1 is Greater than Area 2\n")
elif area1 == area2:
    print("Area 1 and 2 are Equal\n")
else:
    print("Area 2 is Greater than Area 1\n")


