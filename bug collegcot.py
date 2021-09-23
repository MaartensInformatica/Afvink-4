#geef de variabele bugs een waarde om ermee te kunnen werken
bugs = 0
for dag in range(1,6):
    bugs += int(input('Dag '+str(dag )+' aantal bugs: '))
print('totaal: ',bugs)

#Er zijn 5 dagen, dus een reeks van 1 tot 6 (1 t/m 5)
#In de reeks wordt voor elke dag de input gevraagd onder de naam bugs
#print het totaal. Aan het einde van de loop is bugs het aantal bugs van 5 dagen
