#Rithvika Kathroju
#Mrs.Mansi - ICS 2O1 - 12/9/2020
#Unit 2: Introduction to Programming with Python - Final Assignment

"""
Intializing variables for each of the combos to store the the individual prices. I created the combo prices to provide
the customers with a cheaper option and better deal. Calculated prices by adding the specific burger price, fries price,
and medium drink price together --- and then subtracted $0.58. Calculated this seperatly not include in code!

"""
beef_combo_price = 4.49
chicken_combo_price = 4.99
veggie_combo_price = 4.29

"""
Intializing variables for the individual burgers to store the prices. Note - Created the veggie burger option and made a
random but reasonable price.
"""
beef_burger_price = 2.99
chicken_burger_price = 3.49
veggie_burger_price = 2.79
double_burger_price = 3.99
triple_burger_price = 4.99

# Intializing variables for the various sides to store the prices
sides_fries_price = 1.29
sides_salad_price = 1.89
sides_mashed_potatos_price = 1.99
sides_baked_potatos_price = 1.89

# Variable to store all the different drinks. Used the syntax for new line and the star symbol so that it can be printed as a list when called
drinks_type = "\n  ✸ Coke\n  ✸ 7UP\n  ✸ Diet Coke\n  ✸ Diet 7UP\n  ✸ Iced Tea\n  ✸ Apple Juice\n  ✸ Orange Juice\n"

# Intializing variables to store the prices of the drinks size
drinks_small_price = 0.69
drinks_medium_price = 0.79
drinks_large_price = 0.99

# Heading 1 - BURGER SHACK
print("==============================================================================================")
print("                                   ✸✸𝐁𝐔𝐑𝐆𝐄𝐑 𝐒𝐇𝐀𝐂𝐊✸✸")
print("==============================================================================================")

# Introduction
print("Hi, Welcome to Burger Shack. My name’s Rithvika and I’ll be your online server for today!")

# Prompting the user to enter their name on a new line and storing it in the variable user_name.
user_name = input("\nMay I know your name please?: ")
"""
Providing the user with the menu. I concatenated the strings/variables together because i did not want to
use commas. If i used commas, spaces will be automatically inserted.
"""
print("Nice to meet you " + user_name + ", Here is our menu!")

# Heading 2 - MENU
print("\n==============================================================================================")
print("                                       ✸✸𝐌𝐄𝐍𝐔✸✸")
print("==============================================================================================")

"""
Intializing variables to store the original price of the 3 items in the combo option. These are the
prices one would pay if they were to buy the items seperatly and WITHOUT the combo deal.
"""
beef_no_combo_deal = beef_burger_price + sides_fries_price + drinks_medium_price
chicken_no_combo_deal = chicken_burger_price + sides_fries_price + drinks_medium_price
veggie_no_combo_deal = veggie_burger_price + sides_fries_price + drinks_medium_price

# Subheading 1 - COMBOS
print("----------------------------------------------------------------------------------------------")
print("🍱 𝐂𝐎𝐌𝐁𝐎𝐒 🍱")
print("----------------------------------------------------------------------------------------------")
print("Your choice of burger, fries, and any medium sized drink!\n")

# Displays the prices for the combos using the variable.
print("Beef Combo: $" + str(beef_combo_price))
# Concatenated using + signs and typecasted variable to a str since it is float
# Shows the user how much they save and formatted to 2 decimal places. Did not typcast since the formatting automatically converts to a string
print("  ✸ You save $:" + '{:.2f}'.format(beef_no_combo_deal - beef_combo_price))

print("Chicken Combo: $" + str(chicken_combo_price))
print("  ✸ You save $:" + '{:.2f}'.format(chicken_no_combo_deal - chicken_combo_price))

print("Veggie Combo: $" + str(veggie_combo_price))
print("  ✸ You save: $" + '{:.2f}'.format(veggie_no_combo_deal - veggie_combo_price))


# Subheading 2 - BURGERS
print("----------------------------------------------------------------------------------------------")
print("🍔 𝐁𝐔𝐑𝐆𝐄𝐑𝐒 🍔")
print("----------------------------------------------------------------------------------------------")

