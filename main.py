from web3 import Web3
from beem.steem import Steem
from beembase import operations
from beem.transactionbuilder import TransactionBuilder
import time
import logging

nodes="https://api.steemit.com"


player="eth.gas"
key = "5KT1q"
s = Steem(node=nodes, keys=[key])

def upupup(total_missed):
    try:
        op = []
        transfers = {
            'from': player,
            'to': player,
            'amount': "0.001 STEEM",
            'memo': "GAS：%s" % str(total_missed)
        }
        op.append(operations.Transfer(**transfers))
        tx = TransactionBuilder(steem_instance=s)
        tx.appendOps(op)
        tx.appendSigner(player, "active")
        tx.sign()
        tx.broadcast()
        e=tx
    except Exception as e:
        print(e)
    return e

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/9aa3d56161'))
fromadd = Web3.toChecksumAddress("0xDeE245EbB9C4A9553CE1579b7412Eb6E223daAA3")
payload = {
        'from': "0x6c9938f889ca996d7ab1dcb11c6d605c53f0538c",
        'to': "0x6c9938f889ca996d7ab1dcb11c6d605c53f0538c",
        'data': "0x"
    }
try:
    gas=int(w3.fromWei(w3.eth.gasPrice, 'gwei'))
    print("gas:",gas)
    upupup(gas)
    time.sleep(600)
except Exception as e:
    print(e)
    time.sleep(600)
