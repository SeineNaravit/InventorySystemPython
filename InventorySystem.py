import random

itemdb = [
    {
    "id":0,
    "type":"item",
    "name":"Potion",
    "buy":25,
    "sell":10
     },
    {
    "id":1,
    "type":"item",
    "name":"Hi-Potion",
    "buy":50,
    "sell":25
     },
    {
    "id":2,
    "type":"weapon",
    "name":"Sword",
    "buy":100,
    "sell":80
     },
    {
    "id":3,
    "type":"weapon",
    "name":"Hammer",
    "buy":100,
    "sell":80
     },
    {
    "id":4,
    "type":"weapon",
    "name":"Spear",
    "buy":100,
    "sell":80
     },
    {
    "id":5,
    "type":"weapon",
    "name":"Mace",
    "buy":100,
    "sell":80
     },

]

inventory = []

def add_item(itemdb_id):
    try:
        item_added = itemdb[itemdb_id]["name"]
        print(f"DEBUG LOG : Added '{item_added}' to Inventory")
        inventory.append(itemdb_id)
    except IndexError: #Index out of range
        print("Invalid Item_ID : Please look at the item database table to get item id")
    except SyntaxError: #Invalid Syntax
        print("Syntax Error Please check your code")
    except Exception:
        print("Unknown Error")

def remove_item(itemdb_id):
    try:
        item_removed = itemdb[itemdb_id]["name"]
        print(f"DEBUG LOG : Removed '{item_removed}' from Inventory")
        inventory.remove(itemdb_id)
    except IndexError:
        print(f'Invalid Item_ID : Please look at the item database table to get item id')
    except ValueError:
        print(f'Dont Have Item ID{itemdb_id} in the list')

def inven_display(inventory = inventory):
    print(f"\n##########\nThis is your inventory\n")

    #Get Name of item
    inventory_as_name = []
    for item in inventory:
        name_of_item = itemdb[item]["name"]
        inventory_as_name.append(name_of_item)

    #Count name in list and display
    count_list = []
    for count_name in inventory_as_name:
        if count_name not in count_list:
            itemcount = inventory_as_name.count(count_name) # count item in count_name
            print(f"{count_name} x {itemcount}") # display name and quantity
            count_list.append(count_name) #add to count_list to not loop in here again

    print(f"\n##########\n")

def item_info(item_id = 999):
    try:
        item = itemdb[item_id]
        print(f"Item Id : {item['id']}\nName : {item['name']}\nType : {item['type']}\nBuy Price : {item['buy']}z.\nSell Price : {item['sell']}z.")
    except TypeError:
        print("No Item DB")
    except Exception:
        print("Please input Item ID in arguments EX: item_info(2)")

def id():
    print("")
    for item in itemdb:
        print(f'ID : {item["id"]} : {item["name"]}')

def add_item_random():
    try:
        random_id = random.randint(0,len(itemdb)-1)
        item_added = itemdb[random_id]["name"]
        print(f"DEBUG LOG : Added '{item_added}' to Inventory")
        inventory.append(random_id)
    except IndexError: #Index out of range
        print("Invalid Item_ID : Please look at the item database table to get item id")
    except SyntaxError: #Invalid Syntax
        print("Syntax Error Please check your code")
    except Exception:
        print("Unknown Error")

"""

This program Indicated Item as ID Number
if you wish to check all of item ID
please use command : id()

Commands:
add_item(id)        - Add Item Id in to inventory
add_item_random()   - Add Random Item to invetory
remove_item(id)     - Remove Item Id in your inventory
inven_display()     - Display your inventory
item_info(id)       - Get Item info
id()                - Check all Item ID

"""

is_running = True

print(("""
Inventory System Online

This program is an inventory system
you can add, remove, display item

Commands:
(1) add_item            - Add Item Id in to inventory
(2) add_item_random     - Add Random Item to inventory
(3) remove_item         - Remove Item Id in your inventory
(4) inven_display       - Display your inventory
(5) item_info           - Get Item info
(6) id                  - Check all Item ID
"""))

while is_running:
    command_input = input("Please select command ")

    if command_input == '1' and 'add_item':
        item_id = int(input('Please input Item ID'))
        add_item(item_id)

    elif command_input == '2' and 'add_item_random':
        add_item_random()

    elif command_input == "3" and "remove_item":
        item_id = int(input("Please input Item ID"))
        remove_item(item_id)

    elif command_input == "4" and "inven_display":
        inven_display()

    elif command_input == "5" and "item_info":
        item_id = int(input("Please input Item ID"))
        item_info(item_id)

    elif command_input == "6" and "id":
        id()

    else:
        print("Please select right command or right command number.")
