# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    # If the discount is 20% or more, go ahead and calculate the reduced price
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        # If the discount is less than 20%, no changes—keep the original price
        return price

# Let’s get the original price and discount percentage from the user
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Pass the inputs to our function to figure out the final price
    final_price = calculate_discount(original_price, discount_percent)

    # Tell the user whether a discount was applied or not
    if final_price == original_price:
        print(f"No discount applied. The original price remains: {original_price:.2f}")
    else:
        print(f"The final price after applying a {discount_percent}% discount is: {final_price:.2f}")
except ValueError:
    # If the user enters something that isn’t a number, let them know
    print("Oops! Please enter valid numbers for the price and discount percentage.")
