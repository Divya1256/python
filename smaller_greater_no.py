# find smaller and greater number

input1 = {24, -2100, 0, -19, 235, 18, 356, 36000, 21, 46}
print(" Smaller number = ", min(input1))
print(" Greater number = ", max(input1))

# another method for finding smaller and larger no.

input4 = [24, -2100, 0, -19, 235, 18, 356, 36000, 21, 46]


def greater_smaller(input4):
    input4.sort()
    print("\n\n", input4)
    print(" smaller number :", input4[0])
    print(" greater number :", input4[-1])


greater_smaller(input4)

# another method

input4 = [24, -2100, 0, -19, 235, 18, 356, 36000, 21, 46]
maxi = input4[0]
mini = input4[0]
for i in input4:
    if i > maxi:
        maxi = i
    elif i < mini:
        mini = i
print("\n\n Smaller number = ", mini)
print(" Greater number = ", maxi)