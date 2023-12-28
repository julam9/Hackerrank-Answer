##Handshake
# Objective : Given n people at a party, find minimum nuber of handshake so every people shake hands exactly one time with other
def handshake(n):
    #number of sum of handshake with n-1 people because every people does not shake hand with themselves
    return sum(range(n))
#testing
handshake(11000)