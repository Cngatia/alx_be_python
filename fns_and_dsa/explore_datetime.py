from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days_to_add):
    current_date = datetime.now().date()
    
    future_date = current_date + timedelta(days=days_to_add)
    
<<<<<<< HEAD
    print(f"Future Date:{future_date:} ")
=======
    print(f"Future Date: {future_date}")
>>>>>>> ff4181ae64fb3757bb26e7845948bd1cd4eb0a78

def main():
    display_current_datetime()
    
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
<<<<<<< HEAD

=======
>>>>>>> ff4181ae64fb3757bb26e7845948bd1cd4eb0a78
        calculate_future_date(days_to_add)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
