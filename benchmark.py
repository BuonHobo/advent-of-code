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
    def __init__(self, nome: str, first, second, input) -> None:
        self.nome: str = nome
        self.first: function | None = first
        self.timefirst: float | None = None
        self.second: function | None = second
        self.timesecond: float | None = None
        self.input: str = input

    @staticmethod
    def bench(fun, inp):
        if fun is None:
            return float("inf")

        def benched():
            return fun(inp)

        times = 3
        res = timeit.Timer(benched).timeit(times)
        return res / times

    def benchfirst(self, inp=None):
        if inp is None:  # Se non viene dato un input si usa quello del tentativo
            inp = self.input

        self.timefirst = self.bench(self.first, inp)
        return self.timefirst

    def benchsecond(self, inp=None):
        if inp is None:  # Se non viene dato un input si usa quello del tentativo
            inp = self.input

        self.timesecond = self.bench(self.second, inp)
        return self.timesecond


anni: list[Anno] = []

for anno in Path().iterdir():
    if not anno.name.isdigit():  # Evito i file inutili
        continue

    year = Anno(int(anno.name))
    for esercizio in anno.iterdir():  # 1, 2, 3...
        eser = Esercizio(int(esercizio.name))

        for tentativo in esercizio.iterdir():  # Alex, Rainer...

            with tentativo.joinpath(
                "input.txt"
            ).open() as inp:  # Legge il file di input associato
                input = inp.read()

            try:
                modulo = SourceFileLoader(
                    "first", tentativo.joinpath("first.py").as_posix()
                ).load_module()
                first = modulo.main  # Importa la funzione main dell'esercizio 1
            except:
                first = None

            try:
                modulo = SourceFileLoader(
                    "second", tentativo.joinpath("second.py").as_posix()
                ).load_module()
                second = modulo.main  # Importa la funzione main dell'esercizio 2
            except:
                second = None

            attempt = Tentativo(tentativo.name, first, second, input)

            eser.tentativi.append(attempt)
        year.esercizi.append(eser)
    anni.append(year)

print("\n[STARTING BENCHMARK]\n")
for anno in anni:
    print(f"Year {anno.anno}:\n")
    for esercizio in anno.esercizi:
        print(
            "{:>13}  [{:^10}] [{:^10}]".format(
                f"Day {esercizio.numero}:", "PART 1", "PART 2"
            )
        )

        inp = esercizio.tentativi[0].input
        best_first_name = "None"
        best_second_name = "None"
        best_first, best_second = float("inf"), float("inf")

        for tentativo in esercizio.tentativi:

            print("{:>13}  ".format(tentativo.nome + ":"), end="", flush=True)

            curr_first = tentativo.benchfirst(inp)

            print("[ {:^8} ] ".format("{:.6f}".format(curr_first)), end="", flush=True)

            curr_second = tentativo.benchsecond(inp)

            print("[ {:^8} ]".format("{:.6f}".format(curr_second)))

            if curr_first < best_first:
                best_first = curr_first
                best_first_name = tentativo.nome

            if curr_second < best_second:
                best_second = curr_second
                best_second_name = tentativo.nome

        print(
            "{:>13}  [{:^10}] [{:^10}]".format(
                "Winners:", best_first_name, best_second_name
            )
        )
        print()
