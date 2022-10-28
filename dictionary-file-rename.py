import os, sys

dict = {"Pilot":"S1E1 - Pilot", "Naming Rights":"S1E2 - Naming Rights", "YumTime":"S1E3 - YumTime", "Short Squeeze":"S1E4 - Short Squeeze", "The Good Life":"S1E5 - The Good Life", "The Deal":"S1E6 - The Deal", "The Punch":"S1E7 - The Punch", "Boasts and Rails":"S1E8 - Boasts and Rails", "Where the F*** is Donnie?":"S1E9 - Where the F*** is Donnie?", "Quality of Life":"S1E10 - Quality of Life", "Magical Thinking":"S1E11 - Magical Thinking", "The Conversation":"S1E12 - The Conversation", "Risk Management":"S2E1 - Risk Management", "Dead Cat Bounce":"S2E2 - Dead Cat Bounce", "Optimal Play":"S2E3 - Optimal Play", "The Oath":"S2E4 - The Oath", "Currency":"S2E5 - Currency", "Indian Four":"S2E6 - Indian Four", "Victory Lap":"S2E7 - Victory Lap", "The Kingmaker":"S2E8 - The Kingmaker", "Sic Transit Imperium":"S2E9 - Sic Transit Imperium", "With or Without You":"S2E10 - With or Without You", "Golden Frog Time":"S2E11 - Golden Frog Time", "Ball in Hand":"S2E12 - Ball in Hand", "Tie Goes to the Runner":"S3E1 - Tie Goes to the Runner", "The Wrong Maria Gonzalez":"S3E2 - The Wrong Maria Gonzalez", "A Generation Too Late":"S3E3 - A Generation Too Late", "Hell of a Ride":"S3E4 - Hell of a Ride", "Flaw in the Death Star":"S3E5 - Flaw in the Death Star", "The Third Ortolan":"S3E6 - The Third Ortolan", "Not You, Mr. Dake":"S3E7 - Not You, Mr. Dake", "All the Wilburys":"S3E8 - All the Wilburys", "Icebreaker":"S3E9 - Icebreaker", "Redemption":"S3E10 - Redemption", "Kompenso":"S3E11 - Kompenso", "Elmsley Count":"S3E12 - Elmsley Count", "Chucky Rhoades's Greatest Game":"S4E1 - Chucky Rhoades's Greatest Game", "Arousal Template":"S4E2 - Arousal Template", "Chickentown":"S4E3 - Chickentown", "Overton Window":"S4E4 - Overton Window", "A Proper Sendoff":"S4E5 - A Proper Sendoff", "Maximum Recreational Depth":"S4E6 - Maximum Recreational Depth", "Infinite Game":"S4E7 - Infinite Game", "Fight Night":"S4E8 - Fight Night", "American Champion":"S4E9 - American Champion", "New Year's Day":"S4E10 - New Year's Day", "Lamster":"S4E11 - Lamster", "Extreme Sandbox":"S4E12 - Extreme Sandbox", "The New Decas":"S4E1 - The New Decas", "The Chris Rock Test":"S5E2 - The Chris Rock Test", "Beg, Bribe, Bully":"S5E3 - Beg, Bribe, Bully", "Opportunity Zone":"S5E4 - Opportunity Zone", "Contract":"S5E5 - Contract", "The Nordic Model":"S5E6 - The Nordic Model", "The Limitless Shit":"S5E7 - The Limitless Shit", "Copenhagen":"S5E8 - Copenhagen", "Implosion":"S5E9 - Implosion", "Liberty":"S5E10 - Liberty", "Victory Smoke":"S5E11 - Victory Smoke", "No Direction Home":"S5E12 - No Direction Home", "Cannonade":"S6E1 - Cannonade", "Lyin' Eyes":"S6E2 - Lyin' Eyes", "STD":"S6E3 - STD", "Burn Rate":"S6E4 - Burn Rate", "Rock of Eye":"S6E5 - Rock of Eye", "Hostis Humani Generis":"S6E6 - Hostis Humani Generis", "Napoleon's Hat":"S6E7 - Napoleon's Hat", "The Big Ugly":"S6E8 - The Big Ugly", "Hindenburg":"S6E9 - Hindenburg", "Johnny Favorite":"S6E10 - Johnny Favorite", "Succession":"S6E11 - Succession", "Cold Storage":"S6E12 - Cold Storage"}

# get all files from directory

def get_files(directory):
    files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            files.append(os.path.join(root, file))
    return files

# main function
if __name__ == "__main__":
    # get first commandline argument
    directory = sys.argv[1]
    print(directory)
    # get all files from directory
    files = get_files(directory)
    print(files)
    # for file in files:
    #     # check if key from dict is in file name
    #     # get filename

