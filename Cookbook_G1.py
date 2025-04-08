# Digital Cookbook
listRecipes = []
nLen = len(listRecipes)

#Part A) Addinging Recipes/ Editing/ Deleting
def add_recipe(a_New):
    listRecipes.append(a_New)

def edit_recipe(a_RecipeID, a_Update):
    for key, value in a_Update.items():
        listRecipes[a_RecipeID][key] = value

def delete_recipe(a_RecipeID):
    if 0 <= a_RecipeID < nLen:
        del listRecipes[a_RecipeID]

def list_all_recipes():
    for i, recipe in (listRecipes):
        print("[{i}] {recipe['name']} ({recipe['cuisine']})")

# Part B) Ingredient/ Cusine Searching






# Part D) CLI & File Handling

def user_menu():
    while True:
        print("\n === Recipe Book Menu ===")
        print("1. Add Recipe")
        print("2. Edit Recipe")
        print("3. Delete Recipe")
        print("4. List All Recipes")
        print("5. Search by Ingredient")
        print("6. Filter by Cuisine")
        print("7. View Vegetarian Recipes")
        print("8. Group by Meal Type")
        """
        # Add necessary menu items with added features.
        print("9. Get shopping list")
        print("10. Scale recipe ingredients")
        print("11. Calculate total prep time")
        print("12. Random recipe suggestion")
        """
        print("13. Save Recipes to File")
        print("14. Load Recipes from File")
        print("0. Exit")
            
        choice = input("\nEnter your choice (0-14): ")
        handle_choice(choice)

        
def handle_choice(choice):
        if choice == "1": 
            add_recipe(a_New)
            
        elif choice == "2": 
            edit_recipe(a_RecipeID, a_Update)

        elif choice == "3": 
            delete_recipe(a_RecipeID)

        elif choice == "4": 
            list_all_recipes()
        
        elif choice == "5": 
            pass
            #search_by_ingredient()

        elif choice == "6": 
            pass
            #filter_by_cuisine()

        elif choice == "7": 
            pass
            #get_vegetarian_recipes()
        
        elif choice == "8":
            pass
            #group_by_meal_type()

    # Add necessary menu items with added features.
        #elif choice == "9":
        #    pass
        #elif choice == "10":
        #    pass
        #elif choice == "11":
        #    pass
        #elif choice == "12":
        #    pass
        
        elif choice == "13":
            pass
            #save_recipes_to_file()
        
        elif choice == "14":
            pass
            #load_recipes_from_file()

        elif choice == "0":
            print("Exiting program.")
            exit()
        
        else:
            print("Invalid option, try again.")

def save_recipes_to_file():
    pass

def load_recipes_from_file():
    pass

def format_recipe_display():
    pass

def format_recipe_display():
    """print:
            name
            cuisine
            meal type
            prep time
            vegetarian yes / no
            ingredients
            instructions
            ...
        """

# Run app

user_menu()


