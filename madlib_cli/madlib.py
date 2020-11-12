print('''

Welcome to my Madlib game!

''')

def read_template(path):
    with open(path) as file:
      content = file.read()
        stipped_content = content.strip()
    return stripped_content

def parse_template(string_template):
    capturing = False
    dissected_string = ""
    parts = []
    current_speech_part = ""

    # "A {Adjective} and {Adjective} {Noun}."
    #  ^
    #capturing = True
    #dissected_string = "A {} and {} {}"
    #current_speech_part = "Adjective" - should build up to Adjective, the add it to the parts list and var gets set back to 0 before the next speech part
    #push to parts - ["Adjective", "Adjective", "Noun"]

    for char in string_template:
        if not capturing:
            dissected_string += char

            if char == "{"
                capturing = True

        else: 
            if char == "}":
                capturing = False
                parts.append(current_speech_part)
                dissected_string += char
                current_speech_part = ""
            else:
                current_speech_part += char
    return (dissected_string,parts) #could also be a list but tuple preferred


    # dissected_string = "A {} and {} {}."
    # parts = ["Adjective," "Adjective", "Noun"]
    # return (dissected_string, parts)

def merge(bare_template, responses):
    return bare_template.format(*responses) # the * breaks up the list into individual args
    
    #alternative
    # merged = bare_template
    # for response in responses:
    #     merged = merged.replace("{}", response, 1)
    # return merged








#input(adjective >)
#input(a first name >)
#input(past tense verb >)