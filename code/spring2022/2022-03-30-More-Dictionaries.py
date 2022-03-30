from typing import *

# More examples
# You can use a dictionary to match zipcodes (as keys) to states (as value)
# zip_to_state_dict: Dict[int,str] = {72034: 'AR', 70461: 'LA', 72032: 'AR', 35433: 'AL'}

# To go the other way is a bit more complicated.  With very few exceptions, in the US
# any zipcode has only one state, but one state has *many* zipcodes

# state_to_zip_dict: Dict[str,List[int]] = {'AR' : [72032,72034,72211],'LA': [70461,70458]}

# Inventory manager for the cash register:

# inventory_dict -- will contain item name and price
#
# inv_file = open('store_inventory.txt','r')
# inventory_dict = {}
#
# for line in inv_file.readlines():
#     info = line.strip().split(',')
#     item_name = info[0]
#     item_price = float(info[1])
#     inventory_dict[item_name] = item_price
#
# inv_file.close()
#
# print(inventory_dict)

# given a list of tuples, return a dictionary, keyed on the tuple, with value the number of evens in the tuple:

# we could do this with a single function, we will use *two*
#
# def count_evens(tupl: Tuple[int]) -> int:
#     count = 0
#     for entry in tupl:
#         if entry %2 == 0:
#             count += 1
#     return count
#
# def dict_builder(lst: List[Tuple[int]]) -> Dict[Tuple[int],int]:
#     my_dict = {}
#     for item in lst:  # note that item is a Tuple of integers
#         my_dict[item] = count_evens(item)
#
#     return my_dict
#
# def main2():
#     tup1 = (5, 2, 4, 10, -5, 3)
#     tup2 = (3, 5, 7, 11)
#     tup3 = (2, 7, 4, 3)
#     tup4 = (1, 2, 3, 4, 5, 6)
#
#     my_list = [tup1, tup2, tup3, tup4]
#
#     my_dict = dict_builder(my_list)
#
#     print(my_dict)
#
# main2()

## Heap Tracing Example ##
#
def main1():
    my_list = [2, 3, 5]
    your_list = my_list
    my_dict = {'a' : 7, 'f' : 5}
    your_dict =  {'a' : 7, 'f' : 5}
    i = 0
    for key in my_dict:
        if my_dict[key] in my_list:
            my_dict[key] = 0
            my_list[i] = 17
        i += 1

    print(my_list)
    print(your_list)

    print(my_dict)
    print(your_dict)
    print(i)

#main1()




####### Bigger Data Example
## Given a data file in the form    zipcode;state;city;type;location_type
# Construct a dictionary of the form --    zipcode: [states]
# #

def zip_code1() -> Dict[str,List[str]]:
    zip_file = open('zipcodes.txt','r')
    zip_dict = {}
    header = True
    for line in zip_file.readlines():
        data = line.strip().split(';')
        if not header:
            zipc = data[0]
            state = data[1]
            city = data[2]
            zip_type = data[3]
            location_type = data[4]


            if zipc not in zip_dict:
                zip_dict[zipc] = []

            zip_dict[zipc].append(state)

        header = False

    zip_file.close()

    return zip_dict

## Now, let's flip this -- state: [zipcodes]

def zip_code2() -> Dict[str,List[str]]:
    zip_file = open('zipcodes.txt','r')
    zip_dict = {}
    header = True
    for line in zip_file.readlines():
        data = line.strip().split(';')
        if not header:
            zipc = data[0]
            state = data[1]
            city = data[2]
            zip_type = data[3]
            location_type = data[4]


            if state not in zip_dict:
                zip_dict[state] = []

            zip_dict[state].append(zipc)

        header = False

    zip_file.close()

    return zip_dict


## Finally, we could do: zipcode: [(city, state, type)]

def zip_code3() -> Dict[str,List[str]]:
    zip_file = open('zipcodes.txt','r')
    zip_dict = {}
    header = True
    for line in zip_file.readlines():
        data = line.strip().split(';')
        if not header:
            zipc = data[0]
            state = data[1]
            city = data[2]
            zip_type = data[3]
            location_type = data[4]

            
            if zipc not in zip_dict:
                zip_dict[zipc] = []

            zip_dict[zipc].append((city,state,zip_type))

        header = False

    zip_file.close()

    return zip_dict








#
# ###################################
# # Cash Register Example - again
# ###################################
#
def load_inventory() -> Dict[str, float]:
    inv_file = open('store_inventory.txt', 'r')
    inventory_dict = {}

    for line in inv_file.readlines():
        info = line.strip().split(',')
        item_name = info[0]
        item_price = float(info[1])
        inventory_dict[item_name] = item_price

    inv_file.close()

    return inventory_dict


def purchase_item(inventory_dict: Dict[str, float]) -> str:
    success = False
    while not success:
        item = input('What did you buy? ')
        if item in inventory_dict:
            return item
        else:
            print(f'We are sorry, but we do not have {item}')
            print(f'We have: {", ".join(inventory_dict.keys())}')


def str_input(prompt: str, valid_answers: List[str]) -> str:
    is_okay = False
    while not is_okay:
        answer = input(prompt)

        if answer in valid_answers:
            is_okay = True
        else:
            print("That is not a valid answer.")
            print(f'Valid answers are: {",".join(valid_answers)}.')

    return answer



def main():
    cash = 100.00
    items_sold = []
    done = False

    inventory_dict = load_inventory()


    while not done:

        print('Welcome to our store. What would you like to buy today?')
        print('We have the following available:')
        print(', '.join(inventory_dict.keys()))

        item_sold = purchase_item(inventory_dict)
        items_sold.append(item_sold)


        cash += inventory_dict[item_sold]


        cont = str_input('Would you like to purchase more items? (Yes/No)',['Yes','No'])
        if cont == 'No':
            done = True

    print(f'The register contains ${cash}')
    print(f'Today, we have sold: {", ".join(items_sold)}')






#main()