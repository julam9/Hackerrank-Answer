##Birthday Cake
# Return the freq of candles whose height is max height
def birthdayCakeCandles(candles):
    return candles.count(max(candles))
#testing
birthdayCakeCandles([2,3,4,5,5])