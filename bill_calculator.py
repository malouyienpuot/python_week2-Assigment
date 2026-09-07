name: str = "Malou"
age: int = 29
gender: str = "male"

price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity: "))

total = price * quantity

print(f"Customer: {name}, age {age}, gender {gender}")
print(f"{quantity} items at {price:.2f} each = {total:.2f}")
