
def main():
    """Some facts about me in dictionary"""
    # Create the dictionary of my personal information
    about_me = {
            'full name': 'Matthew Rubie',
            'student_id': 10197289,
            'pizza_toppings': ['PEPPERONI', 'MUSHROOMS', 'HAM'],
            'movies': [
                {'title':'the dark knight', 'genre':'action/superhero'},
                {'title':'superbad', 'genre':'comedy'},
                ]
            }

    about_me['movies'].append({'title':'us', 'genre':'horror'})# Step 3
    print(print_student_name_and_id(about_me))# Step 4
    print_pizza_toppings(about_me) # Step 6 pt 1
    add_pizza_toppings(about_me, ('Green Pepper', 'Onions'))# Step 5
    print_pizza_toppings(about_me) #Step 6 pt 2
    print(print_movie_genres(about_me)) # Step 7
    print(print_movie_titles(about_me['movies'])) # Step 8

    return None

def print_student_name_and_id(comp_ds):
    """Prints out student name and ID"""
    full_name = comp_ds['full name'] # Get full name from dict
    student_id = comp_ds['student_id']# Get Student ID from dict

    first_name = full_name.split()[0] # Get just the first name
    name_str = f'My name is {full_name}, but you can call me Sir {first_name}.\n' + \
    f'My student ID is {student_id}.\n'

    return name_str

def add_pizza_toppings(comp_ds, toppings):
    """Function that adds pizza toppings to data structure"""
    # Add toppings to the pizza_toppings entry
    for topping in toppings:
        comp_ds['pizza_toppings'].append(topping)
 
    comp_ds['pizza_toppings'].sort() # Sort toppings alphabetically
    # Convert all pizza toppings to lowercase
    comp_ds['pizza_toppings'] = [topping.lower() for topping in comp_ds['pizza_toppings']]
     
    return comp_ds

def print_pizza_toppings(comp_ds):
    """Prints bullet list of pizza toppings"""
    print('My favourite pizza toppings are:') # Title string
    # Loop over the list and print them out one by one
    for topping in comp_ds['pizza_toppings']:
        print(f'- {topping}')
    print('\n')
    
def print_movie_genres(comp_ds):
    """Prints comma-seperated list of movie genres"""
    # Add genre's to a list
    cs_genre_lst = [movie['genre'] for movie in comp_ds['movies']]
    
    last_entry = cs_genre_lst.pop(-1) # Pop the last genre from the list 
    cs_str = ', '.join(cs_genre_lst) + f', and {last_entry}'# Output str
    
    return f'I like to watch {cs_str} movies.'  

def print_movie_titles(movie_list):
    """Prints comma seperated list of movie titles"""
    movie_title_list = [entry['title'] for entry in movie_list]
    # Convert the list to title case
    movie_list = [mov_name.title() for mov_name in movie_title_list]

    last_entry = movie_list.pop(-1)# Pop the last title from the list 
    output_str = ', '.join(movie_list) + f', and {last_entry}' # Output str

    return f'Some of my favourite movies are {output_str}!'

if __name__ == '__main__': 
    main()
