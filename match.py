# Function to read Steam IDs from a file
def read_steam_ids_from_file(filename):
    steam_ids = set()
    with open(filename, 'r') as file:
        for line in file:
            steam_id = line.strip()
            if steam_id:
                steam_ids.add(steam_id)
    return steam_ids

# Read Steam IDs from both files
steam_ids_891 = read_steam_ids_from_file('knife.txt')
steam_ids_gloves = read_steam_ids_from_file('Gloves.txt')

# Find common Steam IDs
common_steam_ids = steam_ids_891.intersection(steam_ids_gloves)

# Print common Steam IDs with the correct URL format
for steam_id in common_steam_ids:
    print(f"Common Steam ID: https://steamcommunity.com/profiles/{steam_id}")