# Displays the prices for the burgers. Used concatenation and typcasted to str
print("Beef Burger: $" + str(beef_burger_price))
print("Chicken Burger: $" + str(chicken_burger_price))
print("Veggie Burger: $" + str(veggie_burger_price))
print("Double Burger: $" + str(double_burger_price))
print("Triple Burger: $" + str(triple_burger_price))

# Subheading 3 - SIDES
print("----------------------------------------------------------------------------------------------")
print("🍟 𝐒𝐈𝐃𝐄𝐒 🍟")
print("----------------------------------------------------------------------------------------------")

# Displays the prices for the sides. Used concatenation and typcasted to str
print("Fries: $" + str(sides_fries_price))
print("Salad: $" + str(sides_salad_price))
print("Mashed Potatos: $" + str(sides_mashed_potatos_price))
print("Baked Potatos: $" + str(sides_baked_potatos_price))

# Subheading 4 - DRINKS
print("----------------------------------------------------------------------------------------------")
print("🥤 𝐃𝐑𝐈𝐍𝐊𝐒 🥤")
print("----------------------------------------------------------------------------------------------")

# Displays the different types of drinks by calling the variable. Used comma since it was more efficent
print("Types of Drinks:", drinks_type)

# Displays the prices for the drinks size. Used concatenation and typcasted to str
print("Small: $" + str(drinks_small_price))
print("Medium: $" + str(drinks_medium_price))
print("Large: $" + str(drinks_large_price))

# Subheading 5 - EATING ON A BUDGET
print("----------------------------------------------------------------------------------------------")
print("💰 𝐄𝐀𝐓𝐈𝐍𝐆 𝐎𝐍 𝐀 𝐁𝐔𝐃𝐆𝐄𝐓 💰")
print("----------------------------------------------------------------------------------------------")
# Displays the prices for the cheapest items on the menu. This is calculated using the min() function.
print("Cheapest Items On The Menu:")
print("🍱 𝐂𝐎𝐌𝐁𝐎𝐒 🍱: Veggie Combo: $" + str(min(beef_combo_price, chicken_combo_price, veggie_combo_price)))
print("🍔 𝐁𝐔𝐑𝐆𝐄𝐑𝐒 🍔: Veggie Burger: $" + str(min(beef_burger_price, chicken_burger_price, veggie_burger_price, double_burger_price, triple_burger_price)))
print("🍟 𝐒𝐈𝐃𝐄𝐒 🍟: Fries: $" + str(min(sides_fries_price, sides_salad_price, sides_mashed_potatos_price, sides_baked_potatos_price)))
print("🥤 𝐃𝐑𝐈𝐍𝐊𝐒 🥤: Small: $" + str(min(drinks_small_price, drinks_medium_price, drinks_large_price)))
print("----------------------------------------------------------------------------------------------")



# Heading 3 - PLEASE MAKE YOUR SELECTION BELOW
print("==============================================================================================")
print("                         ✸✸𝐏𝐋𝐄𝐀𝐒𝐄 𝐌𝐀𝐊𝐄 𝐘𝐎𝐔𝐑 𝐒𝐄𝐋𝐄𝐂𝐓𝐈𝐎𝐍 𝐁𝐄𝐋𝐎𝐖✸✸")
print("==============================================================================================")

# Subheading 6 - COMBOS
print("----------------------------------------------------------------------------------------------")
print("🍱 𝐂𝐎𝐌𝐁𝐎𝐒 🍱")
print("----------------------------------------------------------------------------------------------")

# Prompts the user to enter the number of beef, chicken and veggie combos they like to order
# The str is typecasted to be an int for future calculations and stored in seperate variables
user_combo_beef = int(input("How many beef combos would you like?: "))
'''
If the number of combos they entered for that specific type is greater than or equal to 1, it will prompt the user
to enter THAT many type of medium sized drinks. Otherwise, nothing will be prompted but instead it will store
"No Combo Drinks" in a variable for future use.
'''
if user_combo_beef >= 1:
    beef_combo_user_drink = input("Please enter the " + str(user_combo_beef) + " type(s) of drinks you would like: ")
