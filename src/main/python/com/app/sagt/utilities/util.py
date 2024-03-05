def convert(input: str):
    reserved_words = {
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
    }
    input_converted = []
    current_word = ""

    for char in input:
        if char in reserved_words:
            input_converted.append(char)
        elif char == " ":
            if current_word:
                if current_word in reserved_words:
                    input_converted.append(current_word)
                else:
                    input_converted.extend(list(current_word))
                current_word = ""
        else:
            current_word += char

    if current_word:
        if current_word in reserved_words:
            input_converted.append(current_word)
        else:
            input_converted.extend(list(current_word))

    for i, x in enumerate(input_converted):
        if x == reserved_words['<'] and input_converted[i+1] == "=" or x == reserved_words['>'] and input_converted[i+1] == "=":
            input_converted[i] += input_converted.pop(i + 1)

    return input_converted
