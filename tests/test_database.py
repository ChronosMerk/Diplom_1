from praktikum.database import Database

class TestDatabase:
    def test_available_buns_correct_returns_non_empty_list(self):
        database = Database()
        buns = database.available_buns()

        assert len(buns) > 0
        assert len(buns) == 3

    def test_available_ingredients_correct_returns_non_empty_list(self):
        database = Database()
        ingredients = database.available_ingredients()

        assert len(ingredients) > 0
        assert len(ingredients) == 6