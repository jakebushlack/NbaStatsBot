import twitterClient
import statToEnglishMapper


def generate_tweet(player_dict, players_of_interest, stats):
    outstring = f'Players in the top ten in {statToEnglishMapper.statsInEnglish[stats[0]]}, {statToEnglishMapper.statsInEnglish[stats[1]]}, {statToEnglishMapper.statsInEnglish[stats[2]]}\n'

    for each_player in players_of_interest:
        outstring += f'{each_player}, {statToEnglishMapper.statsInEnglish[stats[0]]}: {getattr(player_dict[each_player], stats[0])}, {statToEnglishMapper.statsInEnglish[stats[1]]}: {getattr(player_dict[each_player], stats[1])}, {statToEnglishMapper.statsInEnglish[stats[2]]}: {getattr(player_dict[each_player], stats[2])}\n'

    print(outstring)
    # twitterClient.client.create_tweet(text=outstring)
