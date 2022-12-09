def too_far(head,tail)->bool:

	if abs(head[0]-tail[0])>1 or abs(head[1]-tail[1])>1:
		return True

	return False

def parse_move(move:str):
	first,second=move.split()

	match first:
		case "R":
			first=(1,0)
		case "U":
			first=(0,1)
		case "L":
			first=(-1,0)
		case D:
			first=(0,-1)

	return (first for _ in range(int(second)))
	
def aggiorna_posizione(pos:tuple[int,int], mossa:tuple[int,int]):
	return (pos[0]+mossa[0],pos[1]+mossa[1])

def main(input:str)->int:
	moves=(parse_move(move) for move in input.splitlines())
	ultimaposizione:tuple[int,int]=(0,0)
	posizionecorrente:tuple[int,int]=(0,0)
	posizionecoda:tuple[int,int]=(0,0)
	posizionicoda:set[tuple[int,int]]={(0,0)}

	for multiplemove in moves:
		for move in multiplemove:
			ultimaposizione=posizionecorrente
			posizionecorrente=aggiorna_posizione(posizionecorrente,move)
			if too_far(posizionecorrente,posizionecoda):
				posizionecoda=ultimaposizione
				posizionicoda.add(posizionecoda)

	return len(posizionicoda)

if __name__=="__main__":
	with open("input.txt") as f:
		input=f.read()
	
	print(main(input))