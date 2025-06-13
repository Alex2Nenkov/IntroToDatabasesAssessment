import sqlite3

def get_shopper_full_name(conn, shopper_id):
    """Retrieve the full name of the shopper if the shopper_id exists."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT shopper_first_name, shopper_surname
        FROM shoppers
        WHERE shopper_id = ?
    """, (shopper_id,))
    row = cursor.fetchone()
    if row:
        return f"{row[0]} {row[1]}"
    else:
        return None

def print_main_menu():
    """Prints the main menu for the shopper."""
    print("\nPARANÁ – SHOPPER MAIN MENU\n")
    print("1. Display your order history")
    print("2. Add an item to your basket")
    print("3. View your basket")
    print("4. Change the quantity of an item in your basket")
    print("5. Remove an item from your basket")
    print("6. Checkout")
    print("7. Exit\n")

def main():
    # Connect to the database
    conn = sqlite3.connect('parana.db')

    # Prompt for shopper_id
    shopper_id = input("Enter your shopper_id: ").strip()

    # Validate shopper
    shopper_name = get_shopper_full_name(conn, shopper_id)

    if not shopper_name:
        print("Error: shopper_id not found. Exiting program.")
        conn.close()
        return

    print(f"Welcome, {shopper_name}!")
    print_main_menu()

    # Keep connection open for future menu options
    conn.close()

if __name__ == "__main__":
    main()
