"""AMOUNT                             INCOME TAX RATE
Up to ₹2,50,000                     0%
₹2,50,001 - ₹5,00,000               5% above ₹2,50,000
₹5,00,001 - ₹7,50,000               10% above ₹5,00,000 + ₹12,500
₹7,50,001 - ₹10,00,000              15% above ₹7,50,000 + ₹37,500
₹10,00,001 - ₹12,50,000             20% above ₹10,00,000 + ₹75,000
₹12,50,001 - ₹15,00,000             25% above ₹12,50,000 + ₹1,25,000
Above ₹15,00,001                    30% above ₹15,00,000 + ₹1,87,500

"""
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