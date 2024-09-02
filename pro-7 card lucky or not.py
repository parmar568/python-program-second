cards=['ace of spade','heart','queen of diamond','king of diamond',7]   #difind some of luck cards

card=input("enter any card like:king of spade:").lower()    #enter the card user
if(card in cards):  #check condition to card in luck or not 
    print("You are lucky!")
elif('heart' in card or '7' in card):
    print("You are lucky!")
else:
   print("better luck next time!")
  

