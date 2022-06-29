import logging

from random import randint


class Player:
    stats = []

    def __init__(self, _attr, _val):
        setattr(self, _attr, _val)

    def adding_new_attr(self, _attr, _val):
        setattr(self, _attr, _val)

    def get_custom_stat_attributes(self):
        all_player_attributes = list(dir(self))
        custom_player_attributes = []
        stats_that_arent_stats = ['',
                                  'player',
                                  'stats',
                                  'team_id',
                                  'pos',
                                  'get_custom_stat_attributes',
                                  'get_three_random_attributes',
                                  'adding_new_attr']

        logging.debug('Trimming default attributes from Player object')
        for thing in all_player_attributes:
            if not thing.endswith("__") and thing not in stats_that_arent_stats:
                custom_player_attributes.append(thing)

        return custom_player_attributes

    def get_three_random_attributes(self):
        logging.debug('Randomizing 3 stat categories')

        selected_attributes = []
        custom_stat_attributes = self.get_custom_stat_attributes()

        while len(selected_attributes) < 3:
            rand_index = randint(0, len(custom_stat_attributes) - 1)

            if custom_stat_attributes[rand_index] not in selected_attributes:
                selected_attributes.append(custom_stat_attributes[rand_index])

        return selected_attributes
