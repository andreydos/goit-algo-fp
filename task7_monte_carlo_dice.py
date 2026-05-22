import random
from collections import Counter


def monte_carlo_simulation(rolls):
    sums_counter = Counter()

    for _ in range(rolls):
        dice_sum = random.randint(1, 6) + random.randint(1, 6)
        sums_counter[dice_sum] += 1

    probabilities = {}
    for total in range(2, 13):
        probabilities[total] = sums_counter[total] / rolls

    return probabilities


def analytical_probabilities():
    ways = {
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6,
        8: 5,
        9: 4,
        10: 3,
        11: 2,
        12: 1,
    }

    return {total: count / 36 for total, count in ways.items()}


def print_table(monte_carlo, analytical):
    print("Sum | Monte Carlo | Analytical")
    print("--------------------------------")

    for total in range(2, 13):
        monte_carlo_percent = monte_carlo[total] * 100
        analytical_percent = analytical[total] * 100
        print(f"{total:>3} | {monte_carlo_percent:>10.2f}% | {analytical_percent:>9.2f}%")


def print_histogram(probabilities):
    print()
    print("Monte Carlo histogram:")

    for total in range(2, 13):
        bar = "#" * int(probabilities[total] * 100)
        print(f"{total:>2}: {bar}")


if __name__ == "__main__":
    rolls = 100000
    monte_carlo = monte_carlo_simulation(rolls)
    analytical = analytical_probabilities()

    print(f"Number of rolls: {rolls}")
    print_table(monte_carlo, analytical)
    print_histogram(monte_carlo)
