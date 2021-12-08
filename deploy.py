import solcx
import json
from web3 import Web3
from dotenv import load_dotenv
from solcx import compile_standard
import os
load_dotenv()

solcx.install_solc("0.6.0")
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# compile solcx

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)



# get byte compiled_code
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

#abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]['abi']

#print(abi)

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
chain_id = 1337
my_address = '0xE23DeAd453e235595745635C6b7BdF363689B0df'
private_key = os.getenv('PRIVATE_KEY')



SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

#get latest nonce
nonce = w3.eth.getTransactionCount(my_address)

#build a transaction
#sign a transaction
#send a transaction

transaction = SimpleStorage.constructor().buildTransaction({'chainId':chain_id,'from':my_address,'nonce':nonce})

#signed_txn = w3.eth.account(sign_transaction(transaction,private_key= private_key))

print(transaction)
