word = input('Введите слово: ').lower()

def palindrome(word):
    if word == word[::-1]:
        print('Является палиндромом')
    else:
        print('Не является палиндромом')
