item_dic = {"Bubblegum": 202,
            "Toffee": 118,
            "Ice cream": 2250,
            "Milk chocolate": 1680,
            "Doughnut": 1075,
            "Pancake": 80
            }

def item_sum():
    add_items = 0
    for items in item_dic.values():
        add_items += items
    return add_items

def print_items_and_cost():
    print("Earned amount:")
    for item_name in item_dic.keys():
        price = item_dic[item_name]
        print(f"{item_name}: ${price}")

def net_income(income):
    print("Staff expenses")
    staff = int(input())
    print("Other expenses:")
    other = int(input())
    print(f"Net income: ${income- (other+staff)}")

print_items_and_cost()
print(f"Income: {item_sum()}")
net_income(item_sum())
