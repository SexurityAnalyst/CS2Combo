import requests

def get_steam_ids(item_id, category_id, exterior_id):
    page = 1
    steam_ids = []

    while True:
        url = f"https://float.skinport.com/api/assets?page={page}&item_id={item_id}&category_id={category_id}&exterior_id={exterior_id}"
        print(url)

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if "data" in data and isinstance(data["data"], list):
                for item in data["data"]:
                    if "owner" in item and isinstance(item["owner"], dict) and "steamid" in item["owner"]:
                        steam_id = item["owner"]["steamid"]
                        steam_ids.append(steam_id)

                page += 1

                # Check if we have reached the end of data
                if data == {"meta":{"count": None},"data":[]}:
                    print("No more data for item_id", item_id)
                    break
            else:
                print("Invalid JSON response format.")
                break
        else:
            print(f"Failed to retrieve the webpage for item_id {item_id} and page {page}. Status code:", response.status_code)
            break

    return steam_ids

def get_gloves_options():
    print("Gloves Options:")
    print("exteriorId=2 is Factory New")
    print("exteriorId=3 is Minimal Wear")
    print("exteriorId=4 is Field Tested")
    print("exteriorId=5 is Well-Worn")
    print("exteriorId=6 is Battle Scarred")

    exterior_id = int(input("Enter exterior id: "))  # Updated prompt for gloves

    return exterior_id

# User input for item selection
item_choice = input("Choose an item (1 for Knife, 2 for Gloves): ")

if item_choice == "1":  # Knife
    item_id = int(input("Enter item_id for Knife: "))
    category_id = int(input("Enter category (1 for Statrak, 3 for Normal): "))
    exterior_id = int(input("Enter exterior_id (2 for Factory New, 3 for Minimal Wear): "))
    filename = "knife.txt"
else:  # Gloves
    item_id = int(input("Enter item_id for Gloves: "))
    category_id = 3  # Default to Normal for Gloves
    exterior_id = get_gloves_options()
    filename = "gloves.txt"

# Get Steam IDs based on user input
steam_ids = get_steam_ids(item_id, category_id, exterior_id)

# Save Steam IDs to a file
with open(filename, 'w') as file:
    for steam_id in steam_ids:
        file.write(f"{steam_id}\n")

print(f"All Steam IDs for item_id {item_id}, category {category_id}, and exterior {exterior_id} are saved to {filename}.")
