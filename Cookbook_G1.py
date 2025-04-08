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


