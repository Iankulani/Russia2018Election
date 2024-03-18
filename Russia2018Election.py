# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 03:33:04 2024

@author: IAN CARTER KULANI
"""
# -*- coding: utf-8 -*-
#This software prompts the user to enter total number of published centers,total number of registered votes, total number of null and void votes, total number of valid votes and total valid votes for each candidate. Afterward, it determines the candidate with the majority of votes and displays the results on the screen.
#NOTE:For a candidate to be a majority winner the candidate total valid votes should be greater than majority votes.
print("Dyna-stat software [version 1]\n(c) Dyna-stat software.All rights Reserved.")
print("====================================RUSSIA 2024 ELECTION====================================\n") 
Totalpublishedcenters=int(input("Enter Total published centers:"))
#Get the total number of registered votes
TotalRegisteredvotes=int(input("Enter Total Registered Voters/Turnout:"))
#Get Total number of votes cast
Totalvotescast=int(input("Enter Total Votes Cast/Total Votes:"))
#Get total number of Null_&_Void votes
Nullandvoid=int(input("Enter Total Null_&_Void Votes/Invalid Votes:"))
#Get Total Valid Votes for All candidates
Totalvalidvotes=int(input("Enter Total Valid Votes:"))
#Get Total Valid Votes for Vladimir Putin
Totalvalidvotesfor_Vladimir_Putin=int(input("Enter Total Valid Votes for Vladimir Putin:"))
#Get Total Valid Votes for Grigory_Yavlinsky
Totalvalidvotesfor_Pavel_Gudini=int(input("Enter Total Valid Votes for Pavel Gudini:"))
#Get Total Valid Votes for Vladimir Zhironousky 
Totalvalidvotesfor_Vladimir_Zhironousky=int(input("Enter Total Valid Votes for Vladimir Zhironousky:"))
#Get Total Valid Votes for Ksenia Sobchak
Totalvalidvotesfor_Ksenia_Sobchak=int(input("Enter Total Valid Votes for Ksenia Sobchak:"))
#Get Total Valid Votes for  Grigory Yavlinsky
Totalvalidvotesfor_Grigory_Yavlinsky=int(input("Enter Total Valid Votes for Grigory Yavlinsky:"))
#Get Total Valid Votes for Boris Titov
Totalvalidvotesfor_Boris_Titov=int(input("Enter Total Valid Votes for Boris Titov:"))
#Get Total Valid Votes for  Maxim Suraykin
Totalvalidvotesfor_Maxim_Suraykin=int(input("Enter Total Valid Votes for Maxim Suraykin:"))
#Get Total Valid Votes for Sergey Baburin
Totalvalidvotesfor_Sergey_Baburin=int(input("Enter Total Valid Votes for Sergey Baburin:"))

percent=100
if Totalvalidvotesfor_Vladimir_Putin>Totalvalidvotes/2+1:
   print("Cogratulations Vladimir Putin you're the winner of 2018 election\n\n")
 
elif Totalvalidvotesfor_Pavel_Gudini>Totalvalidvotes/2+1:
     print("Cogratulations Pavel Gudini you're the winner of 2018 election\n\n")
   
elif Totalvalidvotesfor_Vladimir_Zhironousky>Totalvalidvotes/2+1:
     print("Cogratulations Vladimir Zhironousky  you're the winner of 2018 elections")
    
elif Totalvalidvotesfor_Ksenia_Sobchak>Totalvalidvotes/2+1:
     print("Cogratulations Ksenia_Sobchak you're the winner of 2018 election\n\n")

elif Totalvalidvotesfor_Grigory_Yavlinsky>Totalvalidvotes/2+1:
     print("Cogratulations Grigory Yavlinsky you're the winner of 2018 election\n\n")

elif Totalvalidvotesfor_Boris_Titov>Totalvalidvotes/2+1:
     print("Cogratulations Boris Tito you're the winner of 2018 election\n\n")
   
elif Totalvalidvotesfor_Maxim_Suraykin>Totalvalidvotes/2+1:
     print("Cogratulations Maxim Suraykin  you're the winner of 2018 elections")
    
elif Totalvalidvotesfor_Sergey_Baburin>Totalvalidvotes/2+1:
     print("Cogratulations Sergey Baburin you're the winner of 2018 election\n\n")

else:
    print("No majority winner was found RUN OFF May be required\n\n")   

print("_________________________________ELECTION STATISTICS_____________________________________\n") 
   
#Calculating Percentage    
Percentage=round(Totalvalidvotes*percent/Totalvalidvotes, 2);
print("Total Votes Cast in percentage=",Percentage)
Percentage=round(Totalvalidvotes*percent/Totalvotescast, 2);
print("Total Valid Votes for all candidtes in percentage=",Percentage)

#Calculating percentage for null_&_void votes
Percentage=round(Nullandvoid*percent/Totalvalidvotes, 2);
print("Total Null_&_Void votes in percentage=",Percentage)
#
Percentage=round(Totalvalidvotesfor_Vladimir_Putin*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Vladimir Putin in percentage=",Percentage )

Percentage=round(Totalvalidvotesfor_Pavel_Gudini*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Pavel Gudini  in percentage=",Percentage )

Percentage=round(Totalvalidvotesfor_Vladimir_Zhironousky*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Vladimir_Zhironousky in percentage=",Percentage )

Percentage=round(Totalvalidvotesfor_Ksenia_Sobchak*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Ksenia Sobchak in percentage=",Percentage )

Percentage=round(Totalvalidvotesfor_Grigory_Yavlinsky*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Grigory Yavlinsky in percentage=",Percentage )

Percentage=round(Totalvalidvotesfor_Boris_Titov*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Boris_Tito in percentage=",Percentage )

Percentage=round(Totalvalidvotesfor_Maxim_Suraykin*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Maxim Suraykin in percentage=",Percentage )

Percentage=round(Totalvalidvotesfor_Sergey_Baburin*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Ksenia Sobchak in percentage=",Percentage )


print("==========================================================================================\n") 


  