else:
    beef_combo_user_drink = "No Combo Drinks"

# Same logic as stated above
user_combo_chicken = int(input("How many chicken combos would you like?: "))
if user_combo_chicken >= 1:
    chicken_combo_user_drink = input("Please enter the " + str(user_combo_chicken) + " type(s) of drinks you would like: ")
else:
    chicken_combo_user_drink = "No Combo Drinks"

user_combo_veggie = int(input("How many veggie combos would you like?: "))
if user_combo_veggie >= 1:
    veggie_combo_user_drink = input("Please enter the " + str(user_combo_veggie) + " type(s) of drinks you would like: ")
else:
    veggie_combo_user_drink = "No Combo Drinks"

user_num_combos = user_combo_beef + user_combo_chicken + user_combo_veggie


# Subheading 7 - BURGERS
print("----------------------------------------------------------------------------------------------")
print("🍔 𝐁𝐔𝐑𝐆𝐄𝐑𝐒 🍔")
print("----------------------------------------------------------------------------------------------")

# Prompts the user to enter the number of beef, chicken, veggie, double and triple burgers they would like to order
# The str is typecasted to be an int for future calculations and stored in seperate variables
user_num_beef_burger = int(input("How many beef burgers would you like?: "))
user_num_chicken_burger =int(input("How many chicken burgers would you like?: "))
user_num_veggie_burger =int(input("How many veggie burgers would you like?: "))
user_num_double_burger = int(input("How many double burgers would you like?: "))
user_num_triple_burger = int(input("How many triple burgers would you like?: "))

# Subheading 8 - SIDES
print("----------------------------------------------------------------------------------------------")
print("🍟 𝐒𝐈𝐃𝐄𝐒 🍟")
print("----------------------------------------------------------------------------------------------")

# Prompts the user to enter the number of sides(fries, salads, mashed potatos and baked potatos) they would like to order
# The str is typecasted to be an int for future calculations and stored in seperate variables
user_num_fries = int(input("How many orders of fries would you like?: "))
user_num_salad = int(input("How many orders of salads would you like?: "))
user_num_mashed_potatos = int(input("How many orders of mashed potatos would you like?: "))
user_num_baked_potatos = int(input("How many orders of baked potatos would you like?: "))

# Subheading 9 - DRINKS
print("----------------------------------------------------------------------------------------------")
print("🥤 𝐃𝐑𝐈𝐍𝐊𝐒 🥤")
print("----------------------------------------------------------------------------------------------")

# Prompts the user to enter the drink size(small, medium and large) and the type of drink they want
# The str is typecasted to be an int for future calculations and stored in seperate variables
user_num_small_drinks = int(input("How many small sized drinks would you like?: "))

"""
If the user enters a value greater than or equal to 1, it will prompt the user to enter THAT many types
of drinks they want in that specific size. Otherwise, nothing will be prompted but instead it will store
"No Drinks" in a variable for future use.
"""
if user_num_small_drinks >= 1:
    user_small_drinks_types = input("Please enter the " + str(user_num_small_drinks) + " type(s) of small drinks you would like: ")
else:
    user_small_drinks_types = "No Drinks"

# Same logic as stated above
user_num_medium_drinks = int(input("How many medium sized drinks would you like?: "))
if user_num_medium_drinks >= 1:
    user_medium_drinks_types = input("Please enter the " + str(user_num_medium_drinks) + " type(s) of medium drinks you would like: ")
else:
    user_medium_drinks_types = "No Drinks"

user_num_large_drinks = int(input("How many large sized drinks would you like?: "))
if user_num_large_drinks >= 1:
    user_large_drinks_types = input("Please enter the " + str(user_num_large_drinks) + " type(s) of large drinks you would like: ")
else:
    user_large_drinks_types = "No Drinks"

print("----------------------------------------------------------------------------------------------")

# Heading 4 - ORDER CONFIRMATION
print("==============================================================================================")
print("                              ✸✸𝐎𝐑𝐃𝐄𝐑 𝐂𝐎𝐍𝐅𝐈𝐑𝐌𝐀𝐓𝐈𝐎𝐍✸✸")
print("==============================================================================================")

