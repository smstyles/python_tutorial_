
income=int(input("Enter your income:"))
if income<250000:
    print("NO income_tax")
elif income<500000:
    print("Your income tax is:",income*0.05)
elif income<750000:
    print("Your income tax is:",income*0.1)
elif income<1000000:
    print("Your income tax is:",income*0.15)
elif income<1250000:
    print("Your income tax is:",income*0.2)
elif income<1500000:
    print("Your income tax is:",income*0.25)
else:
    print("Your income tax is:",income*0.3)
