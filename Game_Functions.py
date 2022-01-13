__author__ = "7723744, Arshid, 7724048, Davoodi"


def create_card_list(number_of_cards: int) -> [(int, str)]:

    list_cards = []
    for i in range(1, number_of_cards + 1):
        for j in ["grün", "gelb", "blau", "rot"]:
            list_cards.append((i, j))
    return list_cards


def bigger_card(card_one: (int, str), card_two: (int, str), trumpf: str) -> int:

    if card_one[1] == trumpf:
        # card one is trumpf
        if card_two[1] == trumpf:
            # card two is trumpf, check bigger number of both cards
            if card_one[0] > card_two[0]:
                return 2
            elif card_one[0] == card_two[0]:
                return 1
            else:
                return 0
        else:
            # card two is no trumpf -> card one is bigger
            return 2
    elif card_two[1] == trumpf:
        # card one no trumpf & card two is trumpf -> card two is bigger
        return 0
    else:
        # no trumpf card - only value
        if card_one[0] > card_two[0]:
            return 2
        elif card_one[0] == card_two[0]:
            return 1
        else:
            return 0


def deal_cards(list_cards: [(int, str)], players: int, number_of_cards: int) -> [[(int, str)]]:

    return_list = []
    for i in range(players):
        return_list.append(list_cards[i * number_of_cards:i * number_of_cards + number_of_cards])
    return return_list


if __name__ == '__main__':
    pass


def rounds(card_amount, players):   # Return amount of Rounds that will be played
    rounds_amount = (card_amount - 1)//players
    return rounds_amount


def gametable(game_table, trump):  # Compare cards on table and return the biggest one
    compare = []
    for i in game_table:
        if trump == i[1]:
            compare.append(i)

    if bool(compare):
        return max(compare)
    else:
        return max(game_table)


def checkifduplicates(listofelems):  # Check if given list contains any duplicates
    if max(listofelems) > 1:
        return False
    else:
        return True
