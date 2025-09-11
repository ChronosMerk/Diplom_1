from data import ModelBurger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestBurger:
    def test_set_buns_correct_data_bun_set_successfully(self, empty_burger, mock_burger_methods):
        empty_burger.set_buns(mock_burger_methods[0])

        assert empty_burger.bun.get_name() == ModelBurger.NAME_BUN
        assert empty_burger.bun
        assert empty_burger.bun.get_price() == ModelBurger.PRICE_BUN

    def test_add_ingredient_success(self,empty_burger, mock_burger_methods):
        empty_burger.add_ingredient(mock_burger_methods[1])

        assert len(empty_burger.ingredients) != 0
        assert empty_burger.ingredients[0].get_type() == ModelBurger.INGREDIENT_SAUCE
        assert empty_burger.ingredients[0].get_price() == ModelBurger.PRICE_INGREDIENTS
        assert empty_burger.ingredients[0].get_name() == ModelBurger.INGREDIENT_NAME

    def test_remove_ingredient_success(self, empty_burger):
        ingredient = Ingredient(ModelBurger.INGREDIENT_FILLING, ModelBurger.INGREDIENT_NAME, ModelBurger.PRICE_INGREDIENTS)
        empty_burger.add_ingredient(ingredient)
        empty_burger.remove_ingredient(0)

        assert len(empty_burger.ingredients) == 0

    def test_move_ingredient_success(self, empty_burger):
        empty_burger.add_ingredient(Ingredient(ModelBurger.INGREDIENT_FILLING, ModelBurger.INGREDIENT_NAME, ModelBurger.PRICE_INGREDIENTS))
        empty_burger.add_ingredient(Ingredient(ModelBurger.INGREDIENT_SAUCE, ModelBurger.INGREDIENT_NAME, ModelBurger.PRICE_INGREDIENTS))
        ingrediens1 = empty_burger.ingredients[0]
        ingrediens2 = empty_burger.ingredients[1]

        empty_burger.move_ingredient(0, 1)

        assert empty_burger.ingredients[0] == ingrediens2
        assert empty_burger.ingredients[1] == ingrediens1

    def test_get_price_returns_sum(self, empty_burger):
        price = ModelBurger.PRICE_BUN * 2 + ModelBurger.PRICE_INGREDIENTS
        bun = Bun(ModelBurger.NAME_BUN, ModelBurger.PRICE_BUN)
        empty_burger.set_buns(bun)
        empty_burger.add_ingredient(Ingredient(ModelBurger.INGREDIENT_FILLING, ModelBurger.INGREDIENT_NAME, ModelBurger.PRICE_INGREDIENTS))

        assert empty_burger.get_price() == price

    def test_get_receipt_success(self,empty_burger, mock_burger_methods):
        empty_burger.set_buns(mock_burger_methods[0])
        empty_burger.set_buns(mock_burger_methods[0])
        empty_burger.add_ingredient(mock_burger_methods[1])
        receipt = empty_burger.get_receipt()

        assert receipt == '(==== Popeyes ====)\n= sauce Lettuce =\n(==== Popeyes ====)\n\nPrice: 300'