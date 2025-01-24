menu = {
"pizza" : 120,
"dosa"  : 200,
"pasta" : 34,
"coke"  : 20,    
}
bill = 0 
bill_detail = {}
print("welcome to code taj restrurent")
for key in menu:
    print(key.ljust(15), "-",menu[key])
while True:
    order = input("enter the item name that you want to order or type DONE for end ")
    if order == "DONE":
         break
    elif order in menu:
        quantity = int(input("enter the quantity of "))
        bill_detail[order]= quantity
    else:
        print("this item i not avilable in shop")
for item in bill_detail:
    item_cost = bill  + (bill_detail[item]* menu[item])   
    bill = item_cost  
    print(f"{item.ljust(10)}\t {bill_detail[item]}\t {item_cost}")
print("your bill=" , bill)   
print("bill with gst =" , bill + ((18/100)*bill))
print("THANKS YOU TO VISI OUR RESTRURENT COME AGAIN")         
