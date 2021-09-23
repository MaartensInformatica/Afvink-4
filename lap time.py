#Maak variabelen aan, een input voor aantal rondjes en een lijst voor de looptijden
Laagste_tijd = 99999999999
Hoogste_tijd = 0
Gemiddelde_tijd = 0
Aantal_rondes = int(input('hoeveel rondes: '))
Looptijden = []
    
#In de loop vullen we lijst in met looptijden
for ronde in range(Aantal_rondes):
    Looptijden.append(float(input('Ronde '+str(ronde+1 )+' looptijd: ')))

#In deze loop kijken we welke tijd het laagste, hoogste en wat het gemiddelde is    
for tijd in Looptijden:
    if tijd < Laagste_tijd:
        Laagste_tijd = tijd
    if tijd > Hoogste_tijd:
        Hoogste_tijd = tijd
    Gemiddelde_tijd += (tijd) / Aantal_rondes
print('Snelste ronde',':',Laagste_tijd, 'minuut')
print('Traagste ronde',':',Hoogste_tijd, 'minuut')
print('Gemiddelde tijd',':',round(Gemiddelde_tijd, 2),'minuut')


