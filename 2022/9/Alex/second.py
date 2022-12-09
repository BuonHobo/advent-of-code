def too_far(head,tail)->bool:

	if abs(head[0]-tail[0])>1 or abs(head[1]-tail[1])>1:
		return True

	return False

def segui_testa(coda:tuple[int,int],testa:tuple[int,int])->tuple[int,int]:
	x_diff=testa[0]-coda[0]
	y_diff=testa[1]-coda[1]

	if x_diff>1: x_diff=1
	elif x_diff<-1:x_diff=-1

	if y_diff>1:y_diff=1
	elif y_diff<-1:y_diff=-1

	return (coda[0]+x_diff,coda[1]+y_diff)

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
	knots=10
	moves=(parse_move(move) for move in input.splitlines())
	posizionicorrenti:list[tuple[int,int]]=[(0,0) for _ in range(knots)]
	posizionicoda:set[tuple[int,int]]={(0,0)}

	for multiplemove in moves:
		for move in multiplemove:
			posizionicorrenti[0]=aggiorna_posizione(posizionicorrenti[0],move)

			for nodo in range(knots-1):
				if too_far(posizionicorrenti[nodo],posizionicorrenti[nodo+1]):
					posizionicorrenti[nodo+1]=segui_testa(posizionicorrenti[nodo+1],posizionicorrenti[nodo])

			posizionicoda.add(posizionicorrenti[-1])

	return len(posizionicoda)

if __name__=="__main__":
	with open("input.txt") as f:
		input=f.read()
	
	print(main(input))