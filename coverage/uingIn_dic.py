
# using 'in' in dictionaries

available_parts = {
    "1" : "computers",
    "2" : "monitor",
    "3" : "keyboard",
    "4" : "mouse",
    "5" : "hdmi port",
    "6" : "hard disk"
 }

customer_choice = ""
while customer_choice != "0":
    if customer_choice in available_parts:   
        choce = available_parts[customer_choice]
        print(f"adding {choce}")
    else:
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")
    customer_choice = input("> ")
    


        
    
