weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
elif unit.upper() == "L":
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))
else:
    print("Please enter unit of (K)g or (L)bs")