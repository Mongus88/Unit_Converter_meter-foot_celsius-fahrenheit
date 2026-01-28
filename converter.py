foot = 0.3048
meter = 3.28084

"""
T(F) = T(C) * 1.8 + 32
T(C) = (T(F) - 32) / 1.8
"""

measure = ["foot", "meter", "fahrenheit", "celsius"]

while True:
    unit = input("Enter unit: ")
    if unit in measure:
        value = input("Enter value: ")
        if unit == "foot":
            print(float(value) * foot, "m")
            break
        elif unit == "meter":
            (print(float(value) * meter, "ft"))
            break
        elif unit == "fahrenheit":
            print((float(value) - 32) / 1.8, "C")
            break
        elif unit == "celsius":
            print(float(value) * 1.8 + 32, "F")
            break
    else:
        print("Invalid unit")
        continue
