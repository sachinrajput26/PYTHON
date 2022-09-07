print("********************WELCOME*******************")
print("election for selection of chairman for educational committee of swami vivekanand trust")
vote='N'
votes_Mr_cb_singh=0
votes_Mr_sachin_rajput=0
votes_Mrs_prachi_thadani=0
votes_Mr_jitendra_singh=0
vote_NOTA=0
while (vote.upper()=='C' or vote.upper()=='S' or vote.upper()=="P" or vote.upper()=='J' or vote.upper()=='N'):
    vote=input("press C:for Mr.cb singh \npress S:for Mr.sachin rajput\npress P:for Mrs.prachi thadani\npress J:for Mr.jitendra singh\npress N:for NOTA\npress E: for exit \nenter your choice: ")
    if (vote.upper()=='C'):
        votes_Mr_cb_singh+=1
    elif(vote.upper()=='S'):
        votes_Mr_sachin_rajput+=1
    elif(vote.upper()=='P'):
        votes_Mrs_prachi_thadani+=1
    elif(vote.upper()=='J'):
        votes_Mr_jitendra_singh+=1
    elif(vote.upper()=='N'):
        vote_NOTA+=1
if votes_Mr_cb_singh > votes_Mr_sachin_rajput and votes_Mr_cb_singh > votes_Mrs_prachi_thadani and votes_Mr_cb_singh > votes_Mr_jitendra_singh and votes_Mr_cb_singh>vote_NOTA:
    print(" *************congratulations*********** \nMr CB SINGH \nyou are selected as chairman of educational committee of swami vivekanand trust \n total number of votes="+str(votes_Mr_cb_singh))
elif votes_Mr_sachin_rajput > votes_Mr_cb_singh and votes_Mr_sachin_rajput > votes_Mrs_prachi_thadani and votes_Mr_sachin_rajput > votes_Mr_jitendra_singh and votes_Mr_sachin_rajput > vote_NOTA:
    print(" *************congratulations*********** \nMr SACHIN RAJPUT \nyou are selected as chairman of educational committee of swami vivekanand trust \n total number of votes="+str(votes_Mr_sachin_rajput))
elif votes_Mrs_prachi_thadani > votes_Mr_cb_singh and votes_Mrs_prachi_thadani > votes_Mr_sachin_rajput and votes_Mrs_prachi_thadani > votes_Mr_jitendra_singh and votes_Mrs_prachi_thadani > vote_NOTA:
    print(" *************congratulations*********** \nMrs PRACHI THADANI \nyou are selected as chairman of educational committee of swami cvivekanand trust \n total number of votes="+str(votes_Mrs_prachi_thadani))
elif votes_Mr_jitendra_singh > votes_Mr_cb_singh and votes_Mr_jitendra_singh > votes_Mr_sachin_rajput and votes_Mr_jitendra_singh > votes_Mrs_prachi_thadani and votes_Mr_jitendra_singh > vote_NOTA:
    print(" *************congratulations*********** \nMr JITENDRA SINGH \nyou are selected as chairman of educational committee of swami vivekanand trust \n total number of votes="+str(votes_Mr_jitendra_singh))
elif vote_NOTA > votes_Mr_cb_singh and vote_NOTA > votes_Mr_sachin_rajput and vote_NOTA > votes_Mrs_prachi_thadani and vote_NOTA > votes_Mr_jitendra_singh:
    print('most of voters opted for NOTA so chairman of educational committee swami vivekanand trust will be Mr. CB SINGH as a senior most member of trust.  ') 
else:
    print('most of voters opted for NOTA so chairman of educational committee swami vivekanand trust will be Mr. CB SINGH as a senior most member of trust.  ') 
