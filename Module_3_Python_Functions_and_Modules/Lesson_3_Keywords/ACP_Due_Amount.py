def calculate_due_amount(bill_amount, amount_paid):
    return amount_paid - bill_amount


bill_amount = float(input("Enter the total bill amount: $"))
amount_paid = float(input("Enter the amount paid: $"))

due_amount = calculate_due_amount(
    bill_amount=bill_amount,
    amount_paid=amount_paid
)

if due_amount > 0:
    print(f"Change to return: ${due_amount:.2f}")
elif due_amount == 0:
    print("No change to return.")
else:
    print(f"Remaining amount to pay: ${abs(due_amount):.2f}")