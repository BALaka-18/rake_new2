from rake_new2 import Rake


def test_first_rake_test():
    r = Rake()

    text = "How are your children ?"
    r.get_keywords_from_raw_text(text)

    result = r.get_keywords_with_scores()
    if result != {(1.0, 'children')}:
        raise AssertionError
