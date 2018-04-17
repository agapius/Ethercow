# Ethercow
CowSay the amount of crypto funds:

     /----------\
    <  133.700 € > 
     \----------/

        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                 ||---w |
                 ||    ||

### What it does:
  1. The script loads current prices for btc and eth from bitstamp using the requests library
  2. The loaded data is put into a JSON file using the JSON Python library
  3. The specific amount of BTC/ETH of the user is multiplied with the respective price to calculate total wealth
  4. An ASCII-Art ethercow with a speech bubble containing the total wealth in Eur is displayed

### How to use it:
  1. Edit script with personal amount of ether/btc
  2. Open script with terminal "python ethercow.py"
  
### ToDo:
  1. More pythonic code (e.g. the json conversion might be obsolete)
  2. Data from coinmarketcap DONE
  3. Source wealth data from personal public key
