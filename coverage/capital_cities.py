countries = ('/home/aberhe/pythonMasterClass/coverage/data/country_info.txt')


coutries_loop = {}  
with open(countries) as file_number:
    for row in file_number:
        data = (row.strip('\n').split('|'))
        # print(data)
        coutry, capital, code, code3, dialing, timezone, currency = data
        coutry_dict = {
            'name' : coutry,
            'capital' : capital,
            'country_code' : code,
            'cc3' : code3,
            'dialing_code' : dialing,
            'timezone' : timezone,
            'currency' : currency,
        } 
        coutries_loop[code.casefold()] = coutry_dict
        coutries_loop[coutry.casefold()] = coutry_dict
while True:
 chosen_country = input(": ").casefold()
 if chosen_country in coutries_loop:
    country_data = coutries_loop[chosen_country]
    print(country_data['capital'])
    print(f"{country_data} no capital")
 elif chosen_country == "quit":
    break
    


        # for key, value in coutry_dict.items():
        #     print(f"{key} --- {value}")
    

            # while customer_choice != "0":
    #     if customer_choice == coutry:
    #         for x in coutry_dict:
    #           x['capital'] = {coutry}
    #     # result = coutry_dict[capital]
            

    #     customer_choice = input(": ")

        

        
            
    
    
        #     if customer_choice in coutry_dict:
        #         chosen = coutries_loop[customer_choice]
        #         if customer_choice == 'ca'

        

        
#         coutries_loop[coutry.casefold()] = coutry_dict
# print(coutries_loop)


        
