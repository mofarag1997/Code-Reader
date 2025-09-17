def code_to_speech(code: str) -> str:
    replacements = {
        "{": " open curly brackets ",
        "}": " close curly brackets ",
        "(": " open parenthesis ",
        ")": " close parenthesis ",
        "[": " open square brackets ",
        "]": " close square brackets ",
        "<": " open angle bracket ",
        ">": " close angle bracket ",
        "<=": " less than or equal ",
        ">=": " greater than or equal ",
        "==": " double equals ",
        "===": " triple equals ",
        "=": " equals ",
        ";": " semicolon ",
        ":": " colon ",
        ",": " comma ",
        ".": " dot ",
        "!": " exclamation mark ",
        "+": " plus ",
        "-": " minus ",
        "*": " star ",
        "/": " slash ",
        "//": " double slash comment ",
        "/*": " open block comment ",
        "*/": " close block comment ",
        "->": " arrow ",
        "=>": " fat arrow "
    }

    for symbol in sorted(replacements.keys(), key=lambda x: -len(x)):
        code = code.replace(symbol, replacements[symbol])
    return code.strip()



sample_code = """
 


"""

print(code_to_speech(sample_code))
