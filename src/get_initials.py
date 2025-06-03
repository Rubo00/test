def format_one_name(name: tuple[str,str,str]) -> str:
    lastname, fristname, surname = name
    return f"{lastname} {fristname[0]}. {surname[0]}."


def format_names (names: list[tuple[str,str,str]]) -> list[str]:
    formated_names = []
    for name in names:
        formated_names.append(format_one_name(name))
    return formated_names