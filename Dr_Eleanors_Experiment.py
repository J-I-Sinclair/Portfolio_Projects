''' The purpose of this code is to create several functions which will do the
following:
1 - Define lists of pre-existing data, this being locations and their
radiation levels
2 - Create a dictionary with this data and prompt the user for the option
of displaying it
3 - Create another function which allows the user to add additional radiation
levels to any of the locations
4 - Create another function which calls the other functions and prints the
average and standard deviation for the radiation levels in each location'''

def data_arrangement(): # This function will define and arrange the data
    # Lists of values for our data
    location_list = ['city centre', 'industrial zone', 'residential district',
                     'rural outskirts','downtown'] 
    centre_list = [22, 19, 20, 31, 28]
    industrial_list = [35, 32, 30, 37, 40]
    residential_list = [15, 12, 18, 20, 14]
    rural_list = [9, 13, 16, 14, 7]
    downtown_list = [25, 18, 22, 21, 26]

    # A list made up of the above lists
    location_data_list = [centre_list, industrial_list, residential_list,
                          rural_list, downtown_list]

    # A dictionary linking the location names with their respective lists
    location_data_dict = {}
    for entry in range(len(location_list)):
        key = location_list[entry]
        value = location_data_list[entry]
        location_data_dict.update({key : value})

    # Prompt the user, asking for a choice on whether to display levels or not
    level_display_question = input("Would you like to display the radiation levels? Enter (y/n): ")
    if level_display_question.lower() == "y":
        levels_message = 0
        while levels_message < len(location_list):                  
            print(f"The radiation levels in the {location_list[levels_message]} are: {location_data_list[levels_message]}")
            levels_message += 1

    # Return our dictionary for use in other functions
    return(location_data_dict)

def data_alteration(): # This function will allow the user to add to the lists
    # Import the data dictionary from the previous function
    location_data_dict = data_arrangement()
    
    # Create a list of dictionary locations to act as keys
    dict_keys = []
    for location in location_data_dict.keys():
        dict_keys.append(location)

    # Prompt the user to add data to the lists if desired
    level_change_question = input("Would you like to add any data to the lists? Enter (y/n): ")
    
    # Prompt the user to select a location
    if level_change_question.lower() == "y":
        location_choice = input("Please enter your location choice."
                                f" Your options are {dict_keys}."
                                " Enter 'exit' to exit."
                                " Enter your choice here: ")
        
        # Match the input with a location if possible
        # While loop exits if user inputs 'exit'
        while location_choice.lower() != "exit":
            for choice1 in dict_keys: # Iterates through locations
                while choice1 == location_choice.lower():
                        new_value = int(input("Insert radiation figure here: "))
                        location_data_dict[choice1].append(new_value)
                        repeat_choice = input("Please input another number or type 'exit' to exit: ")
                        
                        # Allows for additional input and catches errors
                        while repeat_choice != "exit":
                            location_data_dict[choice1].append(int(repeat_choice))
                            repeat_choice = input("Please input another number or type 'exit' to exit :") 
                        
                        # Allows user to select another location and restarts loop
                        location_choice = input("Would you like to change another category?"
                                                " If so, enter the location from the list above."
                                                " Otherwise enter 'exit' again to exit: ")


    # Prints data
    print("Your radiation data: ") 
    print(location_data_dict)
    # Returns new data dictionary
    return(location_data_dict)

def experiment(): # Final function, combines others and calculates statistics
    # Import math module and define dictionary, calling previous function
    import math
    data_dict = data_alteration()
    keys = data_dict.keys()

    # calculate and output the averages
    for category in keys:
        data_set = data_dict[category]
        average = 0
        average = average + (sum(data_set) / len(data_set))
        average = round(average, 2)
        print(f"The average radiation in {category} is : {average}.")
    
    # calculate and output the standard deviation
    for category in keys:
        data_set = data_dict[category]
        num_sum = sum(data_set)
        square_sum = 0
        for num in data_set:
            square_sum = square_sum + num ** 2
        standard_deviation = math.sqrt((square_sum - ((num_sum ** 2) / len(data_set))) / (len(data_set) - 1)) 
        standard_deviation = round(standard_deviation, 2)

        # Prints results
        print(f"The standard deviation of radiation in {category} is {standard_deviation}.")

experiment()