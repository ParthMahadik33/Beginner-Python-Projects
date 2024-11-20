#using dict datatype to assign price with Order
menu={"pasta":80,
      "pizza":100,
      "burger":100,
      "frankie":60,
      "coffee":40,
      "ramen":100
      }
total=0
for items,price in menu.items():
    print(f"{items}:{price}")
while True:
    item=input("Place your order from our menu: ").strip().lower()
    if item in menu:
        total+=menu[item]
        print(f"Your order for {item} is placed. Current Total: {total}") 
    else:
        print(f"Your order for {item} is not in our menu!")
    new = input("Do you want to add to your order (Yes/No): ").strip().lower()
    if new !="yes":
      break
print("\nThank You for visiting Parth's Restaurant") 
print(f"Your Bill for the day is: {total}")   
