import random
from collections import OrderedDict
import matplotlib.pyplot as plt


def simutate_dice_tosses(n):
    sums = [sum(random.choices([1, 2, 3, 4, 5, 6], k=2)) for _ in range(n)]
    count_sums = {sum: sums.count(sum) for sum in sums}
    return OrderedDict(sorted(count_sums.items()))


def draw_histogram(probabilities):
    plt.bar(probabilities.keys(), probabilities.values())
    plt.xlabel("Sum of two dice")
    plt.ylabel("Probability, %")
    plt.title(f"Simulate {n} tosses of two dice")
    plt.show()


def table_of_probabilities(sums, n):
    print(f"| {'Sum':<25} | {'Count of sums':<25} | {'Probability, %':<25} |")
    print(f"| {'-'*25} | {'-'*25} | {'-'*25} |")
    for sum, count in sums.items():
        print(f"| {sum:<25} | {count:<25} | {count/n:<25.2%} |")


if __name__ == "__main__":
    n = 10000
    sums = simutate_dice_tosses(n)
    probabilities = {sum: count / n * 100 for sum, count in sums.items()}
    print(f"Simulate {n} tosses of two dice:")
    table_of_probabilities(sums, n)
    draw_histogram(probabilities)
