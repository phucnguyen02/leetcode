class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        one_min_angle = 6
        one_hour_angle = 30
        
        minutes_angle = one_min_angle * minutes
        hour_angle = (hour % 12 + minutes / 60) * one_hour_angle
        
        diff = abs(hour_angle - minutes_angle)
        return min(diff, 360 - diff)
    
# For every minute, the minute hand goes on 6 degrees
# For every hour, it goes on 30 degrees ontop of the fraction of the minute hand divided by 60, to signify how far along it's gone in an hour.
# Return the absolute minimum difference, including 360 - diff.