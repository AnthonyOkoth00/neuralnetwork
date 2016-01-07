import math

e = math.e

def identity(signals):

    # simple: f(x) = x
    return math.fsum(signals)

def logistic(signals):

    sum = math.fsum(signals)
    return ( 1/( 1 + math.pow( e, -1*sum) ) )

def gaussian(signals):

    sum = math.fsum(signals)
    return math.pow( e, -1 * sum^2 )