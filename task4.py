def number_to_words(num):
    units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    thousands = ['', 'тысяча', 'тысячи', 'тысяч']

    if num == 0:
        return 'ноль'

    result = ''
    if num // 1000000 > 0:
        return 'Число больше миллиона'

    if num // 1000 > 0:
        thousands_part = num // 1000
        if thousands_part >= 100:
            result += hundreds[thousands_part // 100] + ' '
            thousands_part %= 100
        if 10 <= thousands_part <= 19:
            result += teens[thousands_part - 10] + ' '
        else:
            result += tens[thousands_part // 10] + ' '
            result += units[thousands_part % 10] + ' '
        if num % 1000 == 0:
            result += thousands[0] + ' '
        elif num % 1000 in range(10, 20):
            result += thousands[3] + ' '
        elif num % 1000 % 100 in range(10, 20):
            result += thousands[3] + ' '
        elif num % 1000 % 10 == 1:
            result += thousands[1] + ' '
        elif num % 1000 % 10 in range(2, 5):
            result += thousands[2] + ' '
        else:
            result += thousands[3] + ' '
        num %= 1000

    if num // 100 > 0:
        result += hundreds[num // 100] + ' '
        num %= 100
    if 10 <= num <= 19:
        result += teens[num - 10] + ' '
    else:
        result += tens[num // 10] + ' '
        result += units[num % 10] + ' '

    return result.strip()

# Пример использования
print(number_to_words(217045))  # Двести семнадцать тысяч сорок пять
