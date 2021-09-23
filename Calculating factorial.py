#Geef een waarde aan de variabele
Factoriaal = 1
Input = input('Welke positief getal: ')
for getal in range(1, int(Input)+1):
    Factoriaal = Factoriaal * getal
print(Factoriaal)

    
#Geef een variabele aan de input en gebruik die in de loop
#In de loop wordt 1 vermenigvuldigd met het volgende getal, tot het einde van de range en dat is wat de gebruiker ingevoerd heeft
