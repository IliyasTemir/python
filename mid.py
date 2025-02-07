# Функция для чтения данных из файла input.txt
def read_car_data(filename):
    cars = []
    with open(filename, 'r') as file:
        for line in file:
            x, y, speed = map(int, line.split())
            cars.append({'x': x, 'y': y, 'speed': speed})
    return cars

# Функция для вычисления времени, которое потребуется каждому автомобилю, чтобы достичь правого края экрана
def calculate_time_to_finish(cars, screen_width=500):
    times = []
    for car in cars:
        # Вычисляем время до правого края экрана
        time = (screen_width - car['x']) / car['speed']
        times.append(time)
    return times

# Функция для нахождения победителя (первый автомобиль, который достигнет правого края)
def find_winner(times):
    winner_index = times.index(min(times))
    return winner_index

# Функция для сохранения состояния игры в файл
import pickle
def save_game_state(cars, filename="game_state.pkl"):
    with open(filename, 'wb') as file:
        pickle.dump(cars, file)

# Функция для загрузки состояния игры из файла
def load_game_state(filename="game_state.pkl"):
    with open(filename, 'rb') as file:
        cars = pickle.load(file)
    return cars

# Основная функция, которая выполняет все шаги
def main():
    # Чтение данных о машинах из файла
    cars = read_car_data("input.txt")
    
    # Вычисляем, сколько времени потребуется каждому автомобилю, чтобы достичь правого края
    times = calculate_time_to_finish(cars)
    
    # Находим победителя (индекс машины, которая первой достигает правого края)
    winner_index = find_winner(times)
    print(f"The winning car is car #{winner_index + 1}")

    # Сохраняем состояние игры
    save_game_state(cars)
    
    # Загружаем сохраненное состояние игры
    loaded_cars = load_game_state()
    
    # Здесь можно добавить логику для рисования машин на экране с помощью pygame (если нужно)

if __name__ == "__main__":
    main()

