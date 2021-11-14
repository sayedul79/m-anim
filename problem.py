from manim import *
import numpy as np
config.background_color="#3d3d3d"
class IntroScene(Scene):
    def construct(self):
        theta=ValueTracker(0)
    
        axes=Axes(x_range=[0, 6.2*PI, PI/4], axis_config={"color": BLUE}).add_coordinates()
        x_lab=axes.get_x_axis_label(label=MathTex(r"\omega t", color=GREEN), 
                                    edge=RIGHT, direction=RIGHT, buff=0.1)
        y_lab=axes.get_y_axis_label(label=MathTex(r"V(t)", color=GREEN), 
                                    edge=UL, direction=UP, buff=0.1)
        graph=always_redraw(lambda:axes.plot(lambda omega_t: 2*np.cos(omega_t+theta.get_value()), 
                         x_range=[0, 6*PI, PI/100], color=RED))
        self.add(axes, x_lab, y_lab, graph)
        self.play(theta.animate.set_value(3*PI/2), run_time=3)