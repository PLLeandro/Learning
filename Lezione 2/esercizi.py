#1-1

x=8.8
y=1.0/x

print(x,y,x*y)

print((x*y)-x)

#1-2

x=4.9
y=x%2.0

print(x)
print(y)

#1-3

z:int 
z=98
x=45
y=15

media=(x+y+z)/3

print(media)
 
 #1-4

n=int(input("inserire numerodi 4 cifre:"))
m=n // 1000
c=n // 100 - m * 10
d=n // 10 - m * 100 - c * 10
u=n - m * 1000 - c * 100 -d * 10
print(m)
print(c)
print(d)
print(u)

#1-5
grdi_fahr:int=45
gradi_cels= 5 * (gradi_fahr - 32) / 9
print(f"{gradi_farh} gradi