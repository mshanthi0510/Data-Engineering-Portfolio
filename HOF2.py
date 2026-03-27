def pricing_calculator(tax):
    def calculate_total(baseprice):
        total = baseprice+(baseprice*tax)
        return total
    return calculate_total

NY_Menu_list = {"Latte" :60,"Espresso":50,"Cold Brew":70}
TX_Menu_list = {"Latte" :67,"Espresso":55,"Cold Brew":78}

NY_Menu_TAX = {"Latte" :0.08,"Espresso":0.05,"Cold Brew":0.2}
TX_Menu_TAX = {"Latte" :0.1,"Espresso":0.09,"Cold Brew":0.1}

#Latte Price calculator
ny_pricing_LT = pricing_calculator(NY_Menu_TAX["Latte"]) #pricing_calculator(0.08)
tx_pricing_LT = pricing_calculator(TX_Menu_TAX["Latte"])

#Espresso Price calculator
ny_pricing_ESP = pricing_calculator(NY_Menu_TAX["Espresso"])
tx_pricing_ESP = pricing_calculator(TX_Menu_TAX["Espresso"])

#Cold Brew Price Calculator
ny_pricing_CB = pricing_calculator(NY_Menu_TAX["Cold Brew"])
tx_pricing_CB = pricing_calculator(TX_Menu_TAX["Cold Brew"])

print(f"NY Latte Price is :{ny_pricing_LT(NY_Menu_list["Latte"])}") #ny_pricing_LT(60)
print(f"TX Latte price is : {tx_pricing_LT(TX_Menu_list["Latte"])}")

print(f"NY Espresso Price is :{ny_pricing_ESP(NY_Menu_list["Espresso"])}")
print(f"TX Espresso price is : {tx_pricing_ESP(TX_Menu_list["Espresso"])}")

print(f"NY Espresso Price is :{ny_pricing_ESP(NY_Menu_list["Cold Brew"])}")
print(f"TX Espresso price is : {tx_pricing_ESP(TX_Menu_list["Cold Brew"])}")
