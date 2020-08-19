#Python Program for compound interest
#P(1 + R/100) t
#P-principle_amount , T-time , R-rate
P = float(input("Enter your principle amount : "))
T = float(input("Enter the time-span of your investment : "))
R = float(input("Enter the rate of the investment : "))

interest = P*(1 + R/100)*T

print("Your compound interest over",int(T),"time at the rate of",R,"with the principle amount",P,"is : ",interest)	