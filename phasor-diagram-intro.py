from manim import *
import numpy as np
config.background_color="#3d3d3d"
class IntroScene(Scene):
    def construct(self):
        theta=ValueTracker(0)
        amplitude=ValueTracker(1)
    
        axes=Axes(x_range=[0, 6.2*PI], axis_config={"color": BLUE}).add_coordinates()
        x_lab=axes.get_x_axis_label(label=MathTex(r"\omega t", color=GREEN), 
                                    edge=RIGHT, direction=RIGHT, buff=0.1)
        y_lab=axes.get_y_axis_label(label=MathTex(r"V(t)", color=GREEN), 
                                    edge=UL, direction=UP, buff=0.1)
        graph=always_redraw(lambda:axes.plot(lambda omega_t: amplitude.get_value()*np.cos(omega_t+theta.get_value()), 
                         x_range=[0, 6*PI, 0.01], color=RED))
        angle = DecimalNumber(theta.get_value(), num_decimal_places=1, unit="^{\circ}", font_size=40)\
            .add_updater(lambda a: a.set_value(theta.get_value()*180/PI))\
                .set_color(YELLOW)
         
        magnitude = DecimalNumber(amplitude.get_value(), num_decimal_places=1, font_size=40, color=BLUE)\
                    .add_updater(lambda a: a.set_value(amplitude.get_value()))
        text=MathTex(r"cos(\omega t", r"-", r" )")
        graph_lab=VGroup(magnitude,text[0], text[1], angle, text[2])\
            .arrange_submobjects(RIGHT, buff=0.3).to_edge(UP).scale(1.5)
        phas_lab=VGroup(magnitude.copy(),MathTex(r"\angle"), angle.copy())\
            .arrange_submobjects(RIGHT, buff=0.1).to_edge(DOWN-np.array([0,1,0]))
         
        self.add(axes, graph, graph_lab, x_lab, y_lab, phas_lab)
        self.play(theta.animate.set_value(3*PI/2), run_time=4)
        self.wait()
        self.play(amplitude.animate.set_value(3), run_time=3)
        self.wait()