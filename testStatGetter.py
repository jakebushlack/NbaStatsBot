from unittest import TestCase
import statGetter
from config import test_content
from dataService import get_player_data

test_file = test_content['test_table']
player_dict = get_player_data('test_table', {})


class StatGetterTest(TestCase):
    def test_remove_default_attributes_removes_attributes(self):
        print(dir(player_dict))
        print(player_dict)
        print(player_dict[list(player_dict.keys())[0]])

        attr_count_before = len(dir(player_dict))
        attr_count_after = len(statGetter.remove_default_attributes(player_dict[list(player_dict.keys())[0]]))

        self.assertLess(attr_count_after, attr_count_before)

    def test_get_category_top_ten_gets_top_ten(self):
        print(dir(statGetter.remove_default_attributes(player_dict[list(player_dict.keys())[0]])))

        top_ten_points = statGetter.get_category_top_ten('pts', player_dict)
        print(type(top_ten_points))
        print(len(top_ten_points))
        print(top_ten_points)

    def test_get_category_bottom_ten_gets_bottom_ten(self):
        statGetter.get_category_bottom_ten()

    def test_find_top_tens_finds_top_ten(self):
        statGetter.find_top_tens()

    def test_randomize_attribute_gets_random_attributes(self):
        statGetter.randomize_attribute()
