import sys

if len(sys.argv) == 4:
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
else:
    principal = float(input("Enter the prinicipal amount: "))
    rate = float(input("Enter the rate of Interest: "))
    time  = float(input("Enter the Time period (in years): "))
    
simple_interest = (principal * rate * time) / 100

print(f"Simple Interest = {simple_interest} ")
