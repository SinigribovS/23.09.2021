n=int(input('Dati numarul de elemente din vector='))
a=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
# if n<10:
for i in range(0,n):
    x=int(input('Dati elementul='))
    a.extend([x])
print(a)

print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii; ', a[0],a[1],a[2],a[3],a[4])
v=a
v.reverse()
print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator;', v)
print('c)  sortează componentele tabloului în ordine descrescătoare;')
b=sorted(a)
b.sort(reverse=True)
print(b)
print('d)  afişează pe ecran doar componentele pare;')
c=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        c.extend([y])
print(c)
print('e)  afişează pe ecran media aritmetică a componentelor pare;')
print(sum(c)/len(c))
print('f)  afişează pe ecran doar componentele impare;')
d=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        y=a[i]
        d.extend([y])
print(d)
print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
x=int(input('valoarea x= '))
y=int(input('valoarea y= '))
g=[]
for i in range(0,len(a)):
    if ((a[i]>x) and (a[i]%y!=0)):
        u=a[i]
        g.extend([u])
print(g)
print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')
x1=int(input('valoarea x= '))
y1=int(input('valoarea y= '))
h=[]
for i in range(0,len(a)):
    if ((a[i]>x) and (a[i]<y)):
        u1=a[i]
        h.extend([u1])
print(h)
print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative;')
for i in a:
    if i < 0 and i%2==1:
        print(a.index(i))
print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
for i in a:
    if (i < 100 and i>9) or (i > -100 and i<-9):
        print(a.index(i))
print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
k=a
comp=a[0]
ind = a.index(min(a))
k[:1]=[min(k)]

print(k)
print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;')
k[ind]=comp
print(k)
print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
even = []
for i in a:
    if i % 2 == 0:
        even.append(i)
print(even)
print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
en = []
for i in a:
    if i % 3 == 0:
        en.append(i)
print(en)
print('o)  creează un tablou nou, format doar din acele componente ale tabloului in-trodus de la tastatură care au cel mult patru divizori.')
h = []
for i in a:
    counter = 0
    for b in range(1,i):
        if i%b==0:
            counter+=1
    if counter < 5:
        h.append(i)
print(h)



