def show_menu():
	print("\nExpense Tracker Menu")
	print("1. Add Expense")
	print("2. View Expenses")
	print("3. Total Spending")
	print("4. Filter by Category")
	print("5. Exit")
def main():
	while True:
		show_menu()
		choice = input("Enter your choice (1-5): ").strip()
		if choice == "1":
			print("Add Expense selected")
		elif choice == "2":
			print("View Expenses selected")
		elif choice == "3":
			print("Total Spending selected")
		elif choice == "4":
			print("Filter by Category selected")
		elif choice == "5":
			print("Exiting... Goodbye!")
			break
		else:
			print("Invalid choice, try again")
if __name__ == "__main__":
	main()
