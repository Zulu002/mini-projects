def draw_diamond(size):
    # Верхняя часть ромба
    for i in range(size):
        # Печать пробелов
        print(' ' * (size - i - 1), end='')
        # Печать звездочек
        print('*' * (2 * i + 1))
    
    # Нижняя часть ромба
    for i in range(size - 2, -1, -1):
        # Печать пробелов
        print(' ' * (size - i - 1), end='')
        # Печать звездочек
        print('*' * (2 * i + 1))

# Задаем размер ромба
size = 5
draw_diamond(size)