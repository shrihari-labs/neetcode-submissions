class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            match op:
                case '+':
                    last_item = stack[-1]
                    sum_value = stack[len(stack) - 1] + stack[len(stack) - 2]
                    stack.append(sum_value)
                case 'D':
                    last_item = stack[-1]
                    stack.append(last_item * 2)
                case 'C':
                    stack.pop()
                case _:
                    stack.append(int(op))
        return sum(stack)


        