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
        #res=sum(res)/len(res)
        res/=times
        return round(res,5)
        

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
                "first", tentativo.joinpath("second.py").as_posix()
            ).load_module()
            attempt.second = modulo.main  # Importa la funzione main dell'esercizio 2

            eser.tentativi.append(attempt)
        year.esercizi.append(eser)
    anni.append(year)

for anno in anni:
    print(f"Anno {anno.anno}:")
    for esercizio in anno.esercizi:
        print(f"Esercizio {esercizio.numero}:")
        for tentativo in esercizio.tentativi:
            print(f"Soluzione di {tentativo.nome}:")
            print(f"First: {tentativo.benchfirst()}, Second: {tentativo.benchsecond()}")
            