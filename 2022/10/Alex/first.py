#Restituisce (quanto aumentare il clock, quanto aumentare il registro)
def parse_instruction(instruction:str):
	command=instruction[0:4]
	if command=="noop":
		return (1,0)
	else:
		return (2, int(instruction[5:]))

def main(input:str)->int:
	instructions=(parse_instruction(inst) for inst in input.splitlines())
	clock=0
	x_register=1
	latest_value=1
	cycles=[20,60,100,140,180,220]
	cycles.reverse()
	target_cycle=cycles.pop()
	somma=0

	for d_clock, d_x in instructions:
		latest_value=x_register
		clock+=d_clock
		x_register+=d_x
		if clock>=target_cycle:
			somma+=latest_value*target_cycle
			try:
				target_cycle=cycles.pop()
			except:
				break

	return somma

if __name__=="__main__":
	with open("input.txt") as f:
		input=f.read()
	
	print(main(input))