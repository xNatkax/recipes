from enum import Enum

from pydantic import BaseModel


class QuantityType(Enum):
    mililiters = 1
    cup = 2
    grams = 3
    count = 4
    spoon = 5


class Quantity(BaseModel):
    value: int
    type: QuantityType

    class Config:
        use_enum_values = True


class Ingredient(BaseModel):
    name: str
    quantity: Quantity


class Category(Enum):
    breakfast = 1
    dinner = 2
    supper = 3
    snack = 4


class Recipe(BaseModel):
    name: str
    category: Category
    ingredients: list[Ingredient]

    class Config:
        use_enum_values = True


if __name__ == "__main__":
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
    from rich import print
    from recipes.db import recipes_collection

    recipes_collection.insert_one(recipe.dict())

    cursor = recipes_collection.find({"category": Category.breakfast.value})

    recipes_collection.delete_many({"name": "jajecznica"})

    print(recipes_collection.find_one({"name": "jajecznica"}))
