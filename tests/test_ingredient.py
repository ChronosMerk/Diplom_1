import pytest
from data import ModelBurger
from praktikum.ingredient import Ingredient

@pytest.mark.parametrize('type_, name, price',
    [
        (ModelBurger.INGREDIENT_SAUCE, ModelBurger.NAME_BUN, ModelBurger.PRICE_BUN),
        (ModelBurger.INGREDIENT_FILLING, ModelBurger.NAME_BUN, ModelBurger.PRICE_BUN),
    ]
)
class TestIngregient:
    def test_get_price_correct_returns_price(self, type_, name, price):
        ingredient = Ingredient(type_, name, price)

        assert ingredient.get_price() == price

    def test_get_name_correct_returns_name(self, type_, name, price):
        ingredient = Ingredient(type_, name, price)

        assert ingredient.get_name() == name

    def test_get_type_correct_returns_type(self, type_, name, price):
        ingredient = Ingredient(type_, name, price)

        assert ingredient.get_type() == type_