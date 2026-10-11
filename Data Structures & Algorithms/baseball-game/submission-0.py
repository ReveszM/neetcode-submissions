class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for cur_operation in operations:
            if cur_operation == '+':
                record.append(record[-1] + record[-2])
            elif cur_operation == 'D':
                record.append(2 * record[-1])
            elif cur_operation == 'C':
                record.pop()
            else:
                record.append(int(cur_operation))
        return sum(record)
        