#  Set #2 Bonus Project : The ??????? resturant      # <-- title partly hidden by glare
#
################################################################################

#Crate my variables
Dots = '.' * 100
SalesTax = ?          # <-- HIDDEN BY GLARE
Item1 = ?             # <-- HIDDEN (pattern suggests 1)
Item2 = ?             # <-- HIDDEN (pattern suggests 2)
Item3 = 4
Item4 = 8
Item5 = 16
Item6 = 32
Item7 = 64
Item8 = 128
Item9 = 256
Item10 = 512

#Ask for name
PersonName = input('Please enter your first name: ')

#Create menu to person
print('Welcome',PersonName,'to the disaster resturant!')

#Display Menu
print('Here is our expenisve menu!')

print('-'*125)
print('1. Hamburgers..........',Dots,'$',Item1)
print('2. Fries...............',Dots,'$',Item2)
print('3. Onion Rings.........',Dots,'$',Item3)
print('4. Juice...............',Dots,'$',Item4)
print('5. HamburgerMeal.......',Dots,'$',Item5)
print('6. SpicyFries..........',Dots,'$',Item6)
print('7. SpicyHamburger......',Dots,'$',Item7)
print('8. 30pcChickenNuggets..',Dots,'$',Item8)
print('9. GiantMilkshake......',Dots,'$',Item9)
print('10. GIANTHAMBURGER(WatchOut).....',Dots,'$',Item10)
print('-'*125)

#Purchase
Purchase_Item = int(input('Please enter the item you would like to purchase: '))

if Purchase_Item == 1:
    print('Hamburger, The tasty burger mmmm')
    num_Item = int(input('How many do you want to purchase?: '))
    Cost = Item1 * num_Item
    Finalprice = SalesTax + Cost

elif Purchase_Item == 2:
    print('Fries, So Saltyy')
    num_Item = int(input('How many do you want to purchase?: '))
    Cost = Item2 * num_Item
    Finalprice = SalesTax + Cost

elif Purchase_Item == 3:
    print('Onion Rings, Artificial')
    num_Item = int(input('How many do you want to purchase?: '))
    Cost = Item3 * num_Item
    Finalprice = SalesTax + Cost

elif Purchase_Item == 4:
    print('Juice, Made from real meat!')
    num_Item = int(input('How many do you want to purchase?: '))
    Cost = Item4 * num_Item
    Finalprice = SalesTax + Cost

elif Purchase_Item == 5:
    print('HamburgerMeal, for big boy')
    num_Item = int(input('How many do you want to purchase?: '))
    Cost = Item5 * num_Item
    Finalprice = SalesTax + Cost

elif Purchase_Item == 6:
    print('Spicy Fries, 1000000 Scoville!')
    num_Item = int(input('How many do you want to purchase?: '))
    Cost = Item6 * num_Item
    Finalprice = SalesTax + Cost

elif Purchase_Item == 7:
    print('SPicyHamburger, 500mil scovillle!!!!')
    num_Item = int(input('How many do you want to purchase?: '))
    Cost = Item7 * num_Item
    Finalprice = SalesTax + Cost

elif Purchase_Item == 8:
    print('30pcChickenNuggets, Maybe too much?')
    num_Item = int(input('How many do you want to purchase?: '))
    Cost = Item8 * num_Item
    Finalprice = SalesTax + Cost

elif Purchase_Item == 9:
    print('GiantMilkshake, Wont give you a brainFreeze, itll give 10!')
    num_Item = int(input('How many do you want to purchase?: '))
    Cost = Item9 * num_Item
    FinalPrice = SalesTax + Cost      # <-- capital P here in the original, unlike every other branch

elif Purchase_Item == 10:
    print('GIANTHAMBURGER, Too big for anyoneeee!20 Pounds!')
    num_Item = int(input('How many do you want to purchase?: '))
    Cost = Item10 * num_Item
    Finalprice = SalesTax + Cost

else:
    print('That is not a item on the list')
    Cost = 0

print('Your Sales Tax comes out to $',SalesTax,)
print('Your total comes out to $',Cost,)
print('Your grand total comes out to $',Finalprice,)
