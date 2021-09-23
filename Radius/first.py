import math

radius = input("Enter radius: ");
radius_int = int(radius);
area = math.pi * radius_int * radius_int;
circumference = 2 * math.pi * radius_int;
print("area of a circle is: ", area,  "\ncircumference of a circle is:", circumference);
#print(circumference);

a_float = 2.5
a_int = 7
b_int = 6
print(a_int / b_int)
print(a_int // a_float)
print(a_int % b_int)
print(int(a_float))
print(float(a_int))
