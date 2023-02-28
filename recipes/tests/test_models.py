from recipes.models import Ingredient, Quantity, QuantityType, Recipe, Category


def test_create_recipe():
    ingredient_1 = Ingredient(
        name="jajka", quantity=Quantity(value=4, type=QuantityType.count)
    )
    ingredient_2 = Ingredient(
        name="maslo", quantity=Quantity(value=1, type=QuantityType.spoon)
    )
    ingredient_3 = Ingredient(
        name="parowki", quantity=Quantity(value=3, type=QuantityType.count)
    )
    ingredient_4 = Ingredient(
        name="chleb", quantity=Quantity(value=3, type=QuantityType.count)
    )
    recipe = Recipe(
        name="jajecznica",
        category=Category.breakfast,
        ingredients=[ingredient_1, ingredient_2, ingredient_3, ingredient_4],
    )

    assert recipe.dict()["category"] == 1
    assert ingredient_1.dict()["quantity"]["type"] == 4
