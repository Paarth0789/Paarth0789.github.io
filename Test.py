phy = int(input("Enter your marks in Physics: "))
chem = int(input("Enter your marks in Chemistry: "))
math = int(input("Enter your marks in Mathematics: "))

if phy and chem and math > 33:
    print(f"Congratulations! You are Passed.")

else:
    print(f"Better Luck Next Time!")