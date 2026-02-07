def foot_to_meter(x):
    return x * 0.3048
def meter_to_foot(x):
    return x * 3.28084
def fahrenheit_to_celsius(x):
    return (x - 32) / 1.8
def celsius_to_fharenheit(x):
    return x * 1.8 + 32

unit_in = input("Enter unit: ")
x = float(input("Enter value: "))

measure = {
    "foot": [foot_to_meter, "m"],
    "meter": [meter_to_foot, "ft"],
    "fahrenheit": [fahrenheit_to_celsius, "°C"],
    "celsius": [celsius_to_fharenheit, "°F"]
}

print(f"{measure[unit_in][0](x):.2f} {measure[unit_in][1]}")
