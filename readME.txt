brownie networks add "Binance Smart Chain" bsc_test_moralis host='https://speedy-nodes-nyc.moralis.io/c674d7ce50325c694fcece2e/bsc/testnet' name='Testnet(Moralis)' chainid=97 explorer='https://testnet.bscscan.com/'

brownie run scripts/deploy.py --network bsc_test_moralis
