import json
from web3 import Web3


chains = {'arbi':'',
          'opti':'',
          'bsc':'',
          'polygon':''}         #contact_stg, contract_dex, rpc

class stgBuyandStake:

    def __init__(self, chain, amount, privatekey):
        self.chain = chain
        self.n = amount
        self.privatekey = privatekey


    def buy_stg(self):
        w3 = Web3(Web3.HTTPProvider(chains[self.chain][2])
        account = w3.eth.account.from_key(self.privatekey)
        address = account.address



        #check stg on wallet and swap stg on sushiswap etc dexes

    def lock_stg(self)
        w3 = Web3(Web3.HTTPProvider(chains[self.chain][2])
        account = w3.eth.account.from_key(self.privatekey)
        address = account.address


        address_contract_stg = ''
        abi = json.loads('')
        contract_stg = w3.eth.contract(address = address_contract_stg, abi = abi_stg)