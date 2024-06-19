# MLS2024Database

Our project is on the MLS. We show player stats, clubs, stadiums, managers, and referees. We are able to organize all this data into a simple, user friendly platform, so MLS watchers can have this information at their fingertips. 

In our code we read player data, club data, have functions with inserting data, updating data, deleting data, player data stats, stadium ranks, team ranks, stadium ntiles, stadium distance, and percent of non-scorers. Within our main function we have user input commands, this way the user can choose what they want to do based on the options given. 

The first option in our “menu” is read data. By doing this we get 2 sub options, player data and club data, with player data being tied to 1 and club data to 2. By entering the number 1 again the user can see the player data of all players within the database. The data shown will be PID, first name, last name, and club name. By entering the number 2 instead the user can see the club data of all clubs within the database. The data shown will be the club name, stadium, and manager. 

The second option is update data. By entering the number 2 we will enter this process. The user will be asked to enter the player who they want to update’s PID. They can then update the goals, assists, yellow cards, and red cards tied to this player. After this process the player will be updated and entered into the database and can then be seen within read data. 

The third option is insert data. By entering the number 3 we will enter this process. The user will be asked to enter values for this new player: PID, first name, last name, goals, assists, yellow cards, red cards, and club name. This new player will then officially become a part of the database and can be viewed in read data.

The fourth option is delete data. By entering the number 4 we will enter this process. The user will be asked to enter the PID of the player they wish to delete. After that the player will officially be removed from the database.

The fifth option is basic functions. By entering the number 5 we will be able to enter this process. The user will get another prompt to click the number 1, by doing so they will be able to see the player stats. This lets the user see the goals, assists, yellow cards, red cards, and club name, for all players in the database.

The sixth option is advanced functions, these are our OLAP queries. By entering the number 6 we will enter this process. Here the user can see, team ranks, stadium cumulative distribution, stadium ntiles, percentage of teams who have not won a game this season, and players who have at least one goal.

Finally the seventh option lets the user exit the program. 

We have great error catching within our program to limit any confusion and keep the process fun, easy, and simple.


Video: https://www.loom.com/share/b645080815b643f0a92111acca271a1b?sid=7aa7bd65-bd88-4a96-846d-2bdd8831ec6b


