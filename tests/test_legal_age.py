import unittest

from app import is_legal_age


class LegalAgeTests(unittest.TestCase):
    def test_person_over_20_is_legal_age(self):
        self.assertTrue(is_legal_age(21, "single"))

    def test_person_under_20_and_single_is_not_legal_age(self):
        self.assertFalse(is_legal_age(19, "single"))

    def test_person_under_20_but_married_is_legal_age(self):
        self.assertTrue(is_legal_age(19, "married"))

    def test_person_under_20_but_divorced_is_legal_age(self):
        self.assertTrue(is_legal_age(19, "divorced"))


if __name__ == "__main__":
    unittest.main()
