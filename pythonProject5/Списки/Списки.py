# В языке Python список обозначается квадратными скобками ([]) , а отдельные
# элементы списка разделяются запятыми.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print('\b')

# Индексы работают с 0 а не с 1
print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])
print('\b')

# Так же существует специальный синтекс для обращения к последнему элементу списка  -1
print(bicycles[-1])
print('\b')

#Использование отдельных элементов из списка
print(f'My first bicycle was a {bicycles[0]}')
print('\b')

for b in bicycles:
    print(f'\b{b}'.title())