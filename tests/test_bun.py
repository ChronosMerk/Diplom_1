from praktikum.bun import Bun
from data import ModelBurger

class TestBun:
    def test_get_name_correct_returns_name(self):
        bun = Bun(ModelBurger.NAME_BUN, ModelBurger.PRICE_BUN)

        assert bun.get_name() == ModelBurger.NAME_BUN

    def test_get_price_correct_returns_price(self):
        bun = Bun(ModelBurger.NAME_BUN, ModelBurger.PRICE_BUN)

        assert bun.get_price() == ModelBurger.PRICE_BUN