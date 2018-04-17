import requests
import json

###### get the Info from Coinmarketcap Api ######

ethereum_dic = requests.get("https://api.coinmarketcap.com/v1/ticker/ethereum/?convert=EUR").json()[0]

eth_price=(ethereum_dic.get("price_eur"))

###### get the User's Info ######

amount_eth = 100

output_wealth = (float(eth_price)*amount_eth)

###### print ASCII Art Ethercow ######
print()
print("     /----------\\") 
print("   < ", round(output_wealth,2), "€", " >")
print("     \----------/")
print( """
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\\
                 ||----w |
                 ||     ||
    """)
