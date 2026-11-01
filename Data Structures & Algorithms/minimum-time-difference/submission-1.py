class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes= []
        total = 60*24


        for i in timePoints:
            minutes.append(int(i[0:2])*60+int(i[3:5]))

        print(minutes)
        minutes.sort()
        res = total-minutes[-1]+minutes[0]
        for i in range(1, len(minutes)):
            res=min(res,minutes[i]-minutes[i-1])
        return res