def display_inventory(inventory: dict) -> None:
    print('Items in inventory:')
    total_items = 0
    for k, v in inventory.items():
        total_items += v
        print(v, k)
    print('\nTotal items: ', total_items)


def add_to_inventory(inventory: dict, loot: list) -> dict:
    for item in loot:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'ruby', 'gold coin', 'gold coin', 'ruby', 'goober', 'dooby', 'dooby']
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)
