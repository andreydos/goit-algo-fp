items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items_data, budget):
    sorted_items = sorted(
        items_data.items(),
        key=lambda item: item[1]["calories"] / item[1]["cost"],
        reverse=True,
    )

    chosen_items = []
    total_cost = 0
    total_calories = 0

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            chosen_items.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return chosen_items, total_cost, total_calories


def dynamic_programming(items_data, budget):
    names = list(items_data.keys())
    item_count = len(names)
    dp = [[0 for _ in range(budget + 1)] for _ in range(item_count + 1)]

    for i in range(1, item_count + 1):
        name = names[i - 1]
        cost = items_data[name]["cost"]
        calories = items_data[name]["calories"]

        for current_budget in range(budget + 1):
            dp[i][current_budget] = dp[i - 1][current_budget]

            if cost <= current_budget:
                candidate = dp[i - 1][current_budget - cost] + calories
                if candidate > dp[i][current_budget]:
                    dp[i][current_budget] = candidate

    chosen_items = []
    current_budget = budget

    for i in range(item_count, 0, -1):
        if dp[i][current_budget] != dp[i - 1][current_budget]:
            name = names[i - 1]
            chosen_items.append(name)
            current_budget -= items_data[name]["cost"]

    chosen_items.reverse()
    total_cost = sum(items_data[name]["cost"] for name in chosen_items)
    total_calories = sum(items_data[name]["calories"] for name in chosen_items)

    return chosen_items, total_cost, total_calories


if __name__ == "__main__":
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dynamic_result = dynamic_programming(items, budget)

    print(f"Budget: {budget}")
    print()
    print("Greedy algorithm:")
    print(f"Items: {greedy_result[0]}")
    print(f"Total cost: {greedy_result[1]}")
    print(f"Total calories: {greedy_result[2]}")
    print()
    print("Dynamic programming:")
    print(f"Items: {dynamic_result[0]}")
    print(f"Total cost: {dynamic_result[1]}")
    print(f"Total calories: {dynamic_result[2]}")
