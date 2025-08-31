from strategies.easy import Easy
from strategies.normal import Normal


class TicTacToe():
    def __init__(self, level='easy'):
        self.field = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
# BEGIN (write your solution here)
        self.level = level

    def go(self, *args):
        if len(args) == 0 and self.level == "easy":
            cell = Easy.find_none_cell(self.field)
            self.field[cell[0]][cell[1]] = False
        elif len(args) == 0 and self.level == "normal":
            cell = Normal.find_none_cell(self.field)
            self.field[cell[0]][cell[1]] = False
        elif len(args) >= 2:
            self.field[args[0]][args[1]] = True
        else:
            raise ValueError("Недостаточно аргументов.")

        return self.check_field()

    def checking_lines(self):
        # checking_lines
        for row in self.field:
            if row[0] is not None and row[0] == row[1] == row[2]:
                return True

    def checking_columns(self):
        # checking_columns
        for col in range(3):
            if self.field[0][col] is not None and self.field[0][col] ==\
                    self.field[1][col] == self.field[2][col]:
                return True

    def checking_main_diagonal(self):
        # checking_main_diagonal (слева направо)
        if self.field[0][0] is not None and self.field[0][0] ==\
                self.field[1][1] == self.field[2][2]:
            return True

    def checking_side_diagonal(self):
        # checking_side_diagonal (справа налево)
        if self.field[0][2] is not None and self.field[0][2] ==\
                self.field[1][1] == self.field[2][0]:
            return True

    def check_field(self):

        if self.checking_lines():
            return True
        elif self.checking_columns():
            return True
        elif self.checking_main_diagonal():
            return True
        elif self.checking_side_diagonal():
            return True

        return False


# !решение ментора
# ?BEGIN (write your solution here)
    #     if level == 'easy':
    #         self.strategy = Easy()
    #     if level == 'normal':
    #         self.strategy = Normal()

    # def go(self, row=None, col=None):
    #     if row is None and col is None:
    #         row, col = self.strategy.get_next_step(self.field)
    #         self.field[row][col] = 'AI'
    #         return self.is_winner('AI')

    #     self.field[row][col] = 'Player'
    #     return self.is_winner('Player')

    # def is_winner(self, type):
    #     horizontal = self.field
    #     vertical = list(map(list, zip(*horizontal)))
    #     diagonal1 = [self.field[0][0], self.field[1][1], self.field[2][2]]
    #     diagonal2 = [self.field[2][0], self.field[1][1], self.field[0][2]]

    #     for row in horizontal:
    #         if self.has_player_placed_all_the_marks(row, type):
    #             return True

    #     for column in vertical:
    #         if self.has_player_placed_all_the_marks(column, type):
    #             return True

    #     if self.has_player_placed_all_the_marks(diagonal1, type):
    #         return True
    #     if self.has_player_placed_all_the_marks(diagonal2, type):
    #         return True

    #     return False

    # def has_player_placed_all_the_marks(self, row, type):
    #     return all(value == type for value in row)
# ?END
