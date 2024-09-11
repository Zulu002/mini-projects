def draw_sun():
    # Определяем размеры и параметры солнца
    sun_radius = 10
    center_x = 10
    center_y = 10

    # Определяем высоту и ширину выводимого изображения
    height = 20
    width = 20

    # Создаем пустое поле для "неба"
    sky = [[' ' for _ in range(width)] for _ in range(height)]

    # Рисуем солнце
    for y in range(height):
        for x in range(width):
            if (x - center_x) ** 2 + (y - center_y) ** 2 <= sun_radius ** 2:
                sky[y][x] = '*'

    # Выводим на экран
    for row in sky:
        print(''.join(row))

draw_sun()