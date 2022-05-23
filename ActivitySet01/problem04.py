# Conditional Execution

hrs = input("Enter hours? ")
h=float(hrs)
rate=input("Enter rate?")
r=float(rate)
if h>40 :
  lmn=40*r
  pqr=1.5*(h-40)*r
  xp=lmn+pqr
else:
  xp=h*r
print(xp)  