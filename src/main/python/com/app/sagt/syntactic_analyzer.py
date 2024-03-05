from utilities import util
import re

predictive_table = {
    "REPETITIVA": {"mientras": ["mientras", "CONDICIONAL"]},
    "CONDICIONAL": {"(": ["(", "EXPRESIONES", "OPCIONAL", ")"]},
    "EXPRESIONES": {"a...z": ["VALOR", "OPERADOR", "VALOR"]},
    "VALOR": {"a...z": ["LETRA", "RESTO"]},
    "RESTO": {"a...z": ["LETRA", "RESTO"],
              "and": ["ε"],
              "or": ["ε"],
              ")": ["ε"],
              "<": ["ε"],
              ">": ["ε"],
              "==": ["ε"],
              "!=": ["ε"],
              ">=": ["ε"],
              "<=": ["ε"]},
    "LETRA": {"a...z": ["a...z"]},
    "OPERADOR": {">": [">"],
                 "<": ["<"],
                 "==": ["=="],
                 "!=": ["!="],
                 ">=": [">="],
                 "<=": ["<="]},
    "OPCIONAL": {"and": ["LOGICO", "EXPRESIONES"],
                 "or": ["LOGICO", "EXPRESIONES"],
                 ")": ["ε"]},
    "LOGICO": {"and": ["and"],
               "or": ["or"]},
}

terminals = {
    "mientras": "mientras",
    "(": "(",
    ")": ")",
    "or": "or",
    "and": "and",
    ">": ">",
    "<": "<",
    "==": "==",
    "!=": "!=",
    "<=": "<=",
    ">=": ">=",
    "a...z": "^[a-z]$",
}


def validate_terminal(production_pop):
    if production_pop in terminals:
        return True
    if bool(re.match(terminals["a...z"], production_pop)):
        return True
    else:
        return False


def analyze_syntax(input: str):
    input_converted = util.convert(input)
    print(input_converted)
    input_converted.append('$')
    pile = ['$', "REPETITIVA"]
    status = ""
    while len(pile) > 0:
        cdn = input_converted[0]
        production_pop = pile[-1]
        status += f"Pila: {pile} | Entrada: {cdn}\n"
        if pile[-1] == '$':
            status += "GRAMATICA CORRECTA"
            break
        if validate_terminal(production_pop):
            if production_pop == cdn:
                pile.pop()
                input_converted.pop(0)
            else:
                status += f"ERROR EN LA ENTRADA {cdn} SE ESPERABA UNA {production_pop} -> {predictive_table[production_pop]}"
                break
        else:
            try:
                if bool(re.match("^[a-z]$", cdn)):
                    if predictive_table[production_pop]["a...z"]:
                        if predictive_table[production_pop]["a...z"] == ["a...z"]:
                            pile.pop()
                            pile.extend(list(reversed(cdn)))
                        else:
                            pile.pop()
                            pile.extend(list(reversed(predictive_table[production_pop]["a...z"])))
                    else:
                        status += f"ERROR EN LA ENTRADA {cdn} SE ESPERABA UNA {production_pop} -> {predictive_table[production_pop]}"
                        break
                elif predictive_table[production_pop][cdn]:
                    if predictive_table[production_pop][cdn] == ["ε"]:
                        pile.pop()
                        pile.extend(list(reversed([])))
                    else:
                        pile.pop()
                        pile.extend(list(reversed(predictive_table[production_pop][cdn])))
                else:
                    status += f"ERROR EN LA ENTRADA {cdn} SE ESPERABA UNA {production_pop} -> {predictive_table[production_pop]}"
                    break
            except Exception:
                status += f"ERROR EN LA ENTRADA {cdn} SE ESPERABA UNA {production_pop} -> {predictive_table[production_pop]}"
                break
    return status
