def number_to_words(num):
    units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    units_2 = ['', 'одна', 'две', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
             'семнадцать', 'восемнадцать', 'девятнадцать']
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
            if num < 10000:
                result += units_2[thousands_part % 10] + ' '
            else:
                result += units[thousands_part % 10] + ' '

        if thousands_part % 100 in range(10, 20):
            result += thousands[3] + ' '
        else:
            if thousands_part % 10 == 0:
                result += thousands[3] + ' '
            elif thousands_part % 10 == 1:
                result += thousands[1] + ' '
            elif thousands_part % 10 in range(2, 5):
                result += thousands[2] + ' '
            elif thousands_part % 10 in range(5, 10):
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
print(number_to_words(217045))  # двести семнадцать тысяч сорок пять
print(number_to_words(123456))  # сто двадцать три тысячи четыреста пятьдесят шесть
print(number_to_words(123000))  # сто двадцать три тысячи
print(number_to_words(123005))  # сто двадцать три тысячи  пять
print(number_to_words(123015))  # сто двадцать три тысячи пятнадцать
print(number_to_words(12115))  # двенадцать тысяч сто пятнадцать
print(number_to_words(2115))  # две тысячи сто пятнадцать
print(number_to_words(456))  # четыреста пятьдесят шесть
print(number_to_words(13))  # тринадцать
print(number_to_words(1))  # один
print(number_to_words(44444))  # сорок четыре тысячи четыреста сорок четыре
print(number_to_words(10001))  # десять тысяч  один
print(number_to_words(194555))  # сто девяносто четыре тысячи пятьсот пятьдесят пять
print(number_to_words(10101))  # десять тысяч сто  один

# for i in range(1000000):
#     print(number_to_words(i))
