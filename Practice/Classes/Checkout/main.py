import item
from cart import Cart
from item import Item

cart_owner_name ="default"
def set_up_cart():
    global cart
    cart_owner_name = input('What is your name\n')
    cart = Cart(cart_owner_name)
    # print(cart.owner_name)
    
def add_items_to_cart():
    anything_else = "yes"
    while anything_else == "yes":
        add_item_to_cart()
        anything_else = input('Anything else? \n').lower()
    
def add_item_to_cart():
    item_name = input('What did '+ cart.owner_name + ' buy?\n')
    item_price = float(input('How much ' + item_name + ' cost?\n'))
    item_quantity = int(input('How many ' + item_name + ' did' + cart.owner_name + " buy?\n"))
    item = Item(item_name, item_price, item_quantity)
    cart.add(item) 
    

def display_invoice():
    print(cart)
    print('Your total bill is ' + str(cart.calculate_total_price()))

if __name__ == '__main__':
    set_up_cart()
    # add_item_to_cart()
    add_items_to_cart()
    display_invoice()
