from manim import *
class MyAnimation(Scene):
    def construct(self):
        circle=Circle()
        circle.set_fill(YELLOW, opacity=0.6)
        self.play(Create(circle))
        self.wait()