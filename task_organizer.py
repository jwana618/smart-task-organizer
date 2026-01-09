# ------------------------------------------
# SMART TASK ORGANIZER PROGRAM
# ------------------------------------------
# This program helps users manage their tasks.
# Users can:
# 1. Add new tasks
# 2. View all added tasks
# 3. Delete a task by its index
# 4. Exit the program
# ------------------------------------------


tasks = []  # This will save all added tasks in a list for easy access


# ------------------------------------------
# FUNCTION 1: Add_Task()
# ------------------------------------------
# Purpose:
# Allows the user to add one or multiple tasks to the list.
def Add_Task():
   while True:  # A loop so the user can add more than one task without restarting the program
    task_name = input('\nEnter Task: ')  # Asks the user to type the task name
    tasks.append(task_name)  # Adds (appends) the new task to the global tasks list
    print('\nTask Added Successfully!')  # Confirmation message

    # Ask the user if they want to add another task or stop
    add_option = input("\nWould you like to add another task? (yes/no): ")

    # If the user types "yes", the loop continues (they can add more tasks)
    if add_option == "yes":
            continue
    # If the user types "no", the loop ends (stops adding tasks)
    elif add_option == "no":
            break
    # If the user types something else, nothing happens and the loop ends by default
        

# ------------------------------------------
# FUNCTION 2: View_Tasks()
# ------------------------------------------
# Purpose:
# Displays all the tasks currently stored in the list.
def View_Tasks():
     print("\n----Tasks List---")  # Prints a header for the list
     
     # Loops through each element (task) inside the list
     for t in tasks:  # 't' represents each task_name in the list
            print(f"\n - {t}", end = ''+'\n')  # Prints each task with a dash for formatting


# ------------------------------------------
# FUNCTION 3: Delete_Task()
# ------------------------------------------
# Purpose:
# Deletes a specific task chosen by the user using its index.
def Delete_Task():   
    # Ask the user which task number they want to delete.
    # Note: indexing in Python starts at 0, so task 1 = index 0, task 2 = index 1, etc.
    i = eval(input('\nPlease choose the task number you want to delete (0 = task 1): '))
    
    # Remove the selected task from the list using the pop() function
    tasks.pop(i)
    
    print('\nTask Deleted Successfully!')  # Confirmation message


# ------------------------------------------
# FUNCTION 4: return_to_menu()
# ------------------------------------------
# Purpose:
# Gives the user the choice to return to the main menu or exit the program.
def return_to_menu():
    while True:  # Keeps asking until the user types a valid answer (yes or no)
        option = input("\nWould you like to return to the main menu? (yes/no): ")
        
        if option == "yes":
            # If 'yes' → return True, so the main program continues
            return True
        elif option == "no":
            # If 'no' → print a goodbye message and return False to stop the program
            print("\nExiting.. Have a nice day!\n\n")
            return False
            break  # This break is technically not needed since return already stops the function
        else:
            # If user types anything else, show an error and ask again
            print("ERROR: Please Enter 'yes' or 'no'")
            continue


# ------------------------------------------
# MAIN PROGRAM LOOP
# ------------------------------------------
# Purpose:
# Continuously shows a menu to the user until they choose to exit.
while True:
    # Print the main menu
    print('\n--Welcome to your Smart Task Ogranizer!--')
    print(' What would you like to do?\n\n1- Add new Task.\n\n2- View all tasks.\n\n3- Delete a task.\n\n4- Exit')
    
    # Ask the user for their choice (1 to 4)
    choice = eval(input("\nPlease select desired choice to continue: "))

    # If the user chooses 1 → call the Add_Task() function
    if choice == 1:
        Add_Task()
        # After finishing adding, ask if they want to return to the menu
        if return_to_menu() == False:  # If the user says 'no', exit the main loop
            break 

    # If the user chooses 2 → call the View_Tasks() function
    elif choice == 2:
        View_Tasks()
        # After viewing, ask if they want to go back or exit
        if return_to_menu() == False:
            break 
    
    # If the user chooses 3 → call the Delete_Task() function
    elif choice == 3:
        Delete_Task()
        # After deleting, ask if they want to continue or exit
        if return_to_menu() == False:
            break 
    
    # If the user chooses 4 → exit immediately
    elif choice == 4:
        print('\nExiting..Have a nice day!\n\n')
        break  

    # If the user types a number that’s not between 1–4, show an error
    else:
        print("\nInvalid input. Please enter a number between 1 and 4.")
