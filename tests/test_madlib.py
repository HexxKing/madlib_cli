from madlib_cli.madlib import read_template

open_sample_text = open("assets/game.txt").read()
path = "assets/game.txt"

def test_read_template():
    actual = read_template(path)
    expected = open_sample_text.strip()
    assert actual == expected

def test_parse_template():
    

#def test_merge_template():