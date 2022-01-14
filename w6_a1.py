def computepay(h, r):
    if h <= 40 :
        pay = h * r
    else :

        pay = (40 * r) + ((h-40) * 1.5 * r)


    return pay

hrs = float(input("Enter Hours:"))
rate=float(input("Enter Rate per hour:"))
p = computepay(hrs, rate)
print("Pay", p)
