year = int(input("Enter a year : "))

def isLeap(year):
    if year%4 == 0:

        if year%100 == 0:

            if year%400 == 0:
                return 'TRUE'

            return 'FALSE'
        
        return 'TRUE'

    else:
        return 'FALSE'

ans = isLeap(year)
print(ans)