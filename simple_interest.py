#this program is to find the simple interest
#Simple Interest = (P x T x R)/100
#P-principle_amount , T-time , R-rate

P = float(input("Enter your principle amount : "))
T = float(input("Enter the time-span of your investment : "))
R = float(input("Enter the rate of the investment : "))

interest = (P * T * R)/100

print("Your interest over",int(T),"time at the rate of",R,"with the principle amount",P,"is : ",interest)	