
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

    name_id_str = view_name_id(personal_dict)
    return 

def view_name_id(comp_ds):
    """Prints out name and student ID"""
    # Get name and student ID from dictionary
    full_name = comp_ds['full name'] 
    student_id = comp_ds['student_id']

    # Use split to get the first name
    first_name = full_name.split()[0]

    # Strings to be returned
    name_str = f'My name is {full_name}, but you can call me Sir {first_name}\n' + \
    f'My student ID is {student_id}'

    return name_str 

if __name__ == '__main__': 
    main()

