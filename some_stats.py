from math import sqrt
from math import ceil


def run():

    data = []

    while True:
        print("[1] - Enter Data\n" +
              "[2] - View Data\n" +
              "[3] - Delete Data\n" +
              "[4] - Compute Statistics on Dataset\n" +
              "[5] - Compute Statistics on Specific Data Point\n"
              "[6] - Exit")

        selection = input("Select an option: ")
        print()

        try:
            selection = int(selection)
            if selection == 1:
                enter_data(data)
            elif selection == 2:
                view_data(data)
            elif selection == 3:
                delete_data(data)
            elif selection == 4:
                compute_set(data)
            elif selection == 5:
                compute_point(data)
            elif selection == 6:
                print("Exiting!")
                exit(0)
            else:
                print("Not a valid input! Try again.")
        except ValueError:
            print("Not a valid input! Try again,")


def enter_data(data_set):
    print("Enter all values, pressing return after each value.")
    print("Press 'Return' with no data entered to exit.")

    while True:
        entered = input("Enter a value: ")
        if entered == "":
            print("Completed entering data.\n")
            return
        else:
            try:
                entered = int(entered)
                data_set.append(entered)
                print("Value entered!")
            except ValueError:
                print("Not a valid input! Try again.")


def view_data(data_set):
    print("Data Set:")

    cols = 5

    for i in range(0, ceil(len(data_set) / cols)):
        for j in range(0, cols):
            if (i * cols) + j < len(data_set):
                print(str(data_set[i * cols + j]) + ", ", end="")
        print()


def delete_data(data_set):
    print("Enter values you'd like to delete one instance of, pressing return after each one.")
    print("Press 'Return' with no value entered to exit.")

    while True:
        entered = input("Enter a value to delete: ")
        if entered == "":
            print("Completed deleting data.\n")
            return
        else:
            try:
                entered = int(entered)
                if entered in data_set:
                    data_set.remove(entered)
                    print("Removed value!")
                else:
                    print("That value is not in the data set!")
            except ValueError:
                print("Not a valid input! Try again.\n")


def compute_set(data_set):

    def mean():
        if len(data_set) == 0:
            return "NO MEAN"
        else:
            return sum(data_set) / len(data_set)

    def median():
        sorted_set = sorted(data_set)

        if len(sorted_set) == 0:
            return "NO MEDIAN"
        elif len(sorted_set) % 2 == 0:
            return (sorted_set[int(len(sorted_set) // 2 - 1)] + sorted_set[int(len(sorted_set) // 2)]) / 2
        else:
            return sorted_set[len(sorted_set) // 2]

    def mode():
        if len(data_set) == 0:
            return "NO MODE"

        heights_mode = {}

        for item in data_set:
            if item in heights_mode:
                heights_mode[item] += 1
            else:
                heights_mode[item] = 1

        max_mode = max(heights_mode, key=heights_mode.get)

        if heights_mode[max_mode] == 1:
            return "NO MODE"
        else:
            return "[" + str(max_mode) + "] : " + str(heights_mode[max_mode])

    def variance():
        if len(data_set) == 0:
            return "NO VARIANCE"

        return ((sum([x ** 2 for x in data_set])) - ((sum(data_set) ** 2) / len(data_set))) / (len(data_set) - 1)

    def standard_deviation():
        if len(data_set) == 0:
            return "NO STANDARD DEVIATION"

        return sqrt(variance())

    def coefficient_of_variation():
        if len(data_set) == 0:
            return "NO COEFFICIENT OF VARIATION"

        return (standard_deviation() / mean()) * 100

    print("Computed Data:\n" +
          "Mean: " + str(mean()) + "\n" +
          "Median: " + str(median()) + "\n" +
          "Mode: " + str(mode()) + "\n" +
          "Variance: " + str(variance()) + "\n" +
          "Standard Deviation: " + str(standard_deviation()) + "\n" +
          "Coefficient of Variation: " + str(coefficient_of_variation()) + "\n")


def compute_point(data_set):
    sorted_set = sorted(data_set)

    def calc_percentile(position):
        if 0 > position >= len(sorted_set):
            print("Invalid input! Try again\n")
            return "INVALID"

        return round(((position - 1) / (len(data_set) - 1)), 2) * 100

    def calc_position(percentile):
        if percentile < 0 or percentile > 100:
            print("Invalid input! Try again\n")
            return "INVALID"

        return round((percentile * (len(data_set) - 1)) / 100)

    if len(data_set) == 0:
        print("Cannot compute any information on empty data set!\n")
        return

    while True:
        print("[1] - Calculate the percentile of a given position\n" +
              "[2] - Calculate the position of a given value\n" +
              "[3] - Cancel")

        selection = input("Select an option: ")
        print()

        try:
            selection = int(selection)
            if selection == 1:
                print("Positions corresponding to their data values:")
                for i in range(0, len(sorted_set)):
                    print("[" + str(i + 1) + "] - " + str(sorted_set[i]))

                selection = input("Provide a position: ")
                try:
                    selection = int(selection)
                    if 0 < selection <= len(sorted_set):
                        calculated_percentile = calc_percentile(selection)
                        print("The item: [" + str(sorted_set[selection - 1]) +
                              "] at position [" + str(selection) +
                              "] corresponds to percentile [" + str(calculated_percentile) + "].")
                    else:
                        print("Value selected out of bounds! Try again.\n")
                except ValueError:
                    print("Not a valid input! Try again.\n")
            elif selection == 2:
                selection = input("Provide a percentile: ")
                try:
                    selection = int(selection)
                    if 0 <= selection <= 100:
                        calculated_position = calc_position(selection)
                        if 0 <= selection <= 100:
                            if round(selection) == selection:
                                print("The percentile [" + str(selection) +
                                      "] corresponds to the item: [" +
                                      str(sorted_set[selection]) + "] at position: [" + str(calculated_position) + "].")
                            else:
                                print("The percentile [" + str(selection) +
                                      "] corresponds to position: [" + str(calculated_position) + "].")
                    else:
                        print("Not a valid percentile! Try again.")
                except ValueError:
                    print("Not a valid input! Try again.\n")
            elif selection == 3:
                print("Exiting menu!")
                return
            else:
                print("Not a valid input! Try again.\n")
        except ValueError:
            print("Not a valid input! Try again.\n")


if __name__ == '__main__':
    run()
