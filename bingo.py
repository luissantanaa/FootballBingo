from prettytable import PrettyTable

import random


def main():
	teamNames = ["FCPorto","SLBenfica"]
	teamA = ["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11"]
	teamB = ["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","B11"]
	PlayerActions = [" tropeça"," esgaça"," faz falta"," sofre falta"," falha um passe"," leva grande troço"," marca"," manda vir com o arbitro"," remata pó caralho"]
	MaregaActions = [" fumega"," cai", " ri-se"," deixa fugir para canto"," esgaça"," atropela alguém"]
	TeamActions = [" atraso para o guarda-redes", " substituição"," canto a favor"," canto contra"," livre a favor"," livre contra"]
	nrBingoPlayers = 5 
	PlayerPick = 0
	ActionPick = 0
	BingoCard = list()
	toAppend = ""
	nrSquares = 16

	for i in range(nrBingoPlayers):
		print("\n")
		print("\n")
		print("\n")
		BingoCard.clear()
		x = PrettyTable()
		x.field_names = ["Merdas com o Marega", " Valem", " Por", " 2"]
		
		while len(BingoCard) < nrSquares:
			decider = random.randint(1,10)
			
			if decider <= 5:
				if decider==0 or decider==1 or decider==3:
					ActionPick = random.randint(1,len(TeamActions))
					toAppend = teamNames[0] + TeamActions[ActionPick-1]
					if toAppend not in BingoCard:	
						BingoCard.append(toAppend)
						toAppend = ""	
				else:
					PlayerPick = random.randint(1,len(teamA))
					ActionPick = random.randint(1,len(PlayerActions))
					toAppend = teamA[PlayerPick-1] + PlayerActions[ActionPick-1]
					if PlayerPick == 11:
						ActionPick = random.randint(1,len(MaregaActions))
						toAppend = teamA[PlayerPick-1] + MaregaActions[ActionPick-1]
					if toAppend not in BingoCard:
						BingoCard.append(toAppend)
						toAppend = ""
			else:
				if decider==6 or decider==7 or decider==8:
					ActionPick = random.randint(1,len(TeamActions))
					toAppend = teamNames[1] + TeamActions[ActionPick-1]
					if toAppend not in BingoCard:	
						BingoCard.append(toAppend)
						toAppend = ""
				else:
					PlayerPick = random.randint(1,len(teamB))
					ActionPick = random.randint(1,len(PlayerActions))
					toAppend = teamA[PlayerPick-1] + PlayerActions[ActionPick-1]
					if toAppend not in BingoCard:
						BingoCard.append(toAppend)
						toAppend = ""
				
					
		print(BingoCard)
		j = 0
		for k in range(0,int(nrSquares/4)):
			k = k*4
			x.add_row([BingoCard[k], BingoCard[k+1], BingoCard[k+2], BingoCard[k+3]])
		print(x)
		data = x.get_string()

		with open('test' +str(i) +'.txt', 'w') as f:
			f.write("Soccer Dringo\n")
			f.write(data)
	BingoCard.clear()

main()