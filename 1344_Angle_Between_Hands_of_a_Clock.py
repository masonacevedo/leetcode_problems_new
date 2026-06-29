class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minuteAngle = (minutes/60)*360
        hourAngle = (hour/12)*360

        hourAngle += ((minutes/60)/12)*360
        
        if hourAngle > 360:
            hourAngle -= 360
        
        greaterAngle = max(hourAngle, minuteAngle)
        smallerAngle = min(hourAngle, minuteAngle)

        if greaterAngle - smallerAngle < 180:
            return greaterAngle - smallerAngle
        else:
            return 360 - (greaterAngle - smallerAngle)

s = Solution()

hour = 3
minutes = 15

ans = s.angleClock(hour, minutes)
print("ans:", ans)