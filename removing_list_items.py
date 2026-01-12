def main():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    days[0:3] = []  # Removing first three items from the list

    print(days)  # ['Thursday', 'Friday', 'Saturday', 'Sunday']

    days.remove("Saturday")  # Removing specific item by value


    print(days)  # ['Thursday', 'Friday', 'Sunday']

    # Removing last item using pop method
    days.pop()

    print(days)  # ['Thursday', 'Friday']

    item = days.pop(0)  # Removing item at index 0
    print(item)  # Thursday
    print(days)  # ['Friday']

    days.clear()  # Removing all items from the list

    print(days)  # []
    del days  # Deleting the entire list

    print(days)  # This will raise an error as the list is deleted
    return

main()