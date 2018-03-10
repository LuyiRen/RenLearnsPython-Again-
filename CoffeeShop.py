#implements use of list and simple loops
#demonstrates use of string format as well

#this is a simple program that takes the price of the listed amount of coffee
#and then spits out the price with tax included.
coffee = {
    "Macchiato":3.40,
    "White Chocolate Macha":2.50,
    "Pomegranate Green Tea":3.20,
    }

def print_title():
    print("%-20s \t\t %-25s" %("Items: ", "Price: "))
    count=0
    for items in coffee:
        count+=1
        print("%-2s %-20s \t\t %-20.2f" %(count,items,coffee[items]))
        

def main():
    total = 0;
    price = {}
    count=0
    for items in coffee:
        count+=1
        price[count] = coffee[items]

    while(True):
        print("Welcome to Ren's Coffee shop, what would you like?")
        print_title()
        user = input("What would you like to buy? put 99 for exit")
        if(user.isdigit):
            if(int(user) > len(coffee)):
               break
            else:
                total = total + price[int(user)]
        else:
            break
    print("Your total is: %.2f" %(float(total*1.85)))
    
main()
