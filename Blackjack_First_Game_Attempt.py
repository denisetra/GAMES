##This program was written in Python 3.6
## Will need to re-write this.
##Appears to work in all cases except when player stands before computer is done. Game cuts off then.
##Also, treatment of Ace doesn't work.
##When I re-write this, will need to be more modular (functions)


import random


Suit_dict={1:1,11:11,'King':10,'Queen':10,'Jack':10,'Ten':10,'Nine':9,'Eight':8,'Seven':7,'Six':6,'Five':5,'Four':4,'Three':3,'Two':2}

Deck=['Ace', 'King', 'Queen', 'Jack', 'Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two','Ace', 'King', 'Queen', 'Jack', 'Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two','Ace', 'King', 'Queen', 'Jack', 'Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'Ace', 'King', 'Queen', 'Jack', 'Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two']

player_hand=[]
computer_hand=[]
temp_hand=[]
temp_c_hand=[]

done=0

def Poker():
    running_deck=Deck[:]
    player_hand_sum = 0
    computer_hand_sum = 0
    global done

    while player_hand_sum <=21 and computer_hand_sum <=21:
        player_start=input('\nDo you want to take a card? (yes/no) ').lower()
        if player_start=='yes':
            card=random.choice(running_deck)
            #print ('Your card is: ',card)
            running_deck.remove(card)
            player_hand.append(card)
            print ('Your hand has the following card(s): ',player_hand)
            if card=="Ace":
                if player_hand_sum>10:
                    card=1
                else:
                    card=11
            temp_card=Suit_dict[card]
            temp_hand.append(temp_card)
            player_hand_sum=sum(temp_hand)
            #print ('The current hand value is:',player_hand_sum,"\n")

            if computer_hand_sum >= 17:
                print ('The computer stands at:',computer_hand_sum)
            else:

                comp_card=random.choice(running_deck)
                #print ("Computer's card is: ",comp_card)
                running_deck.remove(comp_card)
                computer_hand.append(comp_card)
                print ("The Computer's hand is: ",computer_hand,'\n')
                if card == "Ace":
                    if computer_hand_sum > 10:
                        comp_card = '1'
                    else:
                        comp_card = '11'
                temp_c_card=Suit_dict[comp_card]
                temp_c_hand.append(temp_c_card)
                computer_hand_sum=sum(temp_c_hand)
                #print ("The Computer's hand is currently valued at : ",computer_hand_sum,"\n")
        else:
            if computer_hand_sum>player_hand_sum and computer_hand_sum<22:
                print ('The computer won!!!')
                print ('Player score: ',player_hand_sum,"\nComputer Score: ",computer_hand_sum)
            elif computer_hand_sum==player_hand_sum:
                print ('Its a tie at: ',player_hand_sum," each!!!")
            else:
                if player_hand_sum>=computer_hand_sum and player_hand_sum<22:
                    print ('YOU WON!!!!!!!!!!!!!!!!!')
                    print('Player score: ', player_hand_sum, "\nComputer Score: ", computer_hand_sum)
            done=1
            break
    print ("\n\n+++++++++++++++++FINAL RESULTS+++++++++++++++")
    if computer_hand_sum > player_hand_sum and computer_hand_sum < 22:
        print('!!!The computer won!!!')
        print('Player score: ', player_hand_sum, "\nComputer Score: ", computer_hand_sum)
    elif computer_hand_sum == player_hand_sum:
        print('!!!Its a tie at: ', player_hand_sum, " each!!!")
    else:
        if player_hand_sum > computer_hand_sum and player_hand_sum < 22:
            print('!!!YOU WON!!!!!!!!!!!!!!!!!')
            print('Player score: ', player_hand_sum, "\nComputer Score: ", computer_hand_sum)




Poker()




