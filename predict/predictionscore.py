#prediction score defined as worst possible actual correct prediction ability with at least 90% chance of getting at least correct/total
from scipy import stats

n = 100
k = 57
plist = [x * 0.005 for x in range(0, 200)]
for p in plist:
    prob = stats.binom.cdf(k,n,p)
    #print("chance of getting at least " +str(k) +"/"+ str(n), k, prob)
    print("actual prob " + str(p), "chance of getting more than " +str(k) +"/"+ str(n), k, prob)
