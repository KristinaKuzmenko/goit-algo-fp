import heapq
import networkx as nx
import matplotlib.pyplot as plt
import random


G = nx.Graph()

stops_2 = [
    "парк ім. Тараса Шевченко",
    "вул. Успенська",
    "вул. Тираспольська",
    "пл. Льва Толстого",
    "вул. Пастера",
    "Вул. Новосельського",
]
stops_3 = [
    "парк ім. Тараса Шевченко",
    "вул. Канатна",
    "вул. Катерининська",
    "вул. Преображенська",
    "вул. Прохоровська",
    "вул. Степова",
    "вул. Балківська",
    "Станція Застава 2",
    "вул. Стовпова",
    "Станція Застава 1",
]
stops_5 = [
    "вул. Новосельського",
    "вул. Преображенська",
    "вул. Троїцька",
    "вул. Канатна",
    "Куликово поле",
    "Залізничний вокзал",
    "проспект Шевченка",
    "Палац Спорту",
    "Аркадія",
]
stops_7 = [
    "вул. Архітекторська",
    "вул. Корольова",
    "3-тя станція Люстдорфської дороги",
    "1-а станція Люстдорфської дороги",
    "5-а станція Великого Фонтану",
    "Палац Спорту",
    "проспект Шевченка",
    "Куликово поле",
    "Залізничний вокзал",
    "вул. Пушкінська",
    "вул. Грецька",
    "вул. Преображенська",
    "пл. Льва Толстого",
]
stops_8 = [
    "вул. Хімічна",
    "вул. Грушевського",
    "вул. Розумовська",
    "вул. Прохоровська",
    "вул. Преображенська",
    "вул. Рішельєвська",
    "Залізничний вокзал",
]
stops_9 = [
    "вул. Космонавтів",
    "1-а станція Люстдорфської дороги",
    "5-а станція Великого Фонтану",
    "Палац Спорту",
    "проспект Шевченка",
    "Куликово поле",
    "вул. Канатна",
    "вул. Грецька",
]


all_stops = set(stops_2 + stops_3 + stops_5 + stops_7 + stops_8 + stops_9)

for stop in all_stops:
    G.add_node(stop)

routes = [stops_2, stops_3, stops_5, stops_7, stops_8, stops_9]

for route in routes:
    for i in range(len(route) - 1):
        G.add_edge(route[i], route[i + 1], weight=random.randint(1, 10))


def dijkstra(graph, start):
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0

    heap = [(0, start)]
    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        # Пропускаємо вершину, якщо ми вже отримали більш коротший шлях
        if current_distance > distances[current_vertex]:
            continue

        for neighbor in graph[current_vertex]:
            # Перевірка наявності ваги ребра, якщо немає - використовується вага за замовчуванням 1
            weight = graph[current_vertex][neighbor].get("weight", 1)
            distance = distances[current_vertex] + weight

            # Якщо знайдено коротший шлях до сусідньої вершини, обновлюємо його
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


if __name__ == "__main__":
    distances = dijkstra(G, "Палац Спорту")
    print('\n  Довжини найкоротших шляхів від зупинки "Палац Спорту" до всіх інших:')
    print(f"| {'Напрям поїздки':<35} | {'Відстань':<20} |")
    print(f"| {'-'*35} | {'-'*20} |")
    for station, path in distances.items():
        if station != "Палац Спорту":
            print(f"| {station:<35} | {path:^20} |")
