#Variabele van de sikkel en normale sequentie als string om in te kunnen lezen

sikkel_seq = 'GAGCCATCTATTGCTTACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAGACTCTTGGGTTTCT'
normaal_seq ='GAGCCATCTATTGCTTACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAGACTCTTGGGTTTCT'

#open het bestand en maak twee lijsten
bestand = open('C:\\Users\\Maarten Degenhart\\Documents\\GitHub\\2122-owe1a-afvinkopdracht4-MaartensInformatica\\enzymen.txt')
kniplijst = []
nicelist = []
#In de eerste lijst splitten we tussen de naam en het profiel
for line in bestand:
    knipprofiel = line.split()
    kniplijst.append(knipprofiel[1])
#in de tweede lijst halen we het dakje weg zodat we kunnen kijken of de code van het enzym in de sequentie voorkomt
for char in kniplijst:
    nicelist.append(char.replace('^',''))
    
        
#in de tweede lijst tellen we ieder enzym om te kijken of die in de sikkelseq zit
#Alleen als hij er in zit wordt hij geprint. Hetzelfde wordt gedaan voor de normale sequentie
print('---sikkel sequentie---')
for enzym in nicelist:
    sikkel_seq.count(enzym)
    if sikkel_seq.count(enzym) == 1:
        print(enzym)
        print(sikkel_seq.count(enzym))        
print('---normale sequentie---')
for enzym in nicelist:
    normaal_seq.count(enzym)
    if normaal_seq.count(enzym) == 1:
        print(enzym)
        print(normaal_seq.count(enzym))
   