# Displays the item name and quanity for each option the user had entered. I used commas instead of concatanation
print("You selected:")

# Subheading 10 - Combos
print("----------------------------------------------------------------------------------------------")
print("🍱 𝐂𝐎𝐌𝐁𝐎𝐒 🍱")
print("----------------------------------------------------------------------------------------------")
print(user_num_combos, "Combo(s)")
print(user_combo_beef, "Beef Combo(s)     --- Types:", beef_combo_user_drink)
print(user_combo_chicken, "Chicken Combo(s)  --- Types:", chicken_combo_user_drink)
print(user_combo_veggie, "Veggie Combo(s)   --- Types:", veggie_combo_user_drink)

# Subheading 11 - Burgers
print("----------------------------------------------------------------------------------------------")
print("🍔 𝐁𝐔𝐑𝐆𝐄𝐑𝐒 🍔")
print("----------------------------------------------------------------------------------------------")
print(user_num_beef_burger, "Beef Burger(s)")
print(user_num_chicken_burger, "Chicken Burger(s)")
print(user_num_veggie_burger, "Veggie Burger(s)")
print(user_num_double_burger, "Double Burger(s)")
print(user_num_triple_burger, "Triple Burger(s)")

# Subheading 12 - Sides
print("----------------------------------------------------------------------------------------------")
print("🍟 𝐒𝐈𝐃𝐄𝐒 🍟")
print("----------------------------------------------------------------------------------------------")
print(user_num_fries, "Order(s) of Fries")
print(user_num_salad, "Order(s) of Salad(s)")
print(user_num_mashed_potatos, "Order(s) of Mashed Potatos")
print(user_num_baked_potatos, "Order(s) of Baked Potatos")

# Subheading 13 - Drinks
print("----------------------------------------------------------------------------------------------")
print("🥤 𝐃𝐑𝐈𝐍𝐊𝐒 🥤")
print("----------------------------------------------------------------------------------------------")
print(user_num_small_drinks, "Small Drinks  --- Types:", user_small_drinks_types)
print(user_num_medium_drinks, "Medium Drinks --- Types:", user_medium_drinks_types)
print(user_num_large_drinks, "Large Drinks  --- Types:", user_large_drinks_types)
print("----------------------------------------------------------------------------------------------")


"""
Calculates the total cost for each combo option using it's respective price and the number of items the user enters.
Stored it as a float and did NOT round or format because I will do that later on. I will format when the variable is
being used
"""
combo_beef_total_cost = float(beef_combo_price * user_combo_beef)
combo_chicken_total_cost = float(chicken_combo_price * user_combo_chicken)
combo_veggie_total_cost = float(veggie_combo_price * user_combo_veggie)

# Calculates the total cost for the different burgers using it's respective price and the number of items the user enters.
# Typecasted it as a float
beef_burger_total_cost = float(beef_burger_price * user_num_beef_burger)
chicken_burger_total_cost = float(chicken_burger_price * user_num_chicken_burger)
veggie_burger_total_cost = float(veggie_burger_price * user_num_veggie_burger)
double_burger_total_cost = float(double_burger_price * user_num_double_burger)
triple_burger_total_cost = float(triple_burger_price * user_num_triple_burger)

# Calculates the total cost for the sides using it's respective price and the number of items the user enters
# Typecasted it as a float
fries_total_cost = float(sides_fries_price * user_num_fries)
salads_total_cost = float(sides_salad_price * user_num_salad)
mashed_potatos_total_cost = float(sides_mashed_potatos_price * user_num_mashed_potatos)
baked_potatos_total_cost = float(sides_baked_potatos_price * user_num_baked_potatos)

"""
Calculates the total cost for each of the drinks, according to it's size, using it's respective price
and number of items the user enters. Typecasted it as a float
"""
small_drinks_total_cost = float(drinks_small_price * user_num_small_drinks)
medium_drinks_total_cost = float(drinks_medium_price * user_num_medium_drinks)
large_drinks_total_cost = float(drinks_large_price * user_num_large_drinks)


