import logging

import statToEnglishMapper
import twitterClient


def generate_tweet(player_dict, players_of_interest, stats):
    logging.debug('Building Tweet content')

    outstring = f'Players in the top ten in ' \
                f'{statToEnglishMapper.statsInEnglish[stats[0]]}, ' \
                f'{statToEnglishMapper.statsInEnglish[stats[1]]}, ' \
                f'{statToEnglishMapper.statsInEnglish[stats[2]]}\n'

    for each_player in players_of_interest:
        outstring += f'{each_player}, ' \
                     f'{statToEnglishMapper.statsInEnglish[stats[0]]}: {getattr(player_dict[each_player], stats[0])}, '\
                     f'{statToEnglishMapper.statsInEnglish[stats[1]]}: {getattr(player_dict[each_player], stats[1])}, '\
                     f'{statToEnglishMapper.statsInEnglish[stats[2]]}: {getattr(player_dict[each_player], stats[2])}\n'

    print(outstring)
    logging.debug('Tweet built')

    twitterClient.client.create_tweet(text=outstring)
    logging.debug('Tweet sent')
