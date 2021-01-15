from prettytable import PrettyTable

import random


def main():
	teamNames = ["A","B"]
	teamA = ["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11"]
	teamB = ["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","B11"]
	PlayerActions = [" tropeça"," esgaça"," faz falta"," sofre falta"," falha um passe"," leva grande troço"," marca"," manda vir com o arbitro"," remata pó caralho"]
	TeamActions = []
	nrBingoPlayers = 3 
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
		x.field_names = ["C1", "C2", "C3", "C4"]
		
		while len(BingoCard) < nrSquares:
			decider = random.randint(1,10)
			
			if decider <= 5:
				PlayerPick = random.randint(1,len(teamA))
				ActionPick = random.randint(1,len(PlayerActions))
				
				toAppend = teamA[PlayerPick-1] + PlayerActions[ActionPick-1]
				if toAppend not in BingoCard:
					
					BingoCard.append(teamA[PlayerPick-1] + PlayerActions[ActionPick-1])
					toAppend = ""
				
					
			else:
				PlayerPick = random.randint(1,len(teamB))
				ActionPick = random.randint(1,len(PlayerActions))
				
				if toAppend not in BingoCard:
					
					BingoCard.append(teamB[PlayerPick-1] + PlayerActions[ActionPick-1])
					toAppend = ""
				
					
		print(BingoCard)
		j = 0
		for k in range(0,int(nrSquares/4)):
			k = k*4
			x.add_row([BingoCard[k], BingoCard[k+1], BingoCard[k+2], BingoCard[k+3]])
		print(x)
		data = x.get_string()

		with open('test' +str(i) +'.txt', 'w') as f:
			f.write(data)
	BingoCard.clear()

main()