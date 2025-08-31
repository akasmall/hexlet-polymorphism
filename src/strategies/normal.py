class Normal():
    # BEGIN (write your solution here)
    def find_none_cell(matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows - 1, -1, -1):
            for j in range(cols):
                if matrix[i][j] is None:
                    return (i, j)  # Возвращаем индекс найденной ячейки
        return None  # Если None не найдено
    # END

# !решение ментора
# ?BEGIN (write your solution here)
    # def get_next_step(self, field):
    #     for i in reversed(range(len(field))):
    #         row = field[i]
    #         if None in row:
    #             return [i, row.index(None)]
    #     return []
# ?END
