#Python Program for compound interest
#P(1 + R/100) t
#P-principle_amount , T-time , R-rate
P = float(input("Principle (amount): "))
T = float(input("Time: "))
R = float(input("Rate: "))

interest = P*(1 + R/100)**T

print("Compound interest = ",interest)	