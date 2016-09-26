#python2
import sys 


money = int(input())
coins = map(int,raw_input().strip().split(' '))

def recursive_change_naive(money,coins): 
	if money == 0: 
		return 0 
	min_num_coins = float("infinity")
	
	for i in range(0,len(coins)-1): 
		if money >= coins[i]: 
			num_coins = recursive_change_naive(money-coins[i],coins)
			if num_coins + 1 < min_num_coins:
				min_num_coins = num_coins + 1
	return min_num_coins

print recursive_change_naive(money,coins)