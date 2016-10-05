
def soccer_players():
    """ the first program of this file reads data from a text file on the disk, creates a dictionary of players with
    strings and lists as keys and values respectively. The output in the format of a dictionary is passed to the
    second program which then sorts the players into 3 different teams equally based on their experience.
    Finally, the last program prints personalized letters to the guarding informing them about the teams and
    schedules """

    with open('soccer_players.csv', 'r', encoding='utf-8') as file:  # open file from a relative path
        master_dict = {}
        file.seek(len(file.readline()) + 1)  # reset line position to 2nd line to avoid reading headers
        for row in file.readlines():
            row_split = row.strip().split(',')  # split lines at each comma
            master_dict.update({row_split[0]: [row_split[1], row_split[2], row_split[3]]})  # update the dictionary
        return master_dict


def team_builder(master_dict):
    sharks = {}
    dragons = {}
    raptors = {}
    yes_count = 0
    no_count = 0

    # sort players in 3 teams based on their experience. Also appends the team name to the respective dictionary

    for key, value in master_dict.items():

        if 'YES' in master_dict[key] and yes_count < 3:
            sharks.update({key: value})
            sharks[key].append('sharks')
            sharks[key].append('March 17, 3pm')
            yes_count += 1
        elif 'NO' in master_dict[key] and no_count < 3:
            sharks.update({key: value})
            sharks[key].append('sharks')
            sharks[key].append('March 17, 3pm')
            no_count += 1
        elif 'YES' in master_dict[key] and yes_count < 6:
            dragons.update({key: value})
            dragons[key].append('dragons')
            dragons[key].append('March 17, 1pm')
            yes_count += 1
        elif 'NO' in master_dict[key] and no_count < 6:
            dragons.update({key: value})
            dragons[key].append('dragons')
            dragons[key].append('March 17, 1pm')
            no_count += 1
        else:
            raptors.update({key: value})
            raptors[key].append('raptors')
            raptors[key].append('March 18, 1pm')

    master_tuple = sharks, dragons, raptors
    return master_tuple


def print_letters(master_tuple):
    for teams in master_tuple:
        for key, value in teams.items():
            name = key.split()[0].lower() + '_' + key.split()[1].lower()
            with open(name + '.txt', 'w', encoding='utf-8') as file:  # read from the desk

                player = str(key)
                # player.split()
                # player = player.split()[0] + '_' + player.split()[1]
                guardian = str(value[2])
                team = str(value[3])
                dates = str(value[4])
                string = '''

                Dear Guardian(s): {}
                Player Name: {}
                Team Name: {}
                Date and Time of First Practice: "{}"

                Best Regards
                Soccer LeagueTeam'''

                letter = string.format(guardian, player, team.upper(), dates)
                file.write(letter)  # write all 18 letters to disk

if __name__ == "__main__":
    main_dict = soccer_players()
    built_tuple = team_builder(main_dict)
    print_letters(built_tuple)
