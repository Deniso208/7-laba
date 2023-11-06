import random

def generate_random_array():
    # Ініціалізуємо пустий масив
    array = []
    
    # Додаємо 20% нульових елементів (8 елементів)
    for _ in range(8):
        array.append(0)
    
    # Додаємо 50% від'ємних елементів (20 елементів)
    for _ in range(20):
        array.append(-random.randint(1, 64))
    
    # Додаємо 30% додатних елементів (11 елементів)
    for _ in range(11):
        array.append(random.randint(1, 64))
    
    # Перемішуємо масив, щоб забезпечити різні масиви при кожному запуску
    random.shuffle(array)
    
    return array

if __name__ == "__main__":
    random_array = generate_random_array()
    print(random_array)
