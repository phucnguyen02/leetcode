class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for asteroid in asteroids:
            neg_destroyed = False
            while stack and asteroid < 0 < stack[-1] and not neg_destroyed:
                if -asteroid == stack[-1]:
                    stack.pop()
                    neg_destroyed = True
                elif -asteroid > stack[-1]:
                    stack.pop()
                else:
                    neg_destroyed = True

            if not neg_destroyed or asteroid >= 0:
                stack.append(asteroid)
        return stack
    
# If we see a negative asteroid and the top of the stack has a positive asteroid,
# we attempt to keep popping the stack until the negative asteroid is destroyed. However,
# if the negative asteroid destroys all of the positive asteroids then it is appended to the stack. If an asteroid is positive then it is added