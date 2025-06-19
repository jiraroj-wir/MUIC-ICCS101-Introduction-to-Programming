# Assignment 6, Task 5
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.3 hrs
# Use of AI: NO
# AI usage details: <DETAILS>


### Your code start here ######
def mealCal(meal: list[str], recipes: list[str], db: list[str]) -> float:
    """
    db = ["Cabbage:4,2,0", "Carrot:9,1,5", "Fatty Pork:431,1,5",
    "Pineapple:7,1,0", "Steak Meat:5,20,10", "Rabbit Meat:7,2,20"]
    """
    db_map = {}
    for macro in db:
        [head, tail] = macro.split(":")
        [car, pro, fat] = tail.split(",")
        db_map[head] = (int(car), int(pro), int(fat))

    """
    recipes = ["Pork Stew:Cabbage*5,Carrot*1,Fatty Pork*10",
    "Green Salad1:Cabbage*10,Carrot*2,Pineapple*5",
    "T-Bone:Carrot*2,Steak Meat*1"]
    """
    recipes_map = {}
    for recipe in recipes:
        [head, tail] = recipe.split(":")
        ingredients = tail.split(",")
        recipes_map[head] = []
        for ingredient in ingredients:
            [ing, amount] = ingredient.split("*")
            recipes_map[head].append((ing, int(amount)))

    total_calories = 0
    for dish in meal:
        for ingredient, amount in recipes_map[dish]:
            car, pro, fat = db_map[ingredient]
            total_calories += amount * ((4 * car) + (4 * pro) + (9 * fat))

    return total_calories


assert (
    abs(
        mealCal(
            ["T-Bone", "T-Bone", "Green Salad1"],
            [
                "Pork Stew:Cabbage*5,Carrot*1,Fatty Pork*10",
                "Green Salad1:Cabbage*10,Carrot*2,Pineapple*5",
                "T-Bone:Carrot*2,Steak Meat*1",
            ],
            [
                "Cabbage:4,2,0",
                "Carrot:9,1,5",
                "Fatty Pork:431,1,5",
                "Pineapple:7,1,0",
                "Steak Meat:5,20,10",
                "Rabbit Meat:7,2,20",
            ],
        )
        - 1290.0
    )
    < 1e-5
)
