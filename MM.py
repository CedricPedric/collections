import random
def MnMZAK(hoeveel):
    aantalMM = ['oranje', 'blauw', 'groen', 'bruin']
    Zak = []
    for b in range(hoeveel):
        randomMM = random.randrange(0,4)
        Mm = aantalMM[randomMM] 
        Zak.append(Mm)
    return Zak

hoeveel = int(input('Hoeveel M&M wil je in de zak? :'))   
print(MnMZAK(hoeveel))


