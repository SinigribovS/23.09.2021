v=list(eval(input('Introduceti venitul corezpunzator fiecarei zile pe parcursul doar a unei saptamani: ')))
zi=['Luni', 'Marti', 'Miercuri','Joi', 'Vineri', 'Sambata', 'Duminica']
s=0
m=0
for i in v:
    s+=i
    m=s/len(v)
max=v.index(max(v))
min=v.index(min(v))
print("Venitul saptamanal:", s)
print("Media zilnica a venitului:", round(m,2))
print("Ziua cu cel mai mare venit:", zi[max])
print("Ziua cu cel mai mic venit:", zi[min])
