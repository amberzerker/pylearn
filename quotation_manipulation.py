# Манипуляции с цитатой
# Демонстрирует строковые методы
# цитата Томаса Уотсона, который в 1943 году был директором IBM

quote = "Думаю, на мировом рынке можно будет продать штук пять компьютеров."
print("Исходная цитата:", quote)
print("\nОна же в верхнем регистре:", quote.upper())
print("\nВ нижнем регистре:", quote.lower())
print("\nКак заголовок:", quote.title())
print("\nС ма-а-аленькой заменой:", quote.replace("штук пять", "несколько миллионов"))
print("\nА вот опять исходная цитата:", quote)
input("\n\nНажмите Enter, чтобы выйти.")