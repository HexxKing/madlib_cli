print('''

Welcome to my Madlib game!

''')

# path = open('assets/game.txt')
with open('assets/game.txt') as path:
  string_template = path.readlines()
print(string_template) #Test


def read_template(path):
    content = open(path).read()
    return content.strip()
print('hit here') #Test


def parse_template(string_template):
    #remove these strings from the game.txt file
    string_template.strip('\n', 'Adjective', 'A First Name', 'Past Tense Verb', 'Plural Noun', 'Large Animal', 'Small Animal', 'A girls Name', 'Number 1-50', 'Number')
    return string_template
print(string_template) #Test



#input(adjective >)
#input(a first name >)
#input(past tense verb >)