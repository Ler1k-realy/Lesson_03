result = []

def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
            raise IndexError
    return a / b

data = {10 : 2, 2 : 5, 16: 4, 18 : 0 , 30: 15, 8 : 4}

for key, value in data.items():
    try:
        res = divider(key, value)
        result.append(res)
    except ZeroDivisionError:
        print(f"Помилка: НА НУЛЬ ДІЛИТИ НЕ МОЖНА АЛОООО ТИ БЕЗДАРЬ, ЧУРКА, ЧМО. ТИ ЩО ВИЩУ МАТЕМАТИКУ ЗНАЄШ ? НЄ? ТО ЗАКРИВ ЦЮ ПРОГРАМУ НАХЕР {key}")
    except ValueError as e:
        print(f"Error: {e} for key {key}")
    except IndexError as e:
        print(f"Error: {e} for key {key}")

print(result)
