QUARTER = -1 # Because quarters are going right
PENNY = 1 # Because pennies are going left
EMPTY = 0

class PuzzleGrid:
    def __init__(self, num_quarters, num_pennies):
        self.n = num_quarters
        self.m = num_pennies
        self.grid_size = self.m + self.n + 1
        # Quarters on the left, pennies on the right
        self.grid = [QUARTER] * self.n + [EMPTY] + [PENNY] * self.m
        self.initial_grid = list(self.grid)
        self.empty_index = self.n
        self.moves = []
        self.moves_per_turn = [0] * self.grid_size

        # Now solve itself
        self.__solve()

    def get_max_moves(self):
        # Maximum number of moves per turn
        return max(self.moves_per_turn)

    def get_num_moves(self):
        return (self.n * self.m) + self.n + self.m

    def get_num_turns(self):
        return self.grid_size

    # Try to jump the coin in the specified index
    def __jump(self, index):
        coin = self.grid[index]
        next_index = index - coin
        jump_index = next_index - coin # it's right
        # Next coin should be different, jump index should be empty
        if self.grid[jump_index] == EMPTY and self.grid[next_index] != coin:
            self.grid[jump_index] = coin
            self.grid[index] = EMPTY
            return True
        else:
            return False

    # Try to slide the coin in the specified index
    def __slide(self, index):
        # What's the coin in this index?
        coin = self.grid[index]
        next_index = index - coin # it's right
        if self.grid[next_index] == EMPTY:
            # We can move it, do so and return True
            self.grid[next_index] = coin
            self.grid[index] = EMPTY
            return True
        else:
            # We can't move it; return false
            return False

    def __can_slide(self, coin):
        try:
            index = self.empty_index + coin
            if index >= 0:
                return self.grid[index] == coin
            else:
                return False
        except IndexError:
            return False

    def __can_jump(self, coin):
        try:
            index = self.empty_index + coin
            other_index = index + coin
            if index >= 0 and other_index >= 0:
                return self.grid[index] != coin and self.grid[other_index] == coin
        except IndexError:
            return False

    def __move(self, coin_index, coin):
        # Add it to list of moves (list of tuples, from & to)
        self.moves.append((coin_index, self.empty_index))

        # Update the list of number of moves per turn
        self.moves_per_turn[self.turn_number] += 1

        self.grid[self.empty_index] = coin
        self.grid[coin_index] = EMPTY
        self.empty_index = coin_index

    def __jump(self, coin):
        # Assuming it can jump ...
        coin_index = self.empty_index + coin * 2
        self.__move(coin_index, coin)

    def __slide(self, coin):
        coin_index = self.empty_index + coin
        self.__move(coin_index, coin)

    def __still_has_moves(self, coin):
        # If it can slide or jump return true, else, false
        return self.__can_slide(coin) or self.__can_jump(coin)

    def __move_coin(self, coin):
        no_more_moves = False
        # While there are still valid moves, do stuff:
        while not no_more_moves:
            if self.__can_jump(coin):
                self.__jump(coin)
            elif self.__can_slide(coin):
                self.__slide(coin)
                # If we can move the other coin, keep stop moving this
                if self.__still_has_moves(-coin):
                    no_more_moves = True
            else:
                no_more_moves = True

    def print_grid(self):
        # Print that shit out
        for coin in self.grid:
            if coin == QUARTER:
                print "O",
            elif coin == PENNY:
                print "#",
            else:
                print " ",
        print 

    def __solve(self):
        coin = QUARTER
        for i in xrange(self.grid_size):
            self.turn_number = i
            # Move the coin, then switch turns
            self.__move_coin(coin)
            coin = -coin

    def print_analysis(self):
        print "%d vs %d, %d starts first:" % (self.n, self.m, self.n)
        self.print_grid()
        print "Afterwards, looks like:"
        self.print_grid()
        print "Moves per turn:"
        print self.moves_per_turn
