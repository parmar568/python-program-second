#probability pro-1
tcard=52        #total  card 
tking=4         #how many king cards in  total card 
tspade=12       #how many card spade cards in total card 
check=tcard-(tking+tspade)      #sum of the king card and spade card and (-) total card 
print("king and spade probability is",(tking+tspade)/tcard)  #KING AND SPEDE HOVA NI PROBABILITY
print("neither king nor spade probability is : ",check/tcard)       #than print but div total card to new values