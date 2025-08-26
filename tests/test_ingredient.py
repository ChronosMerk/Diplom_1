import pytest
from data import ModelIngredient
from praktikum.ingredient import Ingredient

class TestIngregient:
    @pytest.mark.parametrize('input_data', [ModelIngredient.INGREDIENT_SAUCE, ModelIngredient.INGREDIENT_FILLING])
    def test_get_price_correct_returns_price(self, input_data):
        type, name, price = input_data
        ingredient = Ingredient(type, name, price)

        assert ingredient.get_price() == price

    @pytest.mark.parametrize('input_data', [ModelIngredient.INGREDIENT_SAUCE, ModelIngredient.INGREDIENT_FILLING])
    def test_get_name_correct_returns_name(self, input_data):
        type, name, price = input_data
        ingredient = Ingredient(type, name, price)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize('input_data',[ModelIngredient.INGREDIENT_SAUCE, ModelIngredient.INGREDIENT_FILLING])
    def test_get_type_correct_returns_type(self, input_data):
        type, name, price = input_data
        ingredient = Ingredient(type, name, price)

        assert ingredient.get_type() == type