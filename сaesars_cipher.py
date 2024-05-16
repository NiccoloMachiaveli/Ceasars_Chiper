from string import ascii_lowercase


def shift_letter(letter: str, shift: int, cipher_simbol: str = ascii_lowercase) -> str:
    """Функция сдвигает символ letter на shift позиций

    :param letter: str Indicates which character should be shifted
    :param shift: int Indicates how many characters to shift
    :param cipher_simbol: str Indicates on the basis of which characters (languages) the shift should be made
    :return: str Returns the character after the shift
    """
    ind = cipher_simbol.index(letter)
    if shift >= 26 or shift <= -26:
        shift %= 26
    index = ind - (len(cipher_simbol)) + shift
    if index <= -26:
        index = (26 % index)
    return cipher_simbol[index]


def caesar_cipher(word: str, shift: int, cipher_simbol=ascii_lowercase) -> str:
    """Шифр цезаря
    :param word: str Indicates which word will be shifted
    :param shift: int Indicates how many characters to shift
    :param cipher_simbol: str Indicates on the basis of which characters (languages) the shift should be made
    :return: str returns the already shifted word
    """
    lst = []
    for i in word:
        if i in cipher_simbol:
            lst.append(shift_letter(i, shift))
        else:
            lst.append(i)
    return ''.join(lst)


cipher_word = input('Напишите слово для который будет шифроваться: ')
cipher_shift = int(input('Напишите размер сдвига: '))

print(caesar_cipher(cipher_word.lower(), cipher_shift))