# Calculates the total cost for all of the combos, burgers, sides and drinks seperately to make code more efficent and simpler to read
# Typecasted it as a float
combo_total_cost = float(combo_beef_total_cost + combo_chicken_total_cost + combo_veggie_total_cost)
burger_total_cost = float(beef_burger_total_cost + chicken_burger_total_cost + veggie_burger_total_cost + double_burger_total_cost + triple_burger_total_cost)
sides_total_cost = float(fries_total_cost + salads_total_cost + mashed_potatos_total_cost + baked_potatos_total_cost)
drinks_total_cost = float(small_drinks_total_cost + medium_drinks_total_cost + large_drinks_total_cost)


# This is the receipt so that the user can see their total costs. They will pay later  on
# Heading 5 - RECEIPT
print("==============================================================================================")
print("                                     ✸✸𝐑𝐄𝐂𝐄𝐈𝐏𝐓✸✸")
print("==============================================================================================")
print("Burger Shack Fast Food Restaurant")
print("        18 Queen St. East")
print("      Brampton, ON. L6Z 3F8")

# Prints the server and customer's name
print("\nServer: Rithvika")
print("Customer:", user_name, "\n")

"""
Displays the receipt of the order with the item name, quantity and price for the individual,
it also formats the price to 2 decimal places.

If an item is greater than or equal to 1, it will print out the number of orders for that specfic dish,
the dish name, and the total cost for that type of dish formatted to 2 decimal places.

Used concatenation and typecasted where necessary
"""
# Combos - This also prints out the type of drinks it ordered
if user_num_combos >= 1:
    print(str(user_num_combos) + " Combo(s)                  $" + '{:.2f}'.format(combo_total_cost))
if user_combo_beef >= 1:
    print("     " + str(user_combo_beef) + " Beef Combo(s)        $" + '{:.2f}'.format(combo_beef_total_cost))
    print("     With: " + beef_combo_user_drink)
if user_combo_chicken >= 1:
    print("     " + str(user_combo_chicken) + " Chicken Combo(s)     $" + '{:.2f}'.format(combo_chicken_total_cost))
    print("     With: " + chicken_combo_user_drink)
if user_combo_veggie >= 1:
    print("     " + str(user_combo_veggie) + " Veggie Combo(s)      $" + '{:.2f}'.format(combo_veggie_total_cost))
    print("     With: " + veggie_combo_user_drink)

# Burgers
if user_num_beef_burger >= 1:
    print("\n" + str(user_num_beef_burger) + " Beef Burger(s)            $" + '{:.2f}'.format(beef_burger_total_cost))
if user_num_chicken_burger >= 1:
    print(str(user_num_chicken_burger) + " Chicken Burger(s)         $" + '{:.2f}'.format(chicken_burger_total_cost))
if user_num_veggie_burger >= 1:
    print(str(user_num_veggie_burger) + " Veggie Burger(s)          $" + '{:.2f}'.format(veggie_burger_total_cost))
if user_num_double_burger >= 1:
    print(str(user_num_double_burger) + " Double Burger(s)          $" + '{:.2f}'.format(double_burger_total_cost))
if user_num_triple_burger >= 1:
    print(str(user_num_triple_burger) + " Triple Burger(s)          $" + '{:.2f}'.format(triple_burger_total_cost))

# Sides
if user_num_fries >= 1:
    print("\n" + str(user_num_fries) + " Fries                     $" + '{:.2f}'.format(fries_total_cost))
if user_num_salad >= 1:
    print(str(user_num_salad) + " Salad(s)                  $" + '{:.2f}'.format(salads_total_cost))
if user_num_mashed_potatos >= 1:
    print(str(user_num_mashed_potatos) + " Mashed Potatos            $" + '{:.2f}'.format(mashed_potatos_total_cost))
if user_num_baked_potatos >= 1:
    print(str(user_num_baked_potatos) + " Baked Potatos             $" + '{:.2f}'.format(baked_potatos_total_cost))

# Drinks - This also prints out the type of drinks it ordered
if user_num_small_drinks >= 1:
    print("\n" + str(user_num_small_drinks) + " Small Drinks              $" + '{:.2f}'.format(small_drinks_total_cost))
    print("     " + str(user_small_drinks_types))
