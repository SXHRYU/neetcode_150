class Solution:
    def dailyTemperatures(self, temps):
        res = [] * len(temps)
        stack = [] # pair: [temp: index]

        for i, t in enumerate(temps):
            while stack and t > stack[-1][0]:
                stack_t, stack_ind = stack.pop()
                res[stack_ind] = (i - stack_ind)
            stack.append([t, i])
        return res
