temperatura=list(eval(input('Introduceti temperatura pentru fiecare ora: ')))
ora=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
print(sum(temperatura)/24)
print(max(temperatura),'maximul temperaturii',min(temperatura),'minimul temperaturii')
max=temperatura.index(max(temperatura))
print('ora',ora[max])
min=temperatura.index(min(temperatura))
print('ora',ora[min])