if user_num_medium_drinks >= 1:
    print(str(user_num_medium_drinks) + " Medium Drinks             $" + '{:.2f}'.format(medium_drinks_total_cost))
    print("     " + str(user_medium_drinks_types))
if user_num_large_drinks >= 1:
    print(str(user_num_large_drinks) + " Large Drinks              $" + '{:.2f}'.format(large_drinks_total_cost))
    print("     " + str(user_large_drinks_types))

#Intialize the tax variable as a constant
TAX = 0.13


# Calculates the subtotal for the users selected menu items and rounds to 2 decimal places
# Used round() function instead of formatting it because it will keep it as a float. I need it as a float to calculate the total cost!
# This adds up the 4 different types of sections in my menu. Recall that each variable stores the total costs for that specific section from the menu
user_subtotal = round(combo_total_cost + burger_total_cost + sides_total_cost + drinks_total_cost, 2)

# Calculates the total tax cost of the entire order using the subtotal and the constant variable tax, it rounds the cost to 2 decimal places
# it first multiplies the user subtotal to the 13% tax. Then it rounds to 2 decimal places and stores it in the variable called user_tax_cost.
# you need to multiply the subtotal by the decimal form of the tax because you are trying to find the amount of dollars from the subtotal that is equivalent
user_tax_cost = round(user_subtotal * TAX, 2)

# Displays the subtotal and the total tax of the order by formating both to 2 decimal places
print("----------------------------------------------------------------------------------------------")
print("SUBTOTAL: $" + '{:.2f}'.format(user_subtotal))
print("TAX: $" + '{:.2f}'.format(user_tax_cost))
print("----------------------------------------------------------------------------------------------")

# Prompts the user to donate money to the Canadian Caner Society or make a tip if they choose to do so
user_donations = float(input("How much would you like to donate to the Canadian Cancer Society? $"))
user_tips = float(input("How much would you like to tip? $"))

# Calculates the total cost of the order using the subtotal, total tax, donations and tip.
# Adds everything together and rounds to 2 decimal places
user_total_cost = round(user_subtotal + user_tax_cost + user_donations + user_tips, 2)

# Displays the total cost of the entire order by formating to 2 decimal places
print("----------------------------------------------------------------------------------------------")
print("TOTAL: $" + '{:.2f}'.format(user_total_cost))
print("==============================================================================================")

# Prompts the user to select a way to pay for the order either by credit card, cash or gift card
payment_method = input("How would you like to pay? ('Credit Card', 'Cash', or 'Gift Card') : ")

print("***TRANSACTION SUCCESSFUL***")



# Heading 6 - RECEIPT - CUSTOMER COPY
print("==============================================================================================")
print("                            ✸✸𝐑𝐄𝐂𝐄𝐈𝐏𝐓 - 𝐂𝐔𝐒𝐓𝐎𝐌𝐄𝐑 𝐂𝐎𝐏𝐘✸✸")
print("==============================================================================================")
print("Burger Shack Fast Food Restaurant")
print("      18 Queen St. East")
print("     Brampton, ON. L6Z 3F8")

print("\nServer: Rithvika")
print("Customer:", user_name, "\n")

"""
Displays the entire copy of the order made by the user including the item name, quantity, and
total price for the number of items they ordered, formatted to 2 decimal places.

I typecasted the variables to a string so that I can concatenate it using plus sign, I did not use
commas because it automatically adds spaces between each item.

I did not typecast the total cost for each item because the '{:.2f}'.format() syntax automatically converts it to a string


If an item is greater than or equal to 1, it will print out the number of orders for that specfic dish,
the dish name, and the total cost for that type of dish formatted to 2 decimal places.

Used concatenation and typecasted where necessary
"""
# Combos
if user_num_combos >= 1:
    print(str(user_num_combos) + " Combo(s)                  $" + '{:.2f}'.format(combo_total_cost))
if user_combo_beef >= 1:
    print("     " + str(user_combo_beef) + " Beef Combo(s)        $" + '{:.2f}'.format(combo_beef_total_cost))
    print("     With: " + beef_combo_user_drink)
