def get_efficiency(items):
    efficiency = {}
    for item, properties in items.items():
        efficiency[item] = properties["calories"] / properties["cost"]
    return efficiency


def greedy_algorithm(items, limit):
    efficiency = get_efficiency(items)
    sorted_items = sorted(items, key=efficiency.get, reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0
    for item in sorted_items:
        if total_cost + items[item]["cost"] <= limit:
            selected_items.append(item)
            total_cost += items[item]["cost"]
            total_calories += items[item]["calories"]
    return selected_items, total_cost, total_calories


def dynamic_programming(items, limit):
    n = len(items)
    items = list(items.items())
    # створюємо таблицю K для зберігання оптимальних значень підзадач
    K = [[0 for _ in range(limit + 1)] for _ in range(n + 1)]

    # будуємо таблицю K знизу вгору
    for item in range(1, n + 1):
        item_cost = items[item - 1][1]["cost"]
        item_calories = items[item - 1][1]["calories"]
        for cost in range(limit + 1):
            if cost >= item_cost:
                K[item][cost] = max(
                    K[item - 1][cost], item_calories + K[item - 1][cost - item_cost]
                )
            else:
                K[item][cost] = K[item - 1][cost]

    # проходження в зворотному напрямку для визначення вибраних елементів
    selected_items = []
    cost = limit
    for item in range(n, 0, -1):
        if K[item][cost] != K[item - 1][cost]:
            selected_items.append(items[item - 1][0])
            cost -= items[item - 1][1]["cost"]

    return K[n][limit], selected_items


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }
    limit = 100
    greedy_selected_items, greedy_total_cost, greedy_total_calories = greedy_algorithm(
        items, limit
    )
    print(
        f"Using greedy algorithm, we can buy these items with total calories {greedy_total_calories} by {limit} limit:"
    )
    print(",".join(greedy_selected_items))

    dynamic_total_calories, dynamic_selected_items = dynamic_programming(items, limit)
    print(
        f"Using dynamic programming, we can buy these items with total calories {dynamic_total_calories} by {limit} limit:"
    )
    print(",".join(dynamic_selected_items))
