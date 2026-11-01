class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        minutes = []
        total = 60 * 24

        for i in timePoints:
            minutes.append(int(i[0:2]) * 60 + int(i[3:5]))

        minutes.sort()

        answer = total + minutes[0] - minutes[-1]

        for i in range(1, len(minutes)):
            answer = min(answer, minutes[i] - minutes[i-1])

        return answer