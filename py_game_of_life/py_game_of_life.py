import os
import time


class PyGameOfLife:
    def __init__(self):
        self.alive = 1
        self.dead = 0
        self.clear = lambda: os.system('clear')
        self.x_axis_length = 10
        self.y_axis_length = 10
        self.cycle_count = 0
        self.board = self.initialize_board(self.dead)

    def run(self):
        self.clear()
        self.place_glider()
        self.print_screen()
        input('Press return to continue.')

        try:
            while True:
                self.calculate_life()
                self.clear()
                self.print_screen()
                self.cycle_count += 1
                time.sleep(0.125)
        except KeyboardInterrupt:
            pass

        return 0

    def place_glider(self):
        self.board[0][2] = self.alive
        self.board[1][2] = self.alive
        self.board[2][2] = self.alive
        self.board[2][1] = self.alive
        self.board[1][0] = self.alive

    def calculate_life(self):
        next_board = self.initialize_board(self.dead)

        for y_coordinate in range(0, self.y_axis_length):
            for x_coordinate in range(0, self.x_axis_length):
                field = self.get_field(x_coordinate, y_coordinate)

                living_neighbors = self.count_living_neighbours(
                    x_coordinate,
                    y_coordinate
                )

                if field == self.alive:
                    if living_neighbors is 2 or living_neighbors is 3:
                        result = self.alive
                    else:
                        result = self.dead
                else:
                    if living_neighbors == 3:
                        result = self.alive
                    else:
                        result = self.dead

                next_board[y_coordinate][x_coordinate] = result

        self.board = next_board

    def print_screen(self):
        output = 'Cycle: ' + str(self.cycle_count) + '\n'
        line_count = 0

        for row in self.board:
            for element in row:
                output += str(element)

            line_count += 1

            if line_count is not self.y_axis_length:
                output += '\n'

        print(output)

    def get_field(self, x_coordinate, y_coordinate):
        if x_coordinate < 0:
            x_coordinate += self.x_axis_length
        elif x_coordinate >= self.x_axis_length:
            x_coordinate -= self.x_axis_length

        if y_coordinate < 0:
            y_coordinate += self.y_axis_length
        elif y_coordinate >= self.y_axis_length:
            y_coordinate -= self.y_axis_length

        return self.board[y_coordinate][x_coordinate]

    def initialize_board(self, initial_value):
        new_list = []

        for row in range(self.y_axis_length):
            new_list.append([initial_value] * self.x_axis_length)

        return new_list

    def count_living_neighbours(self, x_coordinate, y_coordinate):
        count = 0

        if self.get_field(x_coordinate + 1, y_coordinate + 1) is self.alive:
            count += 1

        if self.get_field(x_coordinate + 1, y_coordinate - 1) is self.alive:
            count += 1

        if self.get_field(x_coordinate - 1, y_coordinate - 1) is self.alive:
            count += 1

        if self.get_field(x_coordinate - 1, y_coordinate + 1) is self.alive:
            count += 1

        if self.get_field(x_coordinate, y_coordinate + 1) is self.alive:
            count += 1

        if self.get_field(x_coordinate, y_coordinate - 1) is self.alive:
            count += 1

        if self.get_field(x_coordinate + 1, y_coordinate) is self.alive:
            count += 1

        if self.get_field(x_coordinate - 1, y_coordinate) is self.alive:
            count += 1

        return count
