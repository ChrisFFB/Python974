B=1800
T=1800 # dans un an, l'an prochain
L=[1800]
for i in range(1,10): # dans 10 ans donc on effectue 9 fois la boucle (il faut rajouter 9 ans)
	B=0.95*B
	T=T+B
	L.append(B) # pour expliquer
print(T)
# dernière ligne pas demandée
print('Dans',i+1 ,'ans.')
print('ci dessous la liste des budgets annuels :' )
print(L)