if user_combo_chicken >= 1:
    print("     " + str(user_combo_chicken) + " Chicken Combo(s)     $" + '{:.2f}'.format(combo_chicken_total_cost))
    print("     With: " + chicken_combo_user_drink)
if user_combo_veggie >= 1:
    print("     " + str(user_combo_veggie) + " Veggie Combo(s)      $" + '{:.2f}'.format(combo_veggie_total_cost))
    print("     With: " + veggie_combo_user_drink)

# Burgers
if user_num_beef_burger >= 1:
    print("\n" + str(user_num_beef_burger) + " Beef Burger(s)            $" + '{:.2f}'.format(beef_burger_total_cost))
if user_num_chicken_burger >= 1:
    print(str(user_num_chicken_burger) + " Chicken Burger(s)         $" + '{:.2f}'.format(chicken_burger_total_cost))
if user_num_veggie_burger >= 1:
    print(str(user_num_veggie_burger) + " Veggie Burger(s)          $" + '{:.2f}'.format(veggie_burger_total_cost))
if user_num_double_burger >= 1:
    print(str(user_num_double_burger) + " Double Burger(s)          $" + '{:.2f}'.format(double_burger_total_cost))
if user_num_triple_burger >= 1:
    print(str(user_num_triple_burger) + " Triple Burger(s)          $" + '{:.2f}'.format(triple_burger_total_cost))

# Sides
if user_num_fries >= 1:
    print("\n" + str(user_num_fries) + " Fries                     $" + '{:.2f}'.format(fries_total_cost))
if user_num_salad >= 1:
    print(str(user_num_salad) + " Salad(s)                  $" + '{:.2f}'.format(salads_total_cost))
if user_num_mashed_potatos >= 1:
    print(str(user_num_mashed_potatos) + " Mashed Potatos            $" + '{:.2f}'.format(mashed_potatos_total_cost))
if user_num_baked_potatos >= 1:
    print(str(user_num_baked_potatos) + " Baked Potatos             $" + '{:.2f}'.format(baked_potatos_total_cost))

# Drinks
if user_num_small_drinks >= 1:
    print("\n" + str(user_num_small_drinks) + " Small Drinks              $" + '{:.2f}'.format(small_drinks_total_cost))
    print("     " + str(user_small_drinks_types))
if user_num_medium_drinks >= 1:
    print(str(user_num_medium_drinks) + " Medium Drinks             $" + '{:.2f}'.format(medium_drinks_total_cost))
    print("     " + str(user_medium_drinks_types))
if user_num_large_drinks >= 1:
    print(str(user_num_large_drinks) + " Large Drinks              $" + '{:.2f}'.format(large_drinks_total_cost))
    print("     " + str(user_large_drinks_types))


"""
Displays the subtotal, tax, donations, tips, and total of the order made by the user, formatted to 2 decimal places.

I concatenated using plus signs because I did not want there to be spaces in between the dollar signs. (Note: spaces
are automatically inserted when using commas)
"""
print("----------------------------------------------------------------------------------------------")
print("SUBTOTAL: $" + '{:.2f}'.format(user_subtotal))
print("TAX: $" + '{:.2f}'.format(user_tax_cost))
print("DONATIONS: $" + '{:.2f}'.format(user_donations))
print("TIPS: $" + '{:.2f}'.format(user_tips))
print("----------------------------------------------------------------------------------------------")
print("TOTAL: $" + '{:.2f}'.format(user_total_cost))

# Payment statement
print("----------------------------------------------------------------------------------------------")
print("PAYMENT -", payment_method)
print("***TRANSACTION SUCCESSFUL***")
print("12/11/2020   18:34 --- Trans# - 34263456")

# Conclusion statement
print("==============================================================================================")
print("Thank you for dining at Burger Shack! Your order is being prepared and will be ready soon!")
user_rating = int(input("Please rate our service from 1-5 stars: "))
print("Thank you! Please give us a detailed feedback on our website at www.burgershackbrampton.ca!")
print("==============================================================================================")
