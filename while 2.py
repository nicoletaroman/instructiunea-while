nr=1
nrt=0
suma_p=0
suma_n=0
nr_p=0
nr_n=0
while nr<=12:
    nr=nr+1
    nrt=eval(input("dati nr"))
    if nrt>=0:
        suma_p+=nrt
        nr_p+=1
    if nrt<0:
        suma_n+=nrt
        nr_n+=1

print("temperatura pozitiva medie",suma_p/nr_p,"tempereatura negativa medie",suma_n/nr_n)