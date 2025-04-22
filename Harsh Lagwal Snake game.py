import tkinter as tk
import random


class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")

        self.canvas = tk.Canvas(master, width=400, height=400, bg='black')
        self.canvas.pack()

        self.snake = [(20, 20), (20, 30), (20, 40)]
        self.direction = 'Down'
        self.food_position = self.place_food()
        self.score = 0

        self.master.bind("<Key>", self.change_direction)
        self.game_loop()

    def place_food(self):
        x = random.randint(0, 19) * 10
        y = random.randint(0, 19) * 10
        return (x, y)

    def change_direction(self, event):
        new_direction = event.keysym
        if new_direction in ['Up', 'Down', 'Left', 'Right']:
            self.direction = new_direction

    def game_loop(self):
        self.move_snake()
        self.check_collisions()
        self.draw_elements()
        self.master.after(100, self.game_loop)

    def move_snake(self):
        head_x, head_y = self.snake[0]

        if self.direction == 'Up':
            head_y -= 10
        elif self.direction == 'Down':
            head_y += 10
        elif self.direction == 'Left':
            head_x -= 10
        elif self.direction == 'Right':
            head_x += 10

        new_head = (head_x, head_y)
        self.snake.insert(0, new_head)

        if new_head == self.food_position:
            self.score += 1
            self.food_position = self.place_food()
        else:
            self.snake.pop()

    def check_collisions(self):
        head_x, head_y = self.snake[0]
        if (head_x < 0 or head_x >= 400 or
                head_y < 0 or head_y >= 400 or
                len(self.snake) != len(set(self.snake))):
            self.game_over()

    def draw_elements(self):
        self.canvas.delete(tk.ALL)
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill='green')
        food_x, food_y = self.food_position
        self.canvas.create_oval(food_x, food_y, food_x + 10, food_y + 10, fill='red')

    def game_over(self):
        self.canvas.create_text(200, 200, text="Game Over", fill="white", font=('Arial', 24))
        self.master.update()
        self.master.quit()


# Create the main window
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()