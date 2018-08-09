from blockcypher import get_transaction_details
from blockcypher import get_address_details
response = get_address_details('1DEP8i3QJCsomS4BSMY2RpU1upv62aGvhD')
print response
print "\n" + "\n"

#choose first transaction
transactions = response['txrefs']
tx = transactions[0]['tx_hash']
prevHash = transactions[0]['tx_hash']

for i in range(0, 50):
    tx = prevHash
    r = get_transaction_details(prevHash)
    try:
        prevHash = r['inputs'][0]['prev_hash']
        print prevHash
        print "\n" + "\n"
    except:
        break

#tx = coinbase transaction se nao limitar loop ate 50
print "COINBASE TRANSACTION"
print tx


#txsHashList = []
#for item in transactions:
    #txsHashList.append(item['tx_hash']) 

#for item in txsHashList:
    #r = get_transaction_details(item)
    #print r
    #print "\n" + "\n"


