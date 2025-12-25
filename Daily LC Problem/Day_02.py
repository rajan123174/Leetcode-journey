# Maximize Happiness of Selected Children
class Solution :
    def maximumHappinessSum(self, happiness, k):
        happiness.sort(reverse=True)
        total = 0
        for i in range (k):
            gain = happiness[i]-i
            if gain >0:
                total += gain
            else:
                break
        return total

happiness = [1, 2, 3, 4, 5]
k = 3
obj = Solution()
last = obj.maximumHappinessSum(happiness , k)
print(last)