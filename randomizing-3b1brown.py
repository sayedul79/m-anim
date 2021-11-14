from manim import *
import random
class Randomising(Scene):
    def construct(self):
        def randomize(number):
            value = random.uniform(0, 1)
            number.set_value(value)
            if value > 0.5:
                number.set_color(BLUE_D)
            else:
                number.set_color(RED_C)

        number = DecimalNumber()

        self.add(number)
        self.play(UpdateFromFunc(number, randomize), run_time=3)
        self.wait(2)