#Restituisce (quanto aumentare il clock, quanto aumentare il registro)
def parse_instruction(instruction:str):
	command=instruction[0:4]
	if command=="noop":
		return [0]
	else:
		d_x=int(instruction[5:])
		return [0,d_x]

def main(input:str)->int:
	clock=0
	x_register=1
	pixels=[["" for _ in range(40)] for _ in range(6)]

	for multiple_instruction in input.splitlines():
		for d_x in parse_instruction(multiple_instruction):
			sprite=range(x_register-1,x_register+2)
			pixels[clock//40][clock%40]="#" if (clock%40) in sprite else "."
			clock+=1
			x_register+=d_x

	return pixels

if __name__=="__main__":
	with open("input.txt") as f:
		input=f.read()

	print(main(input))