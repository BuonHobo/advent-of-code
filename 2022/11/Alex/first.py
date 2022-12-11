import itertools
import typing


class monkey:
	def __init__(
		self,
		id: int,
		items: list[int],
		inspection: typing.Callable[[int], int],
		test: int,
		target: tuple[int, int],
	) -> None:
		self.id = id
		self.items = items
		self.inspection = inspection
		self.test = test
		self.target = target
		self.count=0

	def add_item(self, item: int):
		self.items.append(item)

	def inspect_item(self, worry:int) -> int:
		self.count+=1
		worry = self.inspection(worry)
		worry = worry // 3
		return worry

	def inspect_items(self):
		self.items = list(map(self.inspect_item, self.items))

	def throw_item(self) -> tuple[int, int]:
		'''returns (worry,target)'''
		item = self.items.pop()
		if item % self.test == 0:
			return (item, self.target[0])
		else:
			return (item, self.target[1])


def parse_monkey(string: str) -> monkey:
	id, items, inspect, test, iftrue, iffalse = string.split("\n")

	id = id[:-1].split()[-1]
	id = int(id)

	items = list(map(int, items.split(": ")[-1].split(", ")))

	inspect, num = inspect.split()[4:]
	if inspect == "*":
		sign = int.__mul__
	else:
		sign = int.__add__

	if num.isdecimal():
		op:typing.Callable[[int],int] = lambda old: sign(old, int(num))
	else:
		op:typing.Callable[[int],int] = lambda old: sign(old, old)

	test=test.split()[-1]
	test=int(test)
	
	iftrue=iftrue.split()[-1]
	iftrue=int(iftrue)

	iffalse=iffalse.split()[-1]
	iffalse=int(iffalse)

	return monkey(id,items,op,test,(iftrue,iffalse))


def main(input: str) -> int:
	monkeys= list(map( parse_monkey,input.split("\n\n")))
	rounds=20

	for round in range(rounds):
		for id in range(len(monkeys)):
			monkeys[id].inspect_items()
			for _ in range(len(monkeys[id].items)):
				worry,target=monkeys[id].throw_item()
				monkeys[target].add_item(worry)

	res=sorted(map(lambda monke: monke.count,monkeys),reverse=True)
	return res[0]*res[1]

if __name__ == "__main__":
	with open("input.txt") as f:
		input = f.read()

	print(main(input))
