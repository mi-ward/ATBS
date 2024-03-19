inv = {'arrow': 12,
        'gold coin': 42,
        'rope': 1,
        'torch': 6,
        'dagger': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inv):    
    inv_total = str(sum(inv.values()))
    print("Inventory:")
    for k, v in inv.items():
        print(str(v) + " " + k)
    print("Total number of items: " + inv_total)

def addToInventory(inv, newItems):
    for k in newItems:
        inv.setdefault(k, 0)
        inv[k] += 1

displayInventory(inv)

addToInventory(inv, dragonLoot)

displayInventory(inv)

