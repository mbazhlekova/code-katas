package besttime

import "math"

func bestTimeToBuyAndSellStock(prices []int) int {
	minPrice, maxProfit := math.MaxInt32, 0
	for i := 0; i < len(prices); i++ {
		if prices[i] < minPrice {
			minPrice = prices[i]
		} else if prices[i] - minPrice > maxProfit {
			maxProfit = prices[i] - minPrice
		}
	}
	return maxProfit
}