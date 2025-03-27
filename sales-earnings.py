import logging

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main function to calculate the salesperson's pay based on sales, advance pay, and commission rate.
    """
    try:
        # Get the amount of sales.
        sales = get_sales()

        # Get the amount of advanced pay.
        advanced_pay = get_advanced_pay()

        # Determine the commission rate.
        comm_rate = determine_comm_rate(sales)

        # Calculate the pay.
        pay = sales * comm_rate - advanced_pay

        # Display the amount of pay.
        print(f"The pay is ${pay:,.2f}")

        # Determine whether the pay is negative.
        if pay < 0:
            print("The salesperson must reimburse the company.")
        else:
            print("The salesperson has earned their pay.")

    except Exception as e:
        logging.error(f"Error in main: {e}")
        print(f"An error occurred: {e}")


def get_sales():
    """
    Gets the salesperson's monthly sales input and validates it.
    
    Returns:
        float: The monthly sales value.
    """
    while True:
        try:
            sales = float(input("Enter the amount of monthly sales: $"))
            if sales < 0:
                raise ValueError("Sales amount cannot be negative.")
            return sales
        except ValueError as e:
            logging.error(f"Invalid input for sales: {e}")
            print("Please enter a valid sales amount.")

        
def get_advanced_pay():
    """
    Gets the amount of advanced pay given to the salesperson.
    
    Returns:
        float: The advanced pay amount.
    """
    while True:
        try:
            advanced_pay = float(input("Enter the amount of advanced pay, or enter 0 if no advanced pay: $"))
            if advanced_pay < 0:
                raise ValueError("Advanced pay cannot be negative.")
            return advanced_pay
        except ValueError as e:
            logging.error(f"Invalid input for advanced pay: {e}")
            print("Please enter a valid amount for advanced pay.")


def determine_comm_rate(sales):
    """
    Determines the applicable commission rate based on sales.
    
    Args:
        sales (float): The total sales amount.
    
    Returns:
        float: The commission rate.
    """
    if sales < 10000.00:
        rate = 0.10
    elif 10000 <= sales <= 14999.99:
        rate = 0.12
    elif 15000 <= sales <= 17999.99:
        rate = 0.14
    elif 18000 <= sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18

    logging.info(f"Sales: ${sales}, Commission rate: {rate * 100}%")
    return rate


if __name__ == "__main__":
    main()

