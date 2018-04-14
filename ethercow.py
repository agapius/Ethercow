import requests
import json

##### get the JSON code of the site #####
req1 = requests.get("https://www.bitstamp.net/api/v2/ticker/btceur/")
req2 = requests.get("https://www.bitstamp.net/api/v2/ticker/etheur/")

content1 = req1.content.decode("utf-8")
content2 = req2.content.decode("utf-8")

#########################################

loaded1 = json.loads(content1)
loaded2 = json.loads(content2)

btc = loaded1['last']
eth = loaded2['last']

#########################################


amount_eth = 100

output_wealth = (float(eth)*amount_eth)

#########################################
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
