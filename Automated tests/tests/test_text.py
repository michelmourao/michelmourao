from app.text import Text

def test_text():
    assert Text.pprint('testing 1,2,3...') == 'testing 1,2,3...'
