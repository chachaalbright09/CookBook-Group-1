# Digital Cookbook

listRecipes = []
nLen = len(listRecipes)

#Part A) Adding Recipes/ Editing/ Deleting
def add_recipe():
    name = input("Enter recipe name: ")
    cuisine = input("Enter cuisine: ")
    meal_type = input("Enter meal type: ")
    vegetarian = input("Is it vegetarian? (Yes/No): ")
    ingredients = input("Enter ingredients (comma separated): ").split(", ")
    
    new_recipe = {
        "name": name,
        "cuisine": cuisine,
        "meal type": meal_type,
        "vegetarian": vegetarian,
        "ingredients": ingredients }
    

    listRecipes.append(new_recipe)
    print(f"New recipe added successfully")


def edit_recipe(a_RecipeID, a_Update):
    if 0 <= a_RecipeID < nLen:
        for key, value in a_Update.items():
            listRecipes[a_RecipeID][key] = value
    else: 
        print("Not a vaild ID")

def delete_recipe(a_RecipeID):
    if 0 <= a_RecipeID < nLen:
        del listRecipes[a_RecipeID]
        print(a_RecipeID,"Deleted")
    else:
        print("Not a vaild ID")

def list_all_recipes():
    if not listRecipes:
        print("Recipe not found.")
        return
        
    i = 0
    for recipe in listRecipes:
        print(f"[ID: {i}] Recipe:")
        print(f"  Name: {recipe['name']}")
        print(f"  Cuisine: {recipe['cuisine']}")
        print(f"  Meal Type: {recipe['meal type']}")
        print(f"  Vegetarian: {recipe['vegetarian']}")
        print(f"  Ingredients: {', '.join(recipe['ingredients'])}")
        print("------")
        i += 1
        
# Part B) Ingredient/ Cusine Searching
def find_recipe_by_name():
    recipe_to_find = input("enter the name of the recipe: ")
    for recipe in listRecipes:
        if "name" in recipe:
            if recipe["name"] == recipe_to_find:
                return recipe
    return None

def find_recipe_by_ingredient():
    search = input("Enter ingredient: ")
    for recipe in listRecipes:
        if "ingredients" in recipe:
            for item in recipe["ingredients"]:
                if search.lower() in item.lower():
                    if "name" in recipe:
                        print(f"Found: {recipe['name']}")
                    else:
                        print("Sorry")
                    return
    print(f"No recipes with '{search}' found.")

def find_recipe_by_cuisine(search_cuisine):
    matching_recipes = []
    search = search_cuisine.lower()
    for recipe in listRecipes:
        if "cuisine" in recipe and recipe["cuisine"].lower() == search:
            matching_recipes.append(recipe)
    return matching_recipes

# Part C) Cooking Assistant Features
def view_vegetarian_recipes():
    print("\n== Vegetarian Recipes ==")
    bFound = False
    for recipe in listRecipes:
        if recipe["vegetarian"].lower() == "yes":
            print(f"{recipe['name']}")
            bFound = True
    if bFound == False:
        print("No vegetarian recipes found.")

def group_by_meal_type():
    print("\n== Recipes Grouped By Meal Type ==")
    meal_dict = {}

    for recipe in listRecipes:
        if "meal type" in recipe:
          meal_type = recipe["meal type"]
        else:
          meal_type = "Unknown"

        if meal_type in meal_dict:
            meal_dict[meal_type].append(recipe["name"])
        else:
            meal_dict[meal_type] = [recipe["name"]]
    
    for meal in meal_dict:
      print(f"\n{meal}:")
      for meal in meal_dict:
        print(f"\n{meal}:")
        for name in meal_dict[meal]:
          print(f"  - {name} (You might want to try this!)")
    

# Part D) CLI & File Handling
def user_menu():
    while True:
        print("\n === Digital Cookbook Menu ===")
        print("1. Add Recipe")
        print("2. Edit Recipe")
        print("3. Delete Recipe")
        print("4. List All Recipes")
        print("5. Find by Name")
        print("6. Find by Ingredient")
        print("7. Find by Cuisine")
        print("8. View Vegetarian Recipes")
        print("9. Group by Meal Type")

        print("10. Save Recipes to File")
        print("11. Load Recipes from File")
        print("0. Exit")
            
        choice = input("\nEnter your choice: ")
        handle_choice(choice)

        
def handle_choice(choice):
        if choice == "1": 
            add_recipe()
            
        elif choice == "2": 
            a_RecipeID = int(input("Enter the recipe ID to edit: "))
            a_Update = {
                "name": input("Enter new recipe name: "),
                "cuisine": input("Enter new cuisine: "),
                "meal type": input("Enter new meal type: "),
                "vegetarian": input("Is it vegetarian? (Yes/No): "),
                "ingredients": input("Enter new ingredients (comma separated): ").split(", ")
            }
            edit_recipe(a_RecipeID, a_Update)

        elif choice == "3":
            a_RecipeID = int(input("Enter the recipe ID to delete: "))
            delete_recipe(a_RecipeID)

        elif choice == "4": 
            list_all_recipes()
        
        elif choice == "5": 
           find_recipe_by_name()

        elif choice == "6": 
            find_recipe_by_ingredient()

        elif choice == "7":
            search_cuisine = input("Enter cuisine to search: ")
            find_recipe_by_cuisine(search_cuisine)
        
        elif choice == "8":
            view_vegetarian_recipes()

        elif choice == "9":
            group_by_meal_type()
            
        elif choice == "10":
            save_recipes_to_file()
        
        elif choice == "11":
            load_recipes_from_file()

        elif choice == "0":
            print("Exiting program.")
            exit()
        
        else:
            print("Invalid option, try again.")

def save_recipes_to_file():
    with open("recipes.txt", "w") as f:
        for recipe in listRecipes:
            f.write(f"Name: {recipe['name']}\n")
            f.write(f"Cuisine: {recipe['cuisine']}\n")
            f.write(f"Meal Type: {recipe['meal type']}\n")
            f.write(f"Vegetarian: {recipe['vegetarian']}\n")
            f.write(f"Ingredients: {', '.join(recipe['ingredients'])}\n")
            f.write("\n")
    print("Recipes saved to file.")

def load_recipes_from_file():
    global listRecipes
    listRecipes = []
    
    try:

        with open("recipes.txt", "r") as f:
            while True:
                name = f.readline().strip()
                if not name:
                    break

                cuisine = f.readline().strip()
                meal_type = f.readline().strip()
                vegetarian = f.readline().strip()
                ingredients = f.readline().strip()
                ingredients_list = ingredients.split(", ")

                f.readline()

                recipe = {
                    "name": name,
                    "cuisine": cuisine,
                    "meal type": meal_type,
                    "vegetarian": vegetarian,
                    "ingredients": ingredients_list,
                }
                listRecipes.append(recipe)

        print("Recipes loaded from file.")
    except FileNotFoundError:
        print("Starting a new/ empty cookbook")

# Run app
load_recipes_from_file()
user_menu()
