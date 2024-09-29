from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    
    formatted_date = current_date.strftime("YYYY-MM-DD HH:MM:SS")
    
    return(f"Current date and time: {formatted_date}")

def calculate_future_date(days_to_add):
    current_date = datetime.now().date()
    
    future_date = current_date + timedelta(days=days_to_add)
    
    print(f"The date {days_to_add} days from today will be: {future_date}")

def main():
    display_current_datetime()
    
    try:
        days_to_add = int(input("Enter the number of days to add to add to the current date: "))

        calculate_future_date(days_to_add)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
