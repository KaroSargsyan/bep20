#!/usr/bin/python3
import os
from brownie import MyToken, accounts, network, config



def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    publish_source = True if os.getenv("ETHERSCAN_TOKEN") else False
    contract=MyToken.deploy({"from": dev}, publish_source=publish_source)
    return contract