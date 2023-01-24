
def main():
    """Some facts about me in dictionary"""
    # Create the dictionary of my personal information
    personal_dict = {
            'full name': 'Matthew Rubie',
            'student_id': 10197289,
            'pizza_toppings': ['PEPPERONI', 'MUSHROOMS', 'HAM'],
            'movies': [
                {'title':'the dark knight', 'genre':'action/superhero'},
                {'title':'superbad', 'genre':'comedy'},
                ]
            }

    # Add a new movie to the dictionary
    personal_dict['movies'].append({'title':'us', 'genre':'horror'})

    # Get the name string and store it to be used later
    name_id_str = view_name_id(personal_dict)
    # Print out the list of pizza toppings
    bullet_list(personal_dict)
    # Add new toppings, sort the current ones alphabetically, convert to lowercase
    add_topping(personal_dict, ('Green Pepper', 'Onions'))
    # Print ou the list of pizza toppings with the changes made
    bullet_list(personal_dict)

    return 

def view_name_id(comp_ds):
    """Prints out name and student ID"""
    # Get name and student ID from dictionary
    full_name = comp_ds['full name'] 
    student_id = comp_ds['student_id']

    # Use split to get the first name
    first_name = full_name.split()[0]

    # Strings to be returned
    name_str = f'\nMy name is {full_name}, but you can call me Sir {first_name}\n' + \
    f'My student ID is {student_id}\n'

    print(name_str)

def add_topping(comp_ds, toppings):
    """Append pizza toppings to the end of the list"""
    # Add toppings to the pizza_toppings entry
    for topping in toppings:
        comp_ds['pizza_toppings'].append(topping)

    # Sort the pizza toppings alphabetically
    comp_ds['pizza_toppings'].sort()

    # Convert all pizza toppings to lowercase
    topping_len = len(comp_ds['pizza_toppings'])
    for count in range(topping_len):
        topping = comp_ds['pizza_toppings'][count]
        comp_ds['pizza_toppings'][count] = topping.lower()
    
    return comp_ds

def bullet_list(comp_ds):
    """Prints pizza toppings in a bullet list"""
    # Loop over the list and print them out one by one
    for topping in comp_ds['pizza_toppings']:
        print(f'- {topping}')
    print('\n')
    
    

if __name__ == '__main__': 
    main()
    

