__author__ = "7723744, Arshid, 7724048, Davoodi"


import random
from Game_Functions import create_card_list
from Game_Functions import deal_cards
from Game_Functions import gametable
from Game_Functions import rounds
from Game_Functions import checkifduplicates

# This is the main module of the game where it's designed and played.

players = int(input("How many players? "))      # Amount of players
while True:
    if players > 5 or players < 2:
        print("Invalid input. Please enter a number between 2 and 5")
        players = int(input("How many players? "))
    else:
        break
players_bot_inputs = ["yes", "y", "no", "n"]
players_bot = input("Do you want a bot player ? (y/n)")  # Bot player
while True:
    if players_bot in players_bot_inputs:
        break
    else:
        print("Invalid input, please type either yes (y) or no (n)")
        players_bot = input("Do you want a bot player ? (y/n)")
if players_bot == "y" or players_bot == "yes":
    players_bot = True
    players_bot_difficulty = input("select difficulty of bot:"   # Difficulty of bot player
                                   "1- Easy 2- Hard ")
else:
    players_bot = False

win = input("How do you want to win?"                   # Win condition
            "1- Most Rounds won 2- Most mini Rounds won (1/2)")

while True:
    if win.isdigit():
        win = int(win)
        if win > 2 or win < 1:
            print("Invalid input, please type either 1 or 2")
            win = input("How do you want to win? 1- Most Rounds won 2- Most mini Rounds won (1/2)")
        else:
            break
    else:
        print("Invalid input, please type an integer number (Either 1 or 2) ")
        win = input("How do you want to win? 1- Most Rounds won 2- Most mini Rounds won (1/2)")


limit = int(input("Enter the value of cards you want as a maximum"  # determine the size of card deck
                  "(from 5 to 15): "))

while True:
    if limit > 15 or limit < 5:
        print("Invalid input. Please enter a number between 1 and 15")
        limit = int(input("Enter the value of cards you want as a maximum"
                          "(from 5 to 15): "))
    else:
        break

card_list_all = create_card_list(limit)  # Create card deck
random.shuffle(card_list_all)
Round = rounds(len(card_list_all), players)  # Determine Rounds

trump = card_list_all[0]
trump_card = trump[1]

p = {}  # Dictionary created to keep track of players and their cards
for i in range(players):
    p['p'+str(i)] = []

# Records for score in mini Rounds
p0_trick = 0
p1_trick = 0
p2_trick = 0
p3_trick = 0
p4_trick = 0

# Records for score in Rounds
p0 = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0


game_table = []

"""" here begins the main game where everything is put together and the game is played
    until both players are out of cards"""


