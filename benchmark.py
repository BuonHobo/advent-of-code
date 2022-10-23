from pathlib import Path
from importlib.machinery import SourceFileLoader
import timeit


class Anno:
    def __init__(self, anno: int) -> None:
        self.anno: int = anno
        self.esercizi: list[Esercizio] = []


class Esercizio:
    def __init__(self, numero: int) -> None:
        self.numero: int = numero
        self.tentativi: list[Tentativo] = []


class Tentativo:
    def __init__(self, nome: int) -> None:
        self.nome: int = nome
        self.first: function = None
        self.timefirst:float=None
        self.second: function = None
        self.timesecond:float=None
        self.input: str = None

    @staticmethod
    def bench(fun,inp):
        def benched():
            return fun(inp)

        times=20
        res= timeit.Timer(benched).timeit(times)
        return res/times
        

    def benchfirst(self,inp=None):
        if inp is None: #Se non viene dato un input si usa quello del tentativo
            inp=self.input
        
        self.timefirst=self.bench(self.first,inp)
        return self.timefirst

    def benchsecond(self,inp=None):
        if inp is None: #Se non viene dato un input si usa quello del tentativo
            inp=self.input
        
        self.timesecond=self.bench(self.second,inp)
        return self.timesecond




anni: list[Anno] = []

for anno in Path().iterdir():
    if not anno.name.isdigit():  # Evito i file inutili
        continue

    year = Anno(int(anno.name))
    for esercizio in anno.iterdir():  # 1, 2, 3...
        eser = Esercizio(int(esercizio.name))

        for tentativo in esercizio.iterdir():  # Alex, Rainer...
            attempt = Tentativo(tentativo.name)

            with tentativo.joinpath(
                "input.txt"
            ).open() as inp:  # Legge il file di input associato
                attempt.input = inp.read()

            modulo = SourceFileLoader(
                "first", tentativo.joinpath("first.py").as_posix()
            ).load_module()
            attempt.first = modulo.main  # Importa la funzione main dell'esercizio 1

            modulo = SourceFileLoader(
                "second", tentativo.joinpath("second.py").as_posix()
            ).load_module()
            attempt.second = modulo.main  # Importa la funzione main dell'esercizio 2

            eser.tentativi.append(attempt)
        year.esercizi.append(eser)
    anni.append(year)

print("\n[STARTING BENCHMARK]\n")
for anno in anni:
    print(f"Anno {anno.anno}:\n")
    for esercizio in anno.esercizi:
        print("{:<12}  [{:^10}] [{:^10}]".format(f"Esercizio {esercizio.numero}:","PART 1","PART 2"))

        inp=esercizio.tentativi[0].input
        best_first,best_second= float("inf"),float("inf")

        for tentativo in esercizio.tentativi:

            curr_first= tentativo.benchfirst(inp)
            curr_second=tentativo.benchsecond(inp)

            if curr_first<best_first:
                best_first=curr_first
                best_first_name=tentativo.nome

            if curr_second<best_second:
                best_second=curr_second
                best_second_name=tentativo.nome

            print("{:>12}  [ {:.6f} ] [ {:.6f} ]".format(tentativo.nome+":",curr_first,curr_second))

        print("{:>12}  [{:^10}] [{:^10}]".format("Winners:",best_first_name,best_second_name))
        print()