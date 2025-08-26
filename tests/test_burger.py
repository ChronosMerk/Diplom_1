from praktikum.burger import Burger, Bun
from data import ModelBurger

class TestBurger:
    def test_set_buns_correct(self):
        burger = Burger()
        bun = Bun(ModelBurger.NAME_BUN, ModelBurger.PRICE_BUN)

        burger.set_buns(bun)