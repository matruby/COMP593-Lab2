Comp 595 - Scripting Applications - Lab #2

Learning Objectives:

. Initialize a complex data structure.
. Access individual values within a complex data structure.
. Modify and iterate through lists that are nested inside a complex data 
  structure. 
. Define and call functions that have complex data structure parameters.
. Use various methods of the list and str class to manipulate objects 
  nested inside a complex data structure.

Instructions:
Step 1 - Start Writing the Script

Create a new git repository, open the folder in VS Code, create a new Python 
script file and populate it with the module scructure show below.

Step 2 - Create a Complex Data Structure

Using a dictionary as the base object, initialize a data structure that contains
the following information. This dictionary object must be local to the main() 
function. 

Step 3 - Add Another Movie to the Data Structure

Within the main() function, after the data structure is initialized, add one more 
movie to the movie list in it.

Step 4 - Use a Function to Print Student Name and ID

Define a function that does the following:
    . Accepts one parameter: the data structure
    . Prints the following two sentences, replacing the words enclosed in braces
      with information from the data structure.

      My name is {full_name}, but you can call me Sir{first_name}.
      My Student ID is {student_id}.

    . Note: You may replace "Sir" with whatever title you want, e.g., Lord, 
      Queen, Ms., Darth
    . Hint: To extract only the first name from the full name in the data structure, 
      use a str class method to split the full name into a list of words.
 
Call the funcion from main()

Step 5 - Use a Function to Add Pizza Toppings to the Data Structure

Define a function that does the following:
    . Accepts two parameters: the data structure and a tuple of pizza toppings
    . Appends all pizza toppings in the tuple parameter to the end of the pizza
      toppings list in the data structure
    . Sorts all pizza toppings in the data structure alphabetically
    . Converts all pizza topping in the data structure to lowercase

Call the function from main() to add at least 2 more pizza toppings to the list
in the data structure. 

Step 6 - Use a Function to Print a Bullet List of Pizza Toppings

Define a function that does the following:
    . Accepts one parameter: the data structure
    . Prints the following sentence and bullet list, replacing the words 
      enclosed in braces with information from the data structure.
    
	My favourite toppings are: 
        - {pizza_topping_1}
        - {pizza_topping_2}
        - {pizza_topping_3} 

    . Note: the function must print all pizza toppings in the list, regardless
      of how many pizza toppings are in the list. One way to do this is to use
      a loop to iterate the list, printing one topping per iteration.

Call the function from main() twice. Place one function call before adding the 
toppings per step 4, and one function call after adding the toppings per step 5.

Step 7 - Use a Function to Print a Comma-Seperated List of Movie Genres

Define a function that does the following:

    . Accepts one parameter: the data structure
    . Prints the following sentence, replacing the words enclosed in braces with 
      information from the data structure.

	I like to watch {movie_1_genre}, {movie_2_genre}, ..., {movie_n_genre} movies. 

    . Note: The function must print the genres of all movies in the data structure,
      regardless of how many movie are in the data structure. 
    . Bonus: Print "and" after the last comma in the genre list.

Call the function from main()

Step 8 - Use a Function to Print a Comma-Seperated List of Movie Titles

Define a function that does the following:
    . Accepts one parameter: the movie list from the data structure
    . Prints the following sentence, replacing the words enclosed in braces with
      information from the movie list.

	Some of my favourite movies are {movie_1_title}, {movie_2_title}, ...,
        {movie_n_title}!

    . The movie titles must be printed with the first letter of each word in uppercase,
      e.g., A New Hope, The Empire Strikes Back, Return of The Jedi (Hint: Use a str
      class method)
    . Bonus: Print "and" after the last comma in the genre list.

Call the function from main().



