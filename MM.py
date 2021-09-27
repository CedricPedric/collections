import random


zakMM = {'oranje' : 0, 'blauw': 0 , 'groen': 0, 'bruin': 0}
DicMnMSmaken = {'smaken' : ['oranje', 'blauw', 'groen', 'bruin'] }
def MnMZak(aantal):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    for a in range(aantal):
        randomMM = random.randrange(0,4)
        MnM = DicMnMSmaken['smaken'][randomMM]
        print(MnM)
        if MnM == 'oranje':
            var1= var1 +1 
            zakMM['oranje'] = var1
        elif MnM == 'blauw':
            var2 = var2 +1
            zakMM['blauw'] = var2
        elif MnM == 'groen':
            var3 = var3 +1
            zakMM['groen'] = var3
        elif MnM == 'bruin':
            var4 = var4 + 1
            zakMM['bruin'] = var4
    return zakMM
aantal = int(input('Hoeveel M&MS in de zak: '))
print(MnMZak(aantal))


