# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import mysql.connector
import pyfiglet

# Database connection
host = "localhost"
user = "root"
password = "fisayo11"
database = "mls2024"

try:
    # Connect to mysql
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connected successfully")

    cursor = connection.cursor()

    # read data queries

    def read_data_player():
        select_query = "Select PID, firstname, lastname, goals, assists, yellowcards, redcards, clubname from player"
        cursor.execute(select_query)
        players = cursor.fetchall()

        print("Player Data:")
        for player in players:
            print(f"PID: {player[0]} | First Name: {player[1]} | Last Name: {player[2]} | Club Name: {player[7]}")

    def read_data_club():
        select_query = "Select TID, clubname, stadium, clubmanager from club"
        cursor.execute(select_query)
        clubs = cursor.fetchall()

        print("Club Information:")
        for club in clubs:
            print(f"TID: {club[0]} | Club Name: {club[1]} | Stadium: {club[2]} | Club Manager: {club[3]}")

    def read_data_manager():
        select_query = "SELECT MID, firstname, lastname, wins, losses, clubmanaged FROM manager"
        cursor.execute(select_query)
        managers = cursor.fetchall()

        print("Manager Information:")
        for manager in managers:
            print(
                f"MID: {manager[0]} | First Name: {manager[1]} | Last Name: {manager[2]} | Club Managed: {manager[5]}")

    def read_data_match():
        select_query = "SELECT MatchID, Attendence, hometeam, awayteam, RID FROM `match`"
        cursor.execute(select_query)
        matches = cursor.fetchall()

        print("Matches Information:")
        for match in matches:
            print(
                f"MatchID: {match[0]} | HomeTeam: {match[2]} | AwayTeam: {match[3]} | "
                f"RID: {match[4]} | Attendance: {match[1]}")

    def read_data_stadium():
        select_query = "SELECT SID, City, StadiumName, `#ofEmployees`, Club FROM stadium"
        cursor.execute(select_query)
        stadiums = cursor.fetchall()

        print("Stadium Information:")
        for stadium in stadiums:
            print(
                f"SID: {stadium[0]} | City: {stadium[1]} | Stadium Name: {stadium[2]} | "
                f"#ofEmployees: {stadium[3]} | Club: {stadium[4]}")

    def read_data_referee():
        select_query = "SELECT RID, firstname, lastname FROM referee"
        cursor.execute(select_query)
        referees = cursor.fetchall()

        print("Referee Information:")
        for referee in referees:
            print(
                f"RID: {referee[0]} | First Name: {referee[1]} | Last Name: {referee[2]}")

    def read_data_playermatch():
        select_query = "SELECT PID, MatchID, Goals, Assists, YellowCards FROM playermatch"
        cursor.execute(select_query)
        playermatches = cursor.fetchall()

        print("Player-Match Information:")
        for playermatch in playermatches:
            print(
                f"PID: {playermatch[0]} | MatchID: {playermatch[1]} | Goals: {playermatch[2]} | Assists: {playermatch[3]} | YellowCards: {playermatch[4]}")

    # insert data

    def insert_data():
        while True:
            PID = input("Enter PID (Ex. P016): ")

            # Check if the entered PID already exists in the database
            cursor.execute("SELECT PID FROM player WHERE PID = %s", (PID,))
            existing_pid = cursor.fetchone()

            if existing_pid:
                print("Error: PID already exists. Please enter a unique PID.")
            elif not PID.startswith("P0") or len(PID) != 4:
                print("Error: Invalid PID format. PID must start with 'P0' and have 2 additional numbers.")
            else:
                break  # Exit the loop if the input is valid

        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        goals = int(input("Enter goals: "))
        assists = int(input("Enter assists: "))
        yellow_cards = int(input("Enter yellow cards: "))
        red_cards = int(input("Enter red cards: "))
        club_name = input("Enter club name: ")

        insert_query = "INSERT INTO player (PID, firstname, lastname, goals, assists, yellowcards, redcards, clubname) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (PID, first_name, last_name, goals, assists, yellow_cards, red_cards, club_name))
        connection.commit()
        print("Data inserted successfully.")

    # update data

    def update_data():
        player_id = input("Enter player ID to update: ")
        goals = int(input("Enter new goals: "))
        assists = int(input("Enter new assists: "))
        yellow_cards = int(input("Enter new yellow cards: "))
        red_cards = int(input("Enter new red cards: "))

        update_query = "UPDATE player SET goals = %s, assists = %s, yellowcards = %s, redcards = %s WHERE PID = %s"
        cursor.execute(update_query, (goals, assists, yellow_cards, red_cards, player_id))
        connection.commit()
        print("Data updated successfully.")

    # delete data

    def delete_data():
        player_id = input("Enter player ID to delete: ")
        delete_query = "DELETE FROM player WHERE PID = %s"
        cursor.execute(delete_query, (player_id,))
        connection.commit()
        print("Data deleted successfully.")

    # basic functions

    def player_data_stats():
        select_query = "Select PID, firstname, lastname, goals, assists, yellowcards, redcards, clubname from player"
        cursor.execute(select_query)
        players = cursor.fetchall()

        print("Player Data:")
        for player in players:
            print(f"PID: {player[0]} | First Name: {player[1]} | Last Name: {player[2]} | Goals: {player[3]} | "
                  f"Assists: {player[4]} | YellowCards: {player[5]} | RedCards: {player[6]} | Club Name: {player[7]}")

    def club_data_stats():
        select_query = "Select TID, clubname, matchesplayed, points, wins, ties, losses, gf, ga, gd, conference from club"
        cursor.execute(select_query)
        clubs = cursor.fetchall()

        print("Club Information:")
        for club in clubs:
            print(f"TID: {club[0]} | Club Name: {club[1]} | Conference: {club[10]} | MatchesPlayed: {club[2]} | Points: {club[3]} "
                  f"| Wins: {club[4]} | Ties: {club[5]} "
                  f"| Losses: {club[6]} | Goals Scored: {club[7]} | Goals Conceded: {club[8]} | Goal Differential: {club[9]}")

    def show_percentage_nonscorers():
        nonscorers_query = """
        SELECT CONCAT((SELECT COUNT(PID) FROM player WHERE goals = 0) / COUNT(PID) * 100, '%') AS Nonscorers
        FROM player;
        """
        cursor.execute(nonscorers_query)
        result = cursor.fetchone()

        print("Percentage of Players Who Have Not Scored This Season:")
        print(f"{result[0]}")

    def show_highest_wins():
        rank_query = """ 
            Select TID, ClubName, Wins from club where wins = (select max(wins) from club);
        """
        cursor.execute(rank_query)
        results = cursor.fetchall()

        print("Highest Number of Wins:")
        for result in results:
            print(
                f"TID: {result[0]} | Club Name: {result[1]} | Wins: {result[2]}")

    def show_stadium_ranks():
        rank_query = """
        SELECT SID, Club, StadiumName, `#ofEmployees`,
        RANK() OVER (ORDER BY `#ofEmployees` DESC) AS StadiumRank
        FROM stadium;
        """
        cursor.execute(rank_query)
        results = cursor.fetchall()

        print("Stadiums Ranked by Number of Employees:")
        for result in results:
            print(
                f"SID: {result[0]} | Club: {result[1]} | Stadium Name: {result[2]} | Number of Employees: {result[3]} | Rank: {result[4]}")

    def show_players_redcards():
        redcards_query = "SELECT * FROM player WHERE redcards > 0"
        cursor.execute(redcards_query)
        result = cursor.fetchall()

        print("Players Who Have Received At Least One Red Card:")
        for player in result:
            print(f"PID: {player[0]} | First Name: {player[1]} | Last Name: {player[2]} | Goals: {player[3]} | "
                  f"Assists: {player[4]} | Yellow Cards: {player[5]} | Red Cards: {player[6]} | Club Name: {player[7]}")

    # advanced functions

    def show_team_ranks():
        rank_query = """
        Select TID, ClubName, Points, RANK() OVER (ORDER BY Points DESC) AS OverallRank
        from club;
        """
        cursor.execute(rank_query)
        results = cursor.fetchall()

        print("MLS Teams Ranked by Points:")
        for result in results:
            print(f"TID: {result[0]} | Club Name: {result[1]} | Points: {result[2]} | Rank: {result[3]}")

    def show_stadium_cume_dist():
        cume_dist_query = """
        SELECT SID, Club, StadiumName, `#ofEmployees`,
        ROUND(CUME_DIST() OVER (ORDER BY `#ofEmployees`), 2) AS stadium_cume_dist
        FROM stadium;
        """
        cursor.execute(cume_dist_query)
        results = cursor.fetchall()

        print("Cumulative Distribution of Stadiums by Employees:")
        for result in results:
            print(
                f"SID: {result[0]} | Club: {result[1]} | Stadium Name: {result[2]} | Number of Employees: {result[3]} | Cume Dist: {result[4]}")

    def show_stadium_ntiles():
        ntile_query = """
        SELECT SID, Club, StadiumName, `#ofEmployees`,
        NTILE(6) OVER (ORDER BY `#ofEmployees` DESC) AS StadiumNTile6
        FROM stadium;
        """
        cursor.execute(ntile_query)
        results = cursor.fetchall()

        print("Stadiums Grouped by Ntiles (6 Groups):")
        for result in results:
            print(
                f"SID: {result[0]} | Club: {result[1]} | Stadium Name: {result[2]} | Number of Employees: {result[3]} | NTile Group: {result[4]}")

    def show_players_onegoal():
        onegoal_query = "SELECT * FROM player WHERE goals > 0"
        cursor.execute(onegoal_query)
        result = cursor.fetchall()

        print("Players Who Have At Least ONE Goal:")
        for player in result:
            print(f"PID: {player[0]} | First Name: {player[1]} | Last Name: {player[2]} | Goals: {player[3]} | "
                  f"Assists: {player[4]} | YellowCards: {player[5]} | RedCards: {player[6]} | Club Name: {player[7]}")

    def show_percentage_nonwinners():
        nonwinners_query = """
        Select Concat((Select Count(TID) from club where wins = 0) / Count(TID)*100,'%')
        As Nonwinners from club
        """
        cursor.execute(nonwinners_query)
        result = cursor.fetchone()

        print("Percentage of Teams Who Have Won This Season:")
        print(f"{result[0]}")

    def get_conference_stats():
        query = """
                    SELECT
                        IFNULL(conference, 'Total') AS conference,
                        SUM(GF) AS total_goals,
                        SUM(GA) AS total_goals_conceded,
                        SUM(Wins) as total_wins,
                        SUM(Losses) as total_losses,
                        SUM(points) AS total_points
                    FROM
                        club
                    GROUP BY
                        conference WITH ROLLUP;
                """
        cursor.execute(query)
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        for result in results:
            print(
                f"Conference: {result[0]} | Total Goals: {result[1]} | Total Goals Conceded: {result[2]} "
                f"| Total Wins: {result[3]} | Total Losses: {result[4]} | Total Points {result[5]}"
            )

    def main():
        while True:
            print("\nMenu: ⚽⚽⚽")
            print("1. read data")
            print("2. update data")
            print("3. insert data")
            print("4. delete data")
            print("5. basic functions")
            print("6. advanced functions")
            print("7. exit")

            choice = input("Enter your choice: \n")
            if choice == '1':
                print("\nWhich Table Would You Like To View?")
                print("1. player data")
                print("2. club data")
                print("3. manager data")
                print("4. match data")
                print("5. referee data")
                print("6. stadium data")
                print("7. player-match data")

                choice2 = input("Enter your choice: \n")
                if choice2 == '1':
                    read_data_player()
                elif choice2 == '2':
                    read_data_club()
                elif choice2 == '3':
                    read_data_manager()
                elif choice2 == '4':
                    read_data_match()
                elif choice2 == '5':
                    read_data_referee()
                elif choice2 == '6':
                    read_data_stadium()
                elif choice2 == '7':
                    read_data_playermatch()

            elif choice == '2':
                update_data()

            elif choice == '3':
                insert_data()

            elif choice == '4':
                delete_data()

            elif choice == '5':
                print("\nSelect Basic Function")
                print("1. view player stats")
                print("2. view club stats")
                print("3. show stadium ranks (by #ofemployees")
                print("4. show percentage of nonscoreres")
                print("5. show teams that have the most wins this season")
                print("6. show players who have at least ONE redcard")

                choice5 = input("Enter your choice: \n")
                if choice5 == '1':
                    player_data_stats()
                elif choice5 == '2':
                    club_data_stats()
                elif choice5 == '3':
                    show_stadium_ranks()
                elif choice5 == '4':
                    show_percentage_nonscorers()
                elif choice5 == '5':
                    show_highest_wins()
                elif choice5 == '6':
                    show_players_redcards()
                else:
                    print("\nEnter A Valid Number!")

            elif choice == '6':
                print("\nSelect Advanced Function")
                print("1. show team ranks")
                print("2. show stadium cumulative distribution")
                print("3. show stadium ntiles")
                print("4. show percentage of teams who have not won a game this season")
                print("5. show players who have at least ONE goal")
                print("6. show conference stats")

                choice6 = input("Enter your choice: \n")
                if choice6 == '1':
                    show_team_ranks()
                elif choice6 == '2':
                    show_stadium_cume_dist()
                elif choice6 == '3':
                    show_stadium_ntiles()
                elif choice6 == '4':
                    show_percentage_nonwinners()
                elif choice6 == '5':
                    show_players_onegoal()
                elif choice6 == '6':
                    get_conference_stats()
                else:
                    print("\nEnter A Valid Number!")

            elif choice == '7':
                connection.close()
                return 0

            else:
                print("\nEnter A Valid Number!")

    main()

except mysql.connector.Error as error:
    print("Error connecting to MySQL:", error)
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
