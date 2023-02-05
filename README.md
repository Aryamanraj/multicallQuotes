# README

This is a simple script that retrieves price data from a list of selected cryptocurrencies from a smart contract on the Ethereum network. 

## Prerequisites
The script requires the following to be installed:
- [Brownie](https://brownie.readthedocs.io/en/stable/index.html)

## Usage
To use this script, follow the steps below:
1. Clone or download the repository.
2. Open the terminal and navigate to the repository folder.
3. Run `main()` in the terminal to retrieve the price data.

## Code Breakdown
The code contains three functions:
- `price(link)` takes a link as an argument and returns a smart contract instance of the AggregatorV3Interface using the ABI in the code.
- `masterlist(listing)` takes a list of integers as an argument and returns a dictionary of the selected cryptocurrencies and their corresponding contract addresses.
- `main()` is the main function that prompts the user to select cryptocurrencies from a list. It uses the `multicall` function from Brownie to retrieve the price data from the selected contracts, and stores the result in a list of dictionaries. The result is then printed.

## Conclusion
This script can be used as a starting point for retrieving price data from smart contracts on the Ethereum network using Brownie.