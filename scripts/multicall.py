import brownie
from brownie import Contract, interface

def price(link):
    pricing = Contract.from_abi(
        "Hello",
        link,
        interface.AggregatorV3Interface.abi,
    )
    return pricing

def masterlist(listing):

    dictt = dict()
    masterlst = {
        "USDC/ETH":"0x986b5E1e1755e3C2440e960477f25201B0a8bbD4",
        "BTC/USD":"0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c",
        "BUSD/ETH":"0x614715d2Af89E6EC99A233818275142cE88d1Cfd",
        "CTSI/ETH":"0x0a1d1b9847d602e789be38B802246161FFA24930",
        "DAI/ETH":"0x773616E4d11A78F511299002da57A0a94577F1f4"
        }
    for i in range(len(listing)):
        _tmp = list(masterlst.keys())[i]
        __tmp = {_tmp:masterlst[_tmp]}
        dictt.update(__tmp)
    return dictt
    

def main():
    _inputer = input("Enter the numbers you want to check: \n0. USDC/ETH\n1. BTC/USD\n2. BUSD/ETH\n3. CTSI/ETH\n4. DAI/ETH\n")
    inputer = _inputer.replace(" ", "")
    listingg_ = list(inputer)
    lst = masterlist(listingg_)
    result = []
    brownie.multicall(address="0x5BA1e12693Dc8F9c48aAD8770482f4739bEeD696")
    with brownie.multicall:
        for i in range(len(lst)):
            keyyy = list(lst.keys())[i]
            price_feed = price(lst[keyyy])
            round_data = price_feed.getRoundData(price_feed.latestRoundData()[0])[1]
            _tmp_dict = {keyyy:round_data}
            result.append(_tmp_dict)
    print(result)





