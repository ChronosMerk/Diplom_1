import pytest
from praktikum.burger import Burger
from unittest.mock import Mock
from data import ModelBurger

@pytest.fixture
def empty_burger():
    burger = Burger()
    return burger

@pytest.fixture
def mock_burger_methods():
    mock_bun = Mock()
    mock_bun.get_name.return_value = ModelBurger.NAME_BUN
    mock_bun.get_price.return_value = ModelBurger.PRICE_BUN

    mock_ingredient = Mock()
    mock_ingredient.get_price.return_value = ModelBurger.PRICE_INGREDIENTS
    mock_ingredient.get_name.return_value = ModelBurger.INGREDIENT_NAME
    mock_ingredient.get_type.return_value = ModelBurger.INGREDIENT_SAUCE
    return mock_bun, mock_ingredient
