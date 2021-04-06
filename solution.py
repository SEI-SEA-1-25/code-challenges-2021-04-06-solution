def alias_gen(first_name, last_name):
    first_name, last_name = first_name.upper(), last_name.upper()
    if not first_name[0] in FIRST_NAME or not last_name[0] in SURNAME:
        return "Your name must start with a letter from A - Z."

    return f"{FIRST_NAME[first_name[0]]} {SURNAME[last_name[0]]}"

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

def well(ideas):
    count = 0
    for set in ideas:
        for idea in set:
            if type(idea) is str and idea.lower() == 'good':
                count += 1

    if count > 2:
        return "I smell a series!"
    elif count > 0:
        return "Publish!"

    return "Fail!"

