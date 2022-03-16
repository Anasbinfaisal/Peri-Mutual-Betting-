import random
import pickle
import os
import pathlib
from bank_system import *


class Account:
    accNo = 0
    name = ''
    deposit=0
    type = ''
    bet_amt = 0
    bet_team = -1
    bet_done = False

#
# class player:
#     name = ""
#     bet_amt = 0
#     bet_team = -1
#     bet_done = False
#
# betplayer = player()

class bet_data:
    bet_pool = 0
    Match = ""



bet_pool = 0
team1_count = 0
team2_count = 0
team1_amt = 0
team2_amt = 0

def bets_data_update(match, bet_pool):
    file = pathlib.Path("bets.data")
    if file.exists():
        infile = open('bets.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        for item in oldlist:
            if item.Match == match:
                item.bet_pool = bet_pool

        outfile = open('bets.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        # os.rename('newbets.data', 'bets.data')
    else:
        print("\nFile does not exist")




def bets_data(bet_data):
    found = 0
    file = pathlib.Path("bets.data")
    if file.exists():
        infile = open('bets.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        for item in oldlist:
            if item.Match == bet_data.Match:
                print("\n{}".format(item.Match))
                found = 1
        if found != 1:
            	oldlist.append(bet_data)
            	print("\n{}".format(bet_data.Match))
            	outfile = open('bets.data', 'wb')
            	pickle.dump(oldlist, outfile)
            	outfile.close()
            	
    else:
        oldlist = [bet_data]
        outfile = open('bets.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()


def reset_bets_data(bet_data):
    file = pathlib.Path("bets.data")
    if file.exists():
        infile = open('bets.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        for item in oldlist:
            if item.Match == bet_data.Match:
                item.bet_pool = 0

    else:
        oldlist = [bet_data]
        outfile = open('bets.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()


def access_bet_account(num):
    found = 0
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        #os.remove('accounts.data')
        for item in oldlist:
            if item.accNo == num:
                found = 1
                return True
            else:
                continue

        if found == 0:
            return False
    else:
        print("File does not exist")


def modify_account(num, betplayer):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accNo == num:
                item.name = betplayer.name
                item.bet_amt = betplayer.bet_amt
                item.bet_team = betplayer.bet_team
                item.bet_done = betplayer.bet_done

        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


def intro_banner():
    s = "Welcome to the Game!"
    print(s)


def game_over():
    s = "Game Over. Bye!"
    print(s)


def evaluate(win):
    global bet_pool
    global team1_count, team1_amt
    global team2_count, team2_amt
    count = 0
    count_item = 0

    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')

        for item in oldlist:
            count_item += 1
            if item.bet_done:
                count+=1

        print(count_item)

        if (count == count_item) and (win!=0):

            print("\nEvaluating Match results!\n")
            print("Winning Team: Team#",win)
            for item in oldlist:
                
                if item.accNo == 100:
                	item.bet_done = True
                	item.bet_amt = 10
                	item. bet_team = 1
                	continue
                	
                if item.accNo == 101:
                	item.bet_done = True
                	item.bet_amt = 10
                	item. bet_team = 2
                	continue
                	
                item.bet_done = False
               

                if item.bet_team == win:
                    item.bet_team = -1
                    if win == 1:
                        winning = (bet_pool / team1_amt) * item.bet_amt
                        print(round(winning, 2))
                        item.deposit += round(winning, 2 )

                    elif win == 2:
                        winning = (bet_pool / team2_amt) * item.bet_amt
                        print(round(winning, 2))
                        item.deposit += round(winning, 2)

                else:
                    item.bet_team = -1
                 
                item.bet_amt = 0

        else:
            print("All players have not placed their bets or Results have not been announced.")

        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


        if count == count_item:
            displayAll()

    else:
        print("File does not exist")



def get_bet_pool():
    global bet_pool
    global team1_count, team1_amt
    global team2_count, team2_amt

    bet_pool = 0
    team1_count = 0
    team2_count = 0
    team1_amt = 0
    team2_amt = 0

    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()

        for item in oldlist:
            if item.accNo == 100 or item.accNo == 101:
            	bet_pool += item.bet_amt
            else:
	            bet_pool += item.bet_amt
	
	            if item.bet_team == 1:
	                team1_count += 1
	                team1_amt += item.bet_amt
	                
	            elif item.bet_team == 2:
	                team2_count += 1
	                team2_amt += item.bet_amt
	            else:
	                team1_count += 0
	                team2_count += 0
	                team1_amt += 0
	                team2_amt += 0



    else:
        print("File does not exist")



def main():

    win = 1
    bet_data_new = bet_data()
    bet_data_new.Match = "Match: QG vs LQ"

    global bet_pool
    global team1_count, team1_amt
    global team2_count, team2_amt
    keepplaying = False

    intro_banner()
    #Login
    set_data = (input("Do you want to set data auto or manually? "))
    
    if set_data == "y":
        set_match_data()
    elif set_data == "m":
        set_match_data_manual()
        
    get_bet_pool()
    bets_data(bet_data_new)
    print ("{:<8} {:<8} {:<8}".format('Bet Pool','Team 1','Team 2'))
    print ("{:<8} {:<8} {:<8}".format(bet_pool,team1_amt, team2_amt))
    #print("\nBetPool\tTeam1\tTeam2")
#    print(bet_pool, "\t", team1_count, "\t", team2_count)
    
    
        


    # playername = input('Player Name >> ')
    player_account = int(input('Player Account Number >> '))

    # if player_name and account matches, check for bet_done, if false then goto betting part
    betplayer_exists = access_bet_account(player_account)

    if betplayer_exists == False:
        keepplaying = False
        print("\nPlayer does not exist")

    if betplayer_exists == True:
        keepplaying, money = player_exists(player_account)

    while (keepplaying == True) :
       # print("\n",bet_data_new.Match)
        bet_team = int(input("\nEnter team number (1/2)>> "))
        if bet_team > 2:
            bet_team = int(input("Enter team number (1/2)>> "))

        bet = int(input("\nPlace your bet (10 or 20) >> "))
        isbetvalid  =  (bet == 10) or (bet >20)

        #Match - Lahore vs Islamabad
        # Lahore - 1      Islamabad - 2
       #bet_team = 1

       # isbetnotvalid = int(bet) > money or int(bet) < -1
        while isbetvalid != True:
            print("Please enter a valid bet.")
            bet = int(input("Place your bet >> "))
            isbetvalid = bet == 10 or bet ==20
        #    isbetnotvalid = int(bet) > money or int(bet) < -1

        print("\n Bet Amount and Team : ")
        print(bet, " ", bet_team)

        if (bet_team == 1):
            team1_count += 1
            team1_amt += bet
            
        elif (bet_team == 2):
            team2_count += 1
            team2_amt += bet

        bet_pool = bet_pool + bet 
        
        print ("{:<8} {:<8} {:<8}".format('Bet Pool','Team 1','Team 2'))
       
        print ("{:<8} {:<8} {:<8}".format(bet_pool,team1_amt, team2_amt))

        #print("\nBet Pool Team1 Team2")
#        print(bet_pool, "\t\t", team1_count, "\t\t" , team2_count)

        update_bets(player_account, bet, bet_team)
        keepplaying = False

    print(bet_pool)
    bets_data_update(bet_data_new.Match, bet_pool)

    displayAll()

    evaluate(win)
    
    show_match_data()



    choice = input("\nDo you want to exit? (y/n) ")
    if choice == 'y':
        exit()
    else:
        main()


def player_exists(player_account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        # os.remove('accounts.data')
        for item in oldlist:
            if item.accNo == player_account:
                if item.bet_done:
                    print("\nBet already placed!")
                    print("\nBet amount and, team is: ", item.bet_amt, item.bet_team)
                    return False, 0
                else:
                    money = displaySp(player_account)  ##account info - then show balance and get balance to money
                    print("Welcome to the game, " + item.name + ". Your starting amount is " + str(money) + ' Chips.')
                    return True, money


def update_bets(player_account, bet, bet_team):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')

        for item in oldlist:
            if item.accNo == player_account:
                item.bet_amt = bet
                item.bet_done = True
                item.bet_team = bet_team
                item.deposit -= bet

        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


def show_match_data():
    file = pathlib.Path("bets.data")
    if file.exists():
        infile = open('bets.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        print("\n{:<35} {:<15}".format("Match Title", "Bet Pool"))
         #os.remove('accounts.data')

        for item in oldlist:
         	
         	print("{:<35} {:<15}".format(item.Match, item.bet_pool))
#            
#
#         outfile = open('newaccounts.data', 'wb')
#         pickle.dump(oldlist, outfile)
#         outfile.close()
#         os.rename('newaccounts.data', 'accounts.data')
#
    else:
      	print("\nNo File Found")

def set_match_data():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')

        for item in oldlist:
          	
          	if item.accNo == 1 or item.accNo == 2 or item.accNo ==3:
          	    item.bet_amt = 20
          	    item.bet_team = 1
          	    item.bet_done = True
          	    item.deposit -= 20
          	    
          	elif item.accNo == 4 or item.accNo == 5 or item.accNo == 6:
          	    item.bet_amt = 20
          	    item.bet_team = 2
          	    item.bet_done = True
          	    item.deposit -= 20
          	  
          	    
          	elif item.accNo == 100 or item.accNo == 101:
          	    continue
#            
#
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
#
    else:
      	print("\nNo File Found")

def set_match_data_manual():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')

        for item in oldlist:
          	
          	if item.accNo == 1:
          	    item.bet_amt = 20
          	    item.bet_team = 2
          	    item.bet_done = True
          	    item.deposit -= item.bet_amt
          	    
          	elif item.accNo == 2:
          	    item.bet_amt = 30
          	    item.bet_team = 2
          	    item.bet_done = True
          	    item.deposit -=  item.bet_amt
          	
          	elif item.accNo == 3:
          	    item.bet_amt = 20
          	    item.bet_team = 2
          	    item.bet_done = True
          	    item.deposit -=  item.bet_amt
          	    
          	elif item.accNo == 4:
          	    item.bet_amt = 10
          	    item.bet_team = 2
          	    item.bet_done = True
          	    item.deposit -=  item.bet_amt
          	    
          	elif item.accNo == 5:
          	    item.bet_amt = 10
          	    item.bet_team = 2
          	    item.bet_done = True
          	    item.deposit -=  item.bet_amt
          	    
          	elif item.accNo == 6:
          	    item.bet_amt = 15
          	    item.bet_team = 2
          	    item.bet_done = True
          	    item.deposit -=  item.bet_amt        
          	          
          	                
          	elif item.accNo == 100 or item.accNo == 101:
          	    continue
#            
#
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
#
    else:
      	print("\nNo File Found")

main()