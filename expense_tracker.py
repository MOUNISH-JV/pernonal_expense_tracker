import os  # Importing the os module to check if the file exists and to handle file operations.


# Class to manage the expense tracking
class ExpenseTracker:
    # Initialize the class with the filename to store expenses
    def __init__(self, filename='expenses.txt'):
        self.filename = filename  # Store the file name as an instance variable
        self.ensure_file_exists()  # Ensure the file exists when the object is created

    # Method to ensure the expenses file exists, create it if not
    def ensure_file_exists(self):
        if not os.path.isfile(self.filename):  # Check if the file exists
            # If the file does not exist, create it and add a header
            with open(self.filename, 'w') as file:
                file.write("Category,Amount,Description\n")  # Writing the header for CSV format

    # Method to add a new expense to the file
    def add_expense(self, category, amount, description):
        # Open the file in append mode to add the new expense as a line
        with open(self.filename, 'a') as file:
            # Write the new expense in the format: Category, Amount, Description
            file.write(f"{category},{amount},{description}\n")

    # Method to view all the expenses stored in the file
    def view_expenses(self):
        with open(self.filename, 'r') as file:  # Open the file in read mode
            lines = file.readlines()[1:]  # Read all lines except the header (skip first line)

        expenses = []  # Initialize an empty list to store the expense dictionaries
        # Loop through each line and split the values into category, amount, and description
        for line in lines:
            category, amount, description = line.strip().split(',', 2)
            # Append the expense details as a dictionary to the expenses list
            expenses.append({
                'category': category,
                'amount': float(amount),  # Convert the amount to a float
                'description': description
            })
        return expenses  # Return the list of expenses

    # Method to delete an expense by its index (position in the list)
    def delete_expense(self, index):
        expenses = self.view_expenses()  # Get the current list of expenses
        if 0 <= index < len(expenses):  # Check if the provided index is valid
            # Open the file in write mode to overwrite it after deleting the expense
            with open(self.filename, 'w') as file:
                file.write("Category,Amount,Description\n")  # Rewrite the header
                # Write back all expenses except the one to be deleted
                for i, exp in enumerate(expenses):
                    if i != index:  # Skip the expense at the specified index
                        file.write(f"{exp['category']},{exp['amount']},{exp['description']}\n")
            return True  # Return True if deletion was successful
        return False  # Return False if index was invalid


# Main function to interact with the expense tracker using a simple menu interface
def main():
    tracker = ExpenseTracker()  # Create an instance of the ExpenseTracker class

    while True:  # Infinite loop to keep the program running until the user decides to exit
        # Print the menu options
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")  # Get the user's choice from the menu

        if choice == '1':  # If the user chooses to add an expense
            category = input("Enter category: ")  # Get the expense category from the user
            amount = float(input("Enter amount: "))  # Get the amount and convert it to a float
            description = input("Enter description: ")  # Get the description of the expense
            tracker.add_expense(category, amount, description)  # Add the expense to the tracker
            print("Expense added successfully!")  # Confirmation message

        elif choice == '2':  # If the user chooses to view all expenses
            expenses = tracker.view_expenses()  # Retrieve all expenses from the tracker
            if not expenses:  # If there are no expenses, inform the user
                print("No expenses found.")
            else:
                # Loop through each expense and print its details
                for i, exp in enumerate(expenses):
                    print(f"Expense {i + 1}:")
                    print(f"  Category: {exp['category']}")
                    print(f"  Amount: ${exp['amount']:.2f}")
                    print(f"  Description: {exp['description']}")

        elif choice == '3':  # If the user chooses to delete an expense
            index = int(input("Enter expense index to delete: ")) - 1  # Get the index of the expense to delete
            if tracker.delete_expense(index):  # If the expense is successfully deleted
                print("Expense deleted successfully!")
            else:
                print("Invalid index.")  # If the provided index is invalid

        elif choice == '4':  # If the user chooses to exit the program
            print("Exiting...")  # Exit message
            break  # Exit the loop and terminate the program

        else:
            print("Invalid choice. Please try again.")  # Handle invalid menu choices


# Ensures that the main function is called when the script is executed
if __name__ == "__main__":
    main()  # Call the main function
