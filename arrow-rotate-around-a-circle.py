from manim import *
class ArrowRotate(Scene):
    def construct(self):
        theta = ValueTracker(PI/4)

        axis = NumberPlane().add_coordinates()

        arrow_Uabc= always_redraw(lambda:Arrow(axis.c2p(0, 0), axis.c2p(4.25*np.cos(theta.get_value()), 
                                                   4.25*np.sin(theta.get_value())), 
                          buff=0, color=RED))
    
        self.add(axis)
        self.play(GrowArrow(arrow_Uabc))
        self.wait()

        self.play(theta.animate.set_value(9*PI/4), run_time=4)
        self.wait()