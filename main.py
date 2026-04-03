import json
from datetime import datetime
DATA_FILE = "data.json"
def show_menu():
	print("\nExpense Tracker Menu")
	print("1. Add Expense")
	print("2. View Expenses")
	print("3. Total Spending")
	print("4. Filter by Category")
	print("5. Exit")
def load_expenses():
	try:
		with open(DATA_FILE, "r", encoding="utf-8") as file:
			content = file.read().strip()
			if not content:
				return []
			data = json.loads(content)
			return data if isinstance(data, list) else []
	except FileNotFoundError:
		return []
	except json.JSONDecodeError:
		print("Warning: data file is invalid. Starting with empty expenses list.")
		return []
def save_expenses(expenses):
	with open(DATA_FILE, "w", encoding="utf-8") as file:
		json.dump(expenses, file, indent=2)
def get_amount_input():
	while True:
		amount_text = input("Enter amount: ").strip()
		try:
			amount = float(amount_text)
			if amount <= 0:
				print("Amount must be greater than 0. Try again.")
				continue
			return amount
		except ValueError:
			print("Invalid amount. Please enter a number.")
def get_category_input():
	while True:
		category = input("Enter category: ").strip()
		if category:
			return category
		print("Category cannot be empty. Try again.")
def get_date_input():
	while True:
		date_text = input("Enter date (YYYY-MM-DD): ").strip()
		try:
			datetime.strptime(date_text, "%Y-%m-%d")
			return date_text
		except ValueError:
			print("Invalid date format. Use YYYY-MM-DD.")
def add_expense():
	expenses = load_expenses()
	amount = get_amount_input()
	category = get_category_input()
	date_text = get_date_input()
	note = input("Enter note (optional): ").strip()
	expense = {
		"amount": amount,
		"category": category,
		"date": date_text,
		"note": note,
	}
	expenses.append(expense)
	save_expenses(expenses)
	print("Expense added successfully")
def view_expenses():
	expenses = load_expenses()
	if not expenses:
		print("No expenses found.")
		return
	print("\nSaved Expenses")
	for index, expense in enumerate(expenses, start=1):
		amount = expense.get("amount", 0)
		category = expense.get("category", "Unknown")
		date_text = expense.get("date", "Unknown")
		note = expense.get("note", "")
		note_text = note if note else "N/A"
		print(
			f"{index}. Amount: Rs.{amount} | Category: {category} | Date: {date_text} | Note: {note_text}"
		)
def total_spending():
	expenses = load_expenses()
	if not expenses:
		print("No expenses available to calculate total.")
		return
	amounts = []
	for expense in expenses:
		amounts.append(float(expense.get("amount", 0)))
	total = sum(amounts)
	print(f"Total Spending: Rs.{total}")
def filter_by_category():
	expenses = load_expenses()
	if not expenses:
		print("No expenses available.")
		return
	category_input = input("Enter category (Food, Travel, etc): ").strip().lower()
	if not category_input:
		print("Category cannot be empty. Try again.")
		return
	filtered_expenses = []
	for expense in expenses:
		expense_category = str(expense.get("category", "")).strip().lower()
		if expense_category == category_input:
			filtered_expenses.append(expense)
	if not filtered_expenses:
		print("No expenses found for this category.")
		return
	print(f"\nFiltered Expenses for category: {category_input}")
	for index, expense in enumerate(filtered_expenses, start=1):
		amount = expense.get("amount", 0)
		category = expense.get("category", "Unknown")
		date_text = expense.get("date", "Unknown")
		note = expense.get("note", "")
		note_text = note if note else "N/A"
		print(
			f"{index}. Amount: Rs.{amount} | Category: {category} | Date: {date_text} | Note: {note_text}"
		)
def main():
	while True:
		show_menu()
		choice = input("Enter your choice (1-5): ").strip()
		if choice == "1":
			add_expense()
		elif choice == "2":
			view_expenses()
		elif choice == "3":
			total_spending()
		elif choice == "4":
			filter_by_category()
		elif choice == "5":
			print("Exiting... Goodbye!")
			break
		else:
			print("Invalid choice, try again")
if __name__ == "__main__":
	main()
