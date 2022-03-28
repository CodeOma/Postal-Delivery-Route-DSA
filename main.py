# Omar Ahmed #009580996
from os import error
from delivery import print_delivered, print_delivered_individual, total_miles, size

class Main:
    # This is the display message that is shown when the user runs the program. The interface is accessible from here
    print('\tC950 Assignment\t')
    print('\t------------------------------\t\n')
    print(f'Route was completed in {total_miles:.2f} miles.\n')

    user_input = input("""
    Please select an option or type 'quit' to end the program:
    1. Get delivery status for all packages at a specific time
    2. Get individual package status at particular time
    3. Quit
""")

    while user_input != 'quit' and user_input != '3':
        try:
        # Case if user selects Option #1
        # Get info for all packages at a particular time -> O(n)
            if user_input == '1':
                    time = input("""
                    Enter a time to receive the package status report for the given time.
                    Leave blank for End of day report
                    HH:MM:SS : """)
                    if(time == ""):
                        print_delivered()
                    else:
                        print_delivered(time)
            # Case if user selects Option #2
            # Get info for a single package at a particular time -> O(n)
            elif user_input == '2':
                try:
                    id = input("Enter a Package ID to receive the package status:")
                    time = input("""
                    Enter a time to receive report for given time.
                    Leave blank for End of day report
                    HH:MM:SS : """) 
                    if(id == ""):
                        raise ValueError("Can't be left empty")
                    if(0> int(id) or size < int(id)):
                        raise ValueError("No package with the following ID")
                    if(time == ""):
                        print_delivered_individual(int(id))
                    else:
                        print_delivered_individual(int(id), time)                  
                except Exception as e:
                    print(e)
                    id = input("Enter a Package ID to receive the package status:")
                    time = input("""
                    Enter a time to receive report for given time.
                    Leave blank for End of day report
                    HH:MM:SS : """)  
                    if(time == ""):
                        print_delivered_individual(id)
                    else:
                        print_delivered(id, time)  
            elif user_input == '3' or user_input ==  'quit':
                raise

            else:
                user_input = input("""
                Please select an option or type 'quit' to end the program:
                1. Get info for all packages at a particular time
                2. Get info for a single package at a particular time
                3. Quit
                """)
        except Exception as e:
            print(e)

print("\tGoodbye")