print(" ")
print("----- ", Round, " Rounds Will be played -----")
print(" ")
miniround_number = 1
round_number = 1
while True:
    while round_number <= Round:
        trump = card_list_all[0]
        trump_card = trump[1]
        cards = deal_cards(card_list_all, players, round_number)

        for element in cards:
            for element_1 in element:
                if element_1 in card_list_all:
                    card_list_all.remove(element_1)

        if "p0" in p:
            p["p0"] = cards[0]
        if "p1" in p:
            p["p1"] = cards[1]
        if "p2" in p:
            p["p2"] = cards[2]
        if "p3" in p:
            p["p3"] = cards[3]
        if "p4" in p:
            p["p4"] = cards[4]

        if players_bot is False:
            while bool(p["p0"]):
                print("----- Round ", round_number, " -----")
                print("----- Mini Round", miniround_number, " -----")
                for k in sorted(p.items()):
                    trump = card_list_all[0]
                    trump_card = trump[1]
                    print("the Trump card is: ", trump_card)

                    if k[0] == "p0":
                        print("PLAYER 1")
                        print("cards of player 1: ", p["p0"])
                        select = int(input("""please select a card
                                            (input a number from 1 to """
                                           + str(len(p["p0"])) + "): "))
                        select_1 = select
                        game_table.append(p["p0"][select - 1])
                        print("cards on the table: ", game_table)
                        print(" ")

                    if k[0] == "p1":
                        print("PLAYER 2")
                        print("cards of player 2: ", p["p1"])
                        select = int(input("please select a card (input a number from 1 to "
                                           + str(len(p["p1"])) + "): "))
                        select_2 = select
                        game_table.append(p["p1"][select - 1])
                        print("cards on the table: ", game_table)
                        print(" ")

                    if k[0] == "p2":
                        print("PLAYER 3")
                        print("cards of player 3", p["p2"])
                        select = int(input("please select a card (input a number from 1 to "
                                           + str(len(p["p2"])) + "): "))
                        select_3 = select
                        game_table.append(p["p2"][select - 1])
                        print("cards on the table: ", game_table)
                        print(" ")

                    if k[0] == "p3":
                        print("PLAYER 4")
                        print("cards of player 4", p["p3"])
                        select = int(input("please select a card (input a number from 1 to "
                                           + str(len(p["p3"])) + "): "))
                        select_4 = select
                        game_table.append(p["p3"][select - 1])
                        print("cards on the table: ", game_table)
                        print(" ")

                    if k[0] == "p4":
                        print("PLAYER 5")
                        print("cards of player 2: ", p["p4"])
                        select = int(input("please select a card (input a number from 1 to "
                                           + str(len(p["p4"])) + "): "))
                        select_5 = select
                        game_table.append(p["p4"][select - 1])
                        print("cards on the table: ", game_table)
                        print(" ")

                big = gametable(game_table, trump_card)
                if big in p["p0"]:
                    print("The bigger card belongs to player 1")
                    p0_trick = p0_trick + 1
                    game_table = []
                elif big in p["p1"]:
                    p1_trick = p1_trick + 1
                    print("The bigger card belongs to player 2")
                    game_table = []
                elif big in p["p2"]:
                    p2_trick = p2_trick + 1
                    print("The bigger card belongs to player 3")
                    game_table = []
                elif big in p["p3"]:
                    p3_trick = p3_trick + 1
                    print("The bigger card belongs to player 4")
                    game_table = []
                elif big in p["p4"]:
                    p4_trick = p4_trick + 1
                    print("The bigger card belongs to player 5")
                    game_table = []
                else:
                    p0_trick = p0_trick
                    p1_trick = p1_trick
                    p2_trick = p2_trick
                    p3_trick = p3_trick
                    p4_trick = p4_trick
                    game_table = []

                for i in sorted(p.items()):

                    if i[0] == "p0":
                        p["p0"].pop(select_1 - 1)

                    if i[0] == "p1":
                        p["p1"].pop(select_2 - 1)

                    if i[0] == "p2":
                        p["p2"].pop(select_3 - 1)

                    if i[0] == "p3":
                        p["p3"].pop(select_4 - 1)
                    if i[0] == "p4":
                        p["p4"].pop(select_5 - 1)
                points = [p0_trick, p1_trick, p2_trick, p3_trick, p4_trick]
                miniround_number = miniround_number + 1
                print(" ")
                print("current mini rounds points are",
                      "for player 1: ",
                      p0_trick, "for player 2: ", p1_trick,
                      "for player 3: ", p2_trick, "for player 4: ", p3_trick, "for player 5: ", p4_trick)
                print(" ")
                print(" ")

        if players_bot is True:
            if players_bot_difficulty == "easy" or "1":
                while bool(p["p0"]):
                    print("----- Round ", round_number, " -----")
                    print("----- Mini Round", miniround_number, " -----")
                    for k in sorted(p.items()):
                        trump = card_list_all[0]
                        trump_card = trump[1]
                        print("the Trump card is: ", trump_card)

                        if k[0] == "p0":
                            print("PLAYER 1")
                            print("cards of player 1: ", p["p0"])
                            select = int(input("please select a card (input a number from 1 to "
                                               + str(len(p["p0"])) + "): "))
                            select_1 = select
                            game_table.append(p["p0"][select - 1])
                            print("cards on the table: ", game_table)
                            print(" ")

                        if k[0] == "p1":
                            print("PLAYER 2 (Bot)")
                            print("cards of player 2: ", p["p1"])
                            select = random.randint(1, len(p["p1"]))
                            select_2 = select
                            game_table.append(p["p1"][select - 1])
                            print("cards on the table: ", game_table)
                            print(" ")

                        if k[0] == "p2":
                            print("PLAYER 3")
                            print("cards of player 3", p["p2"])
                            select = int(input("please select a card (input a number from 1 to " +
                                               str(len(p["p2"])) + "): "))
                            select_3 = select
                            game_table.append(p["p2"][select - 1])
                            print("cards on the table: ", game_table)
                            print(" ")

                        if k[0] == "p3":
                            print("PLAYER 4")
                            print("cards of player 4", p["p3"])
                            select = int(input("please select a card (input a number from 1 to " +
                                               str(len(p["p3"])) + "): "))
                            select_4 = select
                            game_table.append(p["p3"][select - 1])
                            print("cards on the table: ", game_table)
                            print(" ")

                        if k[0] == "p4":
                            print("PLAYER 5")
                            print("cards of player 2: ", p["p4"])
                            select = int(input("please select a card (input a number from 1 to "
                                               + str(len(p["p4"])) + "): "))
                            select_5 = select
                            game_table.append(p["p4"][select - 1])
                            print("cards on the table: ", game_table)
                            print(" ")

                    big = gametable(game_table, trump_card)
                    if big in p["p0"]:
                        print("The bigger card belongs to player 1")
                        p0_trick = p0_trick + 1
                        game_table = []
                    elif big in p["p1"]:
                        p1_trick = p1_trick + 1
                        print("The bigger card belongs to player 2")
                        game_table = []
                    elif big in p["p2"]:
                        p2_trick = p2_trick + 1
                        print("The bigger card belongs to player 3")
                        game_table = []
                    elif big in p["p3"]:
                        p3_trick = p3_trick + 1
                        print("The bigger card belongs to player 4")
                        game_table = []
                    elif big in p["p4"]:
                        p4_trick = p4_trick + 1
                        print("The bigger card belongs to player 5")
                        game_table = []
                    else:
                        p0_trick = p0_trick
                        p1_trick = p1_trick
                        p2_trick = p2_trick
                        p3_trick = p3_trick
                        p4_trick = p4_trick
                        game_table = []

                    for i in sorted(p.items()):

                        if i[0] == "p0":
                            p["p0"].pop(select_1 - 1)

                        if i[0] == "p1":
                            p["p1"].pop(select_2 - 1)

                        if i[0] == "p2":
                            p["p2"].pop(select_3 - 1)

                        if i[0] == "p3":
                            p["p3"].pop(select_4 - 1)

                        if i[0] == "p4":
                            p["p4"].pop(select_5 - 1)

                    points = [p0_trick, p1_trick, p2_trick, p3_trick]
                    miniround_number = miniround_number + 1
                    print(" ")
                    print("current points are",
                          "for player 1: ",
                          p0_trick, "for player 2: ", p1_trick,
                          "for player 3: ", p2_trick, "for player 4: ", p3_trick)
                    print(" ")
                    print(" ")
            elif players_bot_difficulty == "hard" or "2":
                while bool(p["p0"]):
                    print("----- Round ", round_number, " -----")
                    print("----- Mini Round", miniround_number, " -----")
                    for k in sorted(p.items()):
                        trump = card_list_all[0]
                        trump_card = trump[1]
                        print("the Trump card is: ", trump_card)

                        if k[0] == "p0":
                            print("PLAYER 1")
                            print("cards of player 1: ", p["p0"])
                            select = int(input("please select a card (input a number from 1 to "
                                               + str(len(p["p0"])) + "): "))
                            select_1 = select
                            game_table.append(p["p0"][select - 1])
                            print("cards on the table: ", game_table)
                            print(" ")
                            card_1 = game_table[0]

                        if k[0] == "p1":
                            print("PLAYER 2 (Bot)")
                            print("cards of player 2: ", p["p1"])
                            if bool(game_table):
                                trump_card_exist = False
                                trump_card_bot = []
                                bigger_card_table = []
                                for i in game_table:
                                    if i[1] == trump_card:
                                        bigger_card_table.append(i)
                                for i in p["p1"]:
                                    if i[1] == trump_card:
                                        trump_card_exist = True
                                        trump_card_bot.append(i)
                                if bool(bigger_card_table):
                                    if trump_card_exist is True:
                                        if min(trump_card_bot) > max(bigger_card_table):
                                            select_index = min(
                                                a for a in p["p1"] if
                                                a >= max(bigger_card_table) and a[1] == trump_card)
                                        elif min(trump_card_bot) <= max(bigger_card_table):
                                            select_index = min(
                                                a for a in p["p1"] if a <= max(bigger_card_table))
                                    else:
                                        select_index = min(a for a in p["p1"])

                                else:
                                    if trump_card_exist is True:
                                        select_index = min(
                                            a for a in p["p1"] if a[1] == trump_card)
                                    else:
                                        card_bigger = [b for b in p["p1"] if b >= max(game_table)]
                                        if bool(card_bigger):
                                            select_index = min(
                                                a for a in p["p1"] if a >= max(game_table))
                                        else:
                                            select_index = min(
                                                a for a in p["p1"])

                            else:
                                select_index = min(a for a in p["p1"])

                            select = p["p1"].index(select_index)
                            select_2 = select
                            game_table.append(p["p1"][select])

                            print("cards on the table: ", game_table)
                            print(" ")

                        if k[0] == "p2":
                            print("PLAYER 3")
                            print("cards of player 3", p["p2"])
                            select = int(input("please select a card"
                                               "(input a number from 1 to " +
                                               str(len(p["p3"])) + "): "))
                            select_3 = select
                            game_table.append(p["p2"][select - 1])

                            print("cards on the table: ", game_table)
                            print(" ")

                        if k[0] == "p3":
                            print("PLAYER 4")
                            print("cards of player 4", p["p3"])
                            select = int(input("""please select a card
                                               (input a number from 1 to """ +
                                               str(len(p["p3"])) + "): "))
                            select_4 = select
                            game_table.append(p["p3"][select - 1])
                            print("cards on the table: ", game_table)
                            print(" ")

                        if k[0] == "p4":
                            print("PLAYER 5")
                            print("cards of player 2: ", p["p4"])
                            select = int(input("""please select a card
                                        (input a number from 1 to """
                                               + str(len(p["p4"])) + "):"))
                            select_5 = select
                            game_table.append(p["p4"][select - 1])
                            print("cards on the table: ", game_table)
                            print(" ")

                    big = gametable(game_table, trump_card)
                    if big in p["p0"]:
                        print("The bigger card belongs to player 1")
                        p0_trick = p0_trick + 1
                        game_table = []
                    elif big in p["p1"]:
                        p1_trick = p1_trick + 1
                        print("The bigger card belongs to player 2")
                        game_table = []
                    elif big in p["p2"]:
                        p2_trick = p2_trick + 1
                        print("The bigger card belongs to player 3")
                        game_table = []
                    elif big in p["p3"]:
                        p3_trick = p3_trick + 1
                        print("The bigger card belongs to player 4")
                        game_table = []
                    else:
                        p0_trick = p0_trick
                        p1_trick = p1_trick
                        p2_trick = p2_trick
                        p3_trick = p3_trick
                        game_table = []

                    for i in sorted(p.items()):

                        if i[0] == "p0":
                            p["p0"].pop(select_1 - 1)

                        if i[0] == "p1":
                            p["p1"].pop(select_2)

                        if i[0] == "p2":
                            p["p2"].pop(select_3 - 1)

                        if i[0] == "p3":
                            p["p3"].pop(select_4 - 1)

                        if i[0] == "p4":
                            p["p4"].pop(select_5 - 1)

                    points = [p0_trick, p1_trick, p2_trick, p3_trick, p4_trick]
                    miniround_number = miniround_number + 1
                    print(" ")
                    print("current points are", "for player 1: ", p0_trick,
                          "for player 2: ", p1_trick,
                          "for player 3: ", p2_trick,
                          "for player 4: ", p3_trick,
                          "for player 5: ", p4_trick)
                    print(" ")
                    print(" ")

        miniround_number = 1
        round_number = round_number + 1

        card_list_all = create_card_list(limit)
        random.shuffle(card_list_all)
        if max(points) == p0_trick:        # Determine who won the Round based on Tricks won
            p0 = p0 + 1
        elif max(points) == p1_trick:
            p1 = p1 + 1
        elif max(points) == p2_trick:
            p2 = p2 + 1
        elif max(points) == p3_trick:
            p3 = p3 + 1
        else:
            if max(points) == p4_trick:
                p4 = p4 + 1
        points_rounds = [p0, p1, p2, p3, p4]
        print("current Rounds points are", "for player 1: ",
              p0, "for player 2: ", p1,
              "for player 3: ", p2, "for player 4: ", p3,
              "for player 5: ", p4)

    win_points = []

    if win == 1:   # Determine who won based on win condition
        for i in points_rounds:
            if i != 0:
                win_points.append(i)

        if checkifduplicates(win_points):
            print("Final Rounds points are", "for player 1: ",
                  p0, "for player 2: ", p1,
                  "for player 3: ", p2,
                  "for player 4: ", p3, "for player 5: ", p4)
            print("It's a Tie!")

        else:
            print("Final Rounds points are",
                  "for player 1: ", p0,
                  "for player 2: ", p1,
                  "for player 3: ", p2, "for player 4: ",
                  p3, "for player 5: ", p4)

            if max(points_rounds) == p0:
                print("player 1 has won ")

            elif max(points_rounds) == p1:
                print("player 2 has won ")

            elif max(points_rounds) == p2:
                print("player 3 has won ")

            elif max(points_rounds) == p3:
                print("Player 4 has won")

            else:
                if max(points_rounds) == p4:
                    print("Player 5 has won")

    else:
        if win == 2:
            for i in points_rounds:
                if i != 0:
                    win_points.append(i)

            if checkifduplicates(win_points):
                print("Final mini rounds points are", "for player 1: ",
                      p0_trick, "for player 2: ", p1_trick,
                      "for player 3: ", p2_trick, "for player 4: ", p3_trick)
                print("It's a Tie!")

            else:
                print("Final mini rounds points are", "for player 1: ",
                      p0_trick, "for player 2: ", p1_trick,
                      "for player 3: ", p2_trick, "for player 4: ", p3_trick,
                      "for player 5: ", p4_trick)
                if max(points) == p0_trick:
                    print("player 1 has won ")

                elif max(points) == p1_trick:
                    print("player 2 has won ")

                elif max(points) == p2_trick:
                    print("player 3 has won ")

                elif max(points) == p3_trick:
                    print("player 4 has won ")

                else:
                    if max(points) == p4_trick:
                        print("Player 5 has won")

    restart_input = ["yes", "y", "no", "n"]
    restart = input("Would you like to restart? (y/n) ")

    while True:
        if restart in restart_input:
            break
        else:
            print("Invalid input, please type either yes (y) or no (n)")
            restart = input("would you like to restart? (y/n)")
    if restart == "y" or restart == "yes":
        round_number = 1
        miniround_number = 1
    else:
        break
