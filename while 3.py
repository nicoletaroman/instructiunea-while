n=0
suma=0
while ((n%2==0) or ((n%2!=0)and (n%3!=0))):
    n=eval(input("dati nr"))
    if n%2==0:
        suma+=n

print(suma)