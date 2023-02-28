from fastapi import FastAPI, HTTPException

from recipes.db import recipes_collection
from recipes.models import Recipe

app = FastAPI()


@app.get("/", response_model=list[Recipe])
def get_all_recipes():
    cursor = recipes_collection.find()
    recipes = [r for r in cursor]
    return recipes


@app.post("/")
def create_recipe(recipe: Recipe):
    recipes_collection.insert_one(recipe.dict())

    return {"message": f"Recipe {recipe.name} created."}


@app.get("/{name}", response_model=Recipe)
def get_recipe(name: str):
    recipe = recipes_collection.find_one({"name": name})
    if recipe is None:
        raise HTTPException(status_code=404, detail=f"Recipe {name} not found.")
    return recipe


@app.delete("/{name}")
def delete_recipe(name: str):
    recipes_collection.delete_one({"name": name})
    return {"message": f"Recipe {name} deleted."}
