import math

opposite = int(input("Enter the opposite :"))
adjacent = int(input("Enter the adjacent :"))

hypothenuse = math.sqrt((opposite**2 + adjacent**2))
print("hypothenuse of triangle : " + str(hypothenuse))