# enter the number of years
years = int(input("Enter the number of years: "))

# list of total rainfall for each year
total_rainfall_each_year = []


for year in range(1, years + 1):
   
    total_rainfall = 0
    
    
    for month in range(1, 13):
        # Ask the user to enter the rainfall amount for the current month
        rainfall = float(input(f"Enter the rainfall amount for year {year}, month {month}: "))
        
       
        total_rainfall += rainfall
    
    # Add the total rainfall for the current year 
    total_rainfall_each_year.append(total_rainfall)
    
    # Calculate the average monthly rainfall
    avg_rainfall = total_rainfall / 12
    
    # Print the total rainfall and average monthly rainfall
    print(f"Total rainfall for year {year}: {total_rainfall}")
    print(f"Average monthly rainfall for year {year}: {avg_rainfall} \n")
