from manim import *
class VectorRotate(Scene):
    def construct(self):
        theta=ValueTracker(PI/4)
        plane=NumberPlane()

        vect_1=always_redraw(lambda: Arrow(plane.c2p(0, 0), plane.c2p(4.25*np.cos(theta.get_value()), 
                                                                      4.25*np.sin(theta.get_value())), 
                                           buff=0, color=RED))

        dot_orig=Dot(ORIGIN, color=BLUE)
        dot_tip=Dot(plane.c2p(3,3), color=YELLOW, radius=0.1)
        origin_text = MathTex(r'O\\(0, 0)').next_to(dot_orig, DOWN, buff=0.1)
        tip_tex=MathTex("A", color=YELLOW).next_to(dot_tip, UP+LEFT)

        label_group=VGroup(tip_tex, origin_text)
        dot_group=VGroup(dot_tip, dot_orig)
        angle=Angle(plane.get_x_axis(), vect_1, radius=1, color=WHITE)
         
        self.play(DrawBorderThenFill(plane))
        #self.wait(2)
        self.play(LaggedStart(FadeIn(dot_tip),Write(tip_tex), FocusOn(dot_tip, color=YELLOW),
                              lag_ratio=0.15), run_time=4)
         
        self.play(LaggedStart(FadeIn(dot_orig),Write(origin_text), FocusOn(dot_orig, color=BLUE),
                              lag_ratio=0.15), run_time=4)
        #self.wait()
        vec=self.play(GrowArrow(vect_1))
        self.wait()
        self.play(theta.animate.set_value(9*PI/4), run_time=4)
        self.wait()
        self.add(angle)
        self.wait()