items = []
prices = []

while True:
    # Get the item.
    item = input("Enter a item you bought (or type 'q' to stop): ")

    # Check the user wants to stop.
    if item == "q":
        break

    # Add the item to the empty list.
    items.append(item)

    # Get the price and ensure it's a valid integer
    while True:
        price = input("Enter a price of item: ")
        try:
            number = int(price)
            prices.append(number)
            break # Exit the loop if the price is valid
        except ValueError:
            print("Please enter a valid price.")

# Show every item and price.
print(f"all items:", items)
print(f"All price:", prices)

# Show total price.
print(f"\ntotla price:", sum(prices))