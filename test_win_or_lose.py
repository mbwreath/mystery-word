from model import win_or_lose

def test_win():
    assert win_or_lose(1, "blue", "blue") == "win"

def test_lose():
    assert win_or_lose(0, "blue", "bl_e") == "lose"
