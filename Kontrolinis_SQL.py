import sqlite3

def create_table():
    conn = sqlite3.connect('finances.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Finances (
            id INTEGER PRIMARY KEY,
            type TEXT NOT NULL CHECK (type IN ('income', 'expenses')),
            amount REAL NOT NULL,
            category TEXT NOT NULL
        );
    ''')

    conn.commit()
    conn.close()

def enter_income():
    conn = sqlite3.connect('finances.db')
    cursor = conn.cursor()

    income_amount = float(input('Enter income amount: '))
    income_category = input('Enter income category: ')

    cursor.execute('''
        INSERT INTO Finances (type, amount, category)
        VALUES (?, ?, ?);
    ''', ('income', income_amount, income_category))

    conn.commit()
    conn.close()

def enter_expense():
    conn = sqlite3.connect('finances.db')
    cursor = conn.cursor()

    expense_amount = float(input('Enter expense amount: '))
    expense_category = input('Enter expense category: ')

    cursor.execute('''
        INSERT INTO Finances (type, amount, category)
        VALUES (?, ?, ?);
    ''', ('expenses', expense_amount, expense_category))

    conn.commit()
    conn.close()

def get_balance():
    conn = sqlite3.connect('finances.db')
    cursor = conn.cursor()

    cursor.execute('SELECT SUM(CASE WHEN type = "income" THEN amount ELSE -amount END) AS balance FROM Finances;')
    balance = cursor.fetchone()[0]

    conn.close()
    return balance

def get_all_incomes():
    conn = sqlite3.connect('finances.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Finances WHERE type="income";')
    incomes = cursor.fetchall()

    conn.close()
    return incomes

def get_all_expenses():
    conn = sqlite3.connect('finances.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Finances WHERE type="expenses";')
    expenses = cursor.fetchall()

    conn.close()
    return expenses

def delete_entry(entry_id):
    conn = sqlite3.connect('finances.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM Finances WHERE id=?;', (entry_id,))

    conn.commit()
    conn.close()

def main_menu():
    create_table()

    while True:
        print('\n1. Enter Income')
        print('2. Enter Expense')
        print('3. Get Balance')
        print('4. Get All Incomes')
        print('5. Get All Expenses')
        print('6. Delete Entry')
        print('7. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            enter_income()
            print('Income entered successfully!')
        elif choice == '2':
            enter_expense()
            print('Expense entered successfully!')
        elif choice == '3':
            balance = get_balance()
            print(f'Balance: {balance}')
        elif choice == '4':
            incomes = get_all_incomes()
            print('\nAll Incomes:')
            for income in incomes:
                print(income)
        elif choice == '5':
            expenses = get_all_expenses()
            print('\nAll Expenses:')
            for expense in expenses:
                print(expense)
        elif choice == '6':
            entry_id = int(input('Enter the ID of the entry to delete: '))
            delete_entry(entry_id)
            print('Entry deleted successfully!')
        elif choice == '7':
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == "__main__":
    main_menu()
