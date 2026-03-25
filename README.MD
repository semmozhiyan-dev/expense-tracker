# Expense Tracker
A simple command-line expense tracker built with Python.
It lets you add expenses and store them permanently in 'data.json'.
## Features
- Menu-driven CLI
- Add Expense flow with input validation
- Persistent storage using a JSON file
- Safe handling of missing/empty data file
## Tech Stack
->Python 3
->JSON file storage
## Project Structure
main.py- Application logic and menu flow
data.json - Stored expense records
README.MD - Project documentation
## How To Run
1. Open a terminal in the project folder.
2. Run:python main.py
## Menu Options
When the app starts, choose one of the following:
1. Add Expense
2. View Expenses
3. Total Spending
4. Filter by Category
5. Exit
## Current Implementation Status
- Implemented:
	- Add Expense
	- Exit flow
- Placeholder only (to be implemented next):
	- View Expenses
	- Total Spending
	- Filter by Category
## Data Model
Each expense is saved in this format:
json
{
	"amount": 250.0,
	"category": "Food",
	"date": "2026-03-25",
	"note": "Dinner"
}
## Validation Rules
- Amount must be a number greater than 0
- Category cannot be empty
- Date must follow `YYYY-MM-DD`
- Note is optional
## Author
Semmozhiyan N S
B.E.Computer Science And Engineering
