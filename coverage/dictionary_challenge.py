



available_parts = {
    "1" : "computers",
    "2" : "monitor",
    "3" : "keyboard",
    "4" : "mouse",
    "5" : "hdmi port",
    "6" : "hard disk"
 }  


customer_choce = None
compiter_parts = {}
while customer_choce != "0":
    if customer_choce in available_parts:
        added_choice = available_parts[customer_choce]
        # extra_choice = compiter_parts[added_choice]
        # print(added_choice)
        if customer_choce in compiter_parts:
            print(f"removing {added_choice}")
            compiter_parts.pop(customer_choce)
            
        else:
            
            print(f"Adding {added_choice}")
            compiter_parts[customer_choce] = added_choice
        print(f"Your dictionary contains:  {added_choice}")
        for key, value in available_parts.items():
         print(key, value)
    customer_choce = input(">  ")
    