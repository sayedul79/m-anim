from manim import *

class ColoredCircuit(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american]{circuitikz}")

        c = MathTex(
            r"""\draw (0,0) to[isource, l=$I_0$, v=$V_0$] (0,3);""", 
            r"""\draw (0,3) to[short, -*] (2,3);""",
            r"""\draw (2,3) to[R=$R_1$, i>_=$I_1$] (2,0);""",
            r"""\draw (2,3) -- (4,3);""", 
            r"\draw (4,3) to[R=$R_2$, i>_=$I_2$] (4,0);",
            r"\draw (4,0) to[short, -*] (2,0)--(0,0);"
            , stroke_width=4
            , fill_opacity=0
            , stroke_opacity=1
            , tex_environment="circuitikz"
            , tex_template=template
            
            )
        # for cir, clr in zip(c[0,4],[RED, GREEN, BLUE, YELLOW]):
        #     cir.set_color(clr)
        c.set_color_by_tex_to_color_map({"I_0":RED, "R_1":YELLOW, "R_2":BLUE})

        self.play(FadeIn(c, shift=UP, target_position=ORIGIN), run_time=3)
        self.play(ApplyWave(c[0]))
        self.play(Indicate(c[2], color=TEAL), run_time=2) 
        self.play(Circumscribe(c[4], fade_out=True, color=BLUE))
        self.wait(2)