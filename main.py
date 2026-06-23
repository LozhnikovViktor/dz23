def count_vowels(text: str) -> int:
    """
    Подсчитывает количество гласных букв (a, e, i, o, u) в строке.
    Функция нечувствительна к регистру.

    :param text: Входная строка
    :return: Количество гласных букв
    """
    if not isinstance(text, str):
        raise TypeError("Ожидается строка")

    vowels = set("aeiou")
    return sum(1 for char in text.lower() if char in vowels)


import unittest


class TestCountVowels(unittest.TestCase):
    """Набор тестов для функции count_vowels."""

    def test_basic_vowels(self):
        """Проверка подсчёта гласных в обычной строке."""
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("world"), 1)
        self.assertEqual(count_vowels("python"), 1)

    def test_case_insensitive(self):
        """Проверка нечувствительности к регистру."""
        self.assertEqual(count_vowels("HELLO"), 2)
        self.assertEqual(count_vowels("HeLLo WoRLd"), 3)
        self.assertEqual(count_vowels("AeIoU"), 5)

    def test_all_vowels(self):
        """Строка, состоящая только из гласных."""
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_empty_string(self):
        """Обработка пустой строки."""
        self.assertEqual(count_vowels(""), 0)

    def test_no_vowels(self):
        """Строка без гласных букв."""
        self.assertEqual(count_vowels("rhythm"), 0)
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels("12345"), 0)

    def test_mixed_content(self):
        """Строка с гласными, согласными, цифрами и спецсимволами."""
        self.assertEqual(count_vowels("Hello, World! 123"), 3)
        self.assertEqual(count_vowels("Python 3.12 is awesome"), 6)  # было 7

    def test_spaces_and_symbols(self):
        """Строка из пробелов и спецсимволов."""
        self.assertEqual(count_vowels("   "), 0)
        self.assertEqual(count_vowels("!@#$%^&*()"), 0)

    def test_single_vowel(self):
        """Строка из одного символа-гласной."""
        self.assertEqual(count_vowels("a"), 1)
        self.assertEqual(count_vowels("U"), 1)

    def test_single_consonant(self):
        """Строка из одного символа-согласной."""
        self.assertEqual(count_vowels("b"), 0)
        self.assertEqual(count_vowels("Z"), 0)

    def test_invalid_input(self):
        """Проверка обработки некорректного типа входных данных."""
        with self.assertRaises(TypeError):
            count_vowels(123)
        with self.assertRaises(TypeError):
            count_vowels(None)
        with self.assertRaises(TypeError):
            count_vowels(["a", "e", "i"])


if __name__ == "__main__":
    unittest.main()