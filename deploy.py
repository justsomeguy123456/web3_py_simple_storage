import solcx
import json
from web3 import Web3

solcx.install_solc("0.6.0")
from solcx import compile_standard

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
chain_id = 5777
my_address = '0xefF08Fd8F707080E0C7C812e19aFcd32Aa682c46'
private_key = '0xa3a90e031748ff4a5d8933cfc5363f098cfd8ba496ed249ccf7fc167552bc1e3'


SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

print(SimpleStorage)
