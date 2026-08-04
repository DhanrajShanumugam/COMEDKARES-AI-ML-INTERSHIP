# Restaurant Billing System with 18% GST

print("===== RESTAURANT BILLING SYSTEM =====")

customer_name = input("Enter Customer Name: ")

num_items = int(input("Enter Number of Items: "))

subtotal = 0

print("\nEnter Item Details:")

for i in range(num_items):
    item_name = input(f"Item {i+1} Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per Item: "))

    total = quantity * price
    subtotal += total

gst = subtotal * 0.18
grand_total = subtotal + gst

print("\n" + "=" * 40)
print("        RESTAURANT BILL")
print("=" * 40)
print(f"Customer Name : {customer_name}")
print(f"Subtotal      : ₹{subtotal:.2f}")
print(f"GST (18%)     : ₹{gst:.2f}")
print("-" * 40)
print(f"Grand Total   : ₹{grand_total:.2f}")
print("=" * 40)

print("Thank You! Visit Again.")
