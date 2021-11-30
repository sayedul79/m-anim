from manim import *
import numpy as np
#https://github.com/visual-x/manim-projects/blob/main/2021/TrigFunc-Parameter-a.py
class DiscreteSin(Scene):
    def construct(self):
        self.x_min=0
        self.x_max=3*np.pi
        
        self.amplitude=ValueTracker(1)
        self.angular_velocity=ValueTracker(1)
        self.phase_shift=ValueTracker(0)
        self.offset=ValueTracker(0)
        
        a, omega, theta, c=self.amplitude, self.angular_velocity, self.phase_shift, self.offset
        
        function=MathTex("f(x)", "=", "A", "\\cdot" "\\sin", "\\big(", "\\omega", 
                         "\\cdot", "t", "+", "\\theta", "\\big)", "+", "c")\
                             .scale(1.5)\
                                 .to_edge(UP, buff=0)\
                                     .add_background_rectangle()
        
        function[3].set_color(RED)
        function[6].set_color(BLUE)
        function[10].set_color(YELLOW)
        function[-1].set_color(GREEN)
        
        self.axes=NumberPlane(x_range=[self.x_min, self.x_max], y_range=[-4,4], 
                              x_length=config.frame_width-1)
        arrows=always_redraw(lambda:self.get_arrows(a.get_value(), omega.get_value(), 
                               theta.get_value(), c.get_value()))
        
        self.play(DrawBorderThenFill(self.axes), run_time=2)
        self.play(*[GrowArrow(arrows) for arrows in arrows], run_time=1.5)
        self.add(arrows)
        self.play(a.animate(rate_func=squish_rate_func(smooth, 0.4, 1)).set_value(2),
                  theta.animate(rate_func=squish_rate_func(smooth, 0, 0.6)).set_value(PI/2),
                  run_time = 3)
        self.play(theta.animate.set_value(-2*PI), run_time=3)
        self.play(omega.animate(rate_func=squish_rate_func(smooth, 0, 0.65)).set_value(3), 
                  c.animate(rate_func=squish_rate_func(smooth, 0.4, 0.9)).set_value(-2), 
                  Create(function, rate_func=squish_rate_func(smooth, 0.65,1)),
                  run_time=3)
        
        self.play(AnimationGroup(*[Circumscribe(mob, fade_out=True) for mob in [function[3], 
                                                                      function[6],
                                                                      function[10], 
                                                                      function[-1]
                                                                      ]
                                   ], lag_ratio=0.2
                                 )
                  , run_time=3)
        self.wait(0.5)
        
        self.play(a.animate(rate_func=squish_rate_func(smooth, 0.4,1)).set_value(3), 
                  omega.animate(rate_func=squish_rate_func(smooth, 0.2,1)).set_value(1), 
                  theta.animate(rate_func=squish_rate_func(smooth, 0.2, 0.8)).set_value(0), 
                  c.animate(rate_func=squish_rate_func(smooth, 0, 0.6)).set_value(0), 
                  run_time=4)
        self.play(Circumscribe(function[3],run_time=2))
        self.play(a.animate.set_value(-2), run_time=2)
        self.wait(2)

    def get_arrows(self, a, omega, theta, c, **kwargs):
        arrows=VGroup()
        for t in np.arange(self.x_min, self.x_max, 2*PI/(omega*15)):
            start=self.axes.c2p(t,0)
            end=self.axes.c2p(t, a*np.sin(omega*t+theta)+c)
            arrow=Arrow(start, end, buff=0, max_tip_length_to_length_ratio = 0.15, 
                        color=YELLOW)
            arrows.add(arrow)
        return arrows
     