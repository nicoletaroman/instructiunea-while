nr=0
suma=0
produsul=1
media_a=0

n=eval(input("dati nr"))
while nr<n:
    nr=nr+1
    suma=suma+nr
    produsul=produsul*nr
    media_a=suma/nr
   
print("suma este",suma,"produsul este",produsul,"media aritmetica este",media_a)