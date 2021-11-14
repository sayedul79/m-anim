from manim import *
import random
HOME2="D:\Extra Knowledge\Python\python-code"
class Randomising(Scene):
    def construct(self):
        def randomize(numbers):
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
        
# class MoreRandomising(Scene):
#     def construct(self):
        
#         numbers=VGroup()
#         for x in range(10):
#             num=DecimalNumber()
#             numbers.add(num)
#         numbers.arrange(RIGHT).to_edge(UP)
#         self.add(numbers)
        
#         def randomize_numbers(numbers):
#             for num in numbers:
#                 value=random.uniform(0,1)
#                 num.set_value(value)
#                 if value>0.2:
#                     num.set_color(GREEN)
#                 else:
#                     num.set_color(RED)
#         def get_results(numbers):
#             for num in numbers:
#                 if num.get_value()
class MoreRandomising(Scene):
    def construct(self):
        def randomize_numbers(numbers):
            for num in numbers:
                value = random.uniform(0, 1)
                num.set_value(value)
                if value > 0.2:
                    num.set_color(GREEN)
                else:
                    num.set_color(RED_C)

        def get_results(numbers):
            results = VGroup()
            for num in numbers:
                if num.get_value() > 0.2:
                    win = SVGMobject(f"{HOME2}\\check-mark.svg").set_color(GREEN)
                    win.set(height=0.4)
                    win.next_to(num, DOWN, buff=0.25)
                    und = Underline(win).match_color(win)
                    results.add(win, und)
                else:
                    loss = SVGMobject(f"{HOME2}\\cross-mark.svg").set_color(RED_C)
                    loss.set(height=0.4)
                    loss.next_to(num, DOWN, buff=0.25)
                    und = Underline(loss).match_color(loss)
                    results.add(loss, und)
            return results

        numbers = VGroup()
        for x in range(10):
            num = DecimalNumber()
            numbers.add(num)
        numbers.arrange(RIGHT).to_edge(UP)

        self.add(numbers)

        for k in range(2):
            self.play(UpdateFromFunc(numbers, randomize_numbers))
            results = get_results(numbers)
            self.play(Create(results))
            self.wait()
            self.play(FadeOut(results))
            self.wait(0.3)