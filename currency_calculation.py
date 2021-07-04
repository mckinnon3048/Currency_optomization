# prints the average number of units of currency to make change in order to test hypothetical

import random


def calculate_currency(currency_list, starting_change):
    # currency_list = [23, 19, 17, 13, 11, 7, 5, 3, 2, 1] # in descending order, the possible currency
    change = starting_change
    change_count = []
    change_avg = []
    for each in currency_list:
        change_avg.insert(0,0)
        change_count.insert(0,0)
    while change > 0:
        change_remaining = change
        for each in range(len(change_count)):
            change_count[each] = 0
        while change_remaining > 0:
            for c in range(len(currency_list)):
                while change_remaining > 0:
                    if change_remaining - currency_list[c] >= 0:
                        change_remaining = change_remaining-currency_list[c]
                        change_count[c] = change_count[c] + 1
                    else:
                        if c < (len(currency_list)):
                            c = c + 1
            # print(f"{change} - {change_count}")
            c = 0

        change -= 1
        for pos in range(len(change_avg)):
            change_avg[pos] = change_avg[pos] + change_count[pos]
    for pos in range(len(change_avg)):
        change_avg[pos] = (change_avg[pos] / starting_change)
    print
    # print(f"{currency_list} = {change_avg} --- sum: {sum(change_avg)}")
    # print(f"{currency_list} : {sum(change_avg)} units")
    return [currency_list, (sum(change_avg))]


def generate_currency(number_of_divisions):
    currency_list = [1]
    for x in range (number_of_divisions-1):
        currency_list.append(random.randint(2, 50))
    currency_list.sort(reverse=True)
    return currency_list


def find_best(iterations, number_of_divisions):
    starting_change = 50 # the max possible change to be produced
    best_option = [0,0]
    while iterations > 0:
        currency_list = generate_currency(number_of_divisions)
        current_test = calculate_currency(currency_list, starting_change)
        if best_option[1] == 0 or current_test[1] <= best_option[1]:
            best_option = current_test
        iterations -= 1

    print(f"The best is \n {best_option[0]} -- averaging {best_option[1]} units")


find_best(100000, 11)
