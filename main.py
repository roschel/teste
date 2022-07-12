from abstractions import Impulsive, Demanding, Aleatory, Prudent
from model.board import Board
from model.player import Player


def check_if_the_game_is_over(players):
    result = []
    for player in players:
        if player.playing:
            result.append({"player": player.id, "balance": player.balance})

    return result


def start_game():
    player_1 = Player(id=1, behavior=Impulsive)
    player_2 = Player(id=2, behavior=Demanding)
    player_3 = Player(id=3, behavior=Prudent)
    player_4 = Player(id=4, behavior=Aleatory)

    round = 1
    while round <= 1000:
        result = check_if_the_game_is_over([player_1, player_2, player_3, player_4])
        if len(result) == 1 or not result:
            break
        dices = player_1.roll_dices()
        player_1.buy_or_pay(Board(player_1.currently_position).play_round(dices=dices))
        player_1.currently_position = dices

        dices = player_2.roll_dices()
        player_2.buy_or_pay(Board(player_2.currently_position).play_round(dices=dices))
        player_2.currently_position = dices

        dices = player_3.roll_dices()
        player_3.buy_or_pay(Board(player_3.currently_position).play_round(dices=dices))
        player_3.currently_position = dices

        dices = player_4.roll_dices()
        player_4.buy_or_pay(Board(player_4.currently_position).play_round(dices=dices))
        player_4.currently_position = dices

        print(f'Round - {round}')
        round += 1
        print(f'Player - {player_1}')
        print(f'Player - {player_2}')
        print(f'Player - {player_3}')
        print(f'Player - {player_4}')

    return round, player_1, player_2, player_3, player_4


if __name__ == '__main__':
    round_by_time_out = 0
    total_rounds = 0
    player_1_win = 0
    player_2_win = 0
    player_3_win = 0
    player_4_win = 0
    for i in range(1, 301):
        rounds, player_1, player_2, player_3, player_4 = start_game()
        result = check_if_the_game_is_over([player_1, player_2, player_3, player_4])
        if rounds >= 1000:
            round_by_time_out += 1
        total_rounds += rounds

        if result:
            if result[0]['player'] == 1:
                player_1_win += 1
            if result[0]['player'] == 2:
                player_2_win += 1
            if result[0]['player'] == 3:
                player_3_win += 1
            if result[0]['player'] == 4:
                player_4_win += 1

    average_rounds = total_rounds / 300

    print('By time out', round_by_time_out)
    print('average_by_round', average_rounds)
    print('impulsive %', round((player_1_win / 300) * 100, 2))
    print('demanding %', round((player_2_win / 300) * 100, 2))
    print('prudent %', round((player_3_win / 300) * 100, 2))
    print('aleatory %', round((player_4_win / 300) * 100, 2))
