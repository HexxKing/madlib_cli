import builtins
import pytest
from madlib_cli.madlib import read_template, parse_template, merge, main

open_sample_text = open("assets/game.txt").read()
path = "assets/game.txt"

def test_read_template_returns_stripped_string():
    actual = read_template(path)
    expected = open_sample_text.strip()
    assert actual == expected



def test_parse_template():
    actual_stripped, actual_parts = parse_template("A {Adjective} and {Adjective} {Noun}.")
    expected_stripped = "A {} and {} {}."
    expected_parts = ["Adjective", "Adjective", "Noun"]
    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


def test_merge_template():
    actual = merge("A {} and {} {}.", ["dark", "stormy", "night"])
    expected = "A dark and stormy night."
    assert actual == expected 