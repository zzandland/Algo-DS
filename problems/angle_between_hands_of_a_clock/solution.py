class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # get min angle
        min_angle = 6 * minutes
        
        # get hr angle
        hr_angle = 30 * (hour if hour != 12 else 0)
        # get min offset
        hr_angle += 0.5 * minutes
        
        a, b = hr_angle - min_angle, min_angle - hr_angle
        if a < 0: a += 360
        if b < 0: b += 360
        return min(a, b)