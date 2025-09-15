operation_list = {}

class Operation:

    def __init__(self, strength: int, str_symbol: str, str_name: str):
        self.strength = strength
        self.str_symbol = str_symbol
        self.str_name = str_name

        operation_list[str_name] = self

    def calculate(self, number1: int, number2: int):
        return 0

    def __str__(self):
        return self.str_name

class Addition(Operation):
    def calculate(self, number1: int, number2: int):
        return number1 + number2

addition = Addition(100, "+", "addition")

class Subtraction(Operation):
    def calculate(self, number1: int, number2: int):
        return number1 - number2

subtraction = Subtraction(100, "-", "subtraction")

class Multiplication(Operation):
    def calculate(self, number1: int, number2: int):
        return number1 * number2

multiplication = Multiplication(200, "*", "multiplication")

class Division(Operation):
    def calculate(self, number1: int, number2: int):
        return number1 / number2

division = Division(200, "/", "division")

class Calc:

    def __init__(self):
        # base
        self.calculations = []
        self.current_pointer = -1

        # calculating
        self.united_number = []


    def add_symbol(self, symbol: str | int, position: int = None):
        if not position:
            position = self.current_pointer

        if isinstance(symbol, int):
            self.calculations.insert(position, symbol)

        elif symbol in operation_list.keys():
            self.calculations.insert(position, operation_list[symbol])

        else:
            print("Not Supported/Wrong Key")

    def _preparing_list(self) -> str | bool:
        prepare_calc_list = self.calculations.copy()

        for i in self.calculations:
            if isinstance(i, int):
                self.united_number.append(str(i))

            else:
                if not self.united_number:
                    return "Syntax Error"

                prepare_calc_list.append(int("".join(self.united_number)))
                self.united_number = []

                prepare_calc_list.append(i)

        self.calculations = prepare_calc_list
        return True

    def calculate(self) -> int | str:
        result = self._preparing_list()

        if isinstance(result, str):
            return result



