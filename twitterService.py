import twitterClient

response = twitterClient.client.create_tweet(text='we back')


def generateTweet(players, stats):
    print(f'Players in the top ten in {stats[0]}, {stats[1]}, {stats[2]}')
    for player in players:
        print(f'{player_name}: {stats_val[0]}, {stats_val[1]}, {stats_val[2]}')
    return 0
