from manim import *

class CircuitAnimation(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages]{circuitikz}")
        template.tex_compiler = "pdflatex"
        template.output_format = ".pdf"
        circuit = MathTex(r"""
        \begin{circuitikz}[american]
        \draw (0,0) to[isource, l=$I_0$, v=$V_0$] (0,3) to[short, -*, i=$I_0$] (2,3) to[R=$R_1$, i>_=$I_1$, color=red] (2,0);
        \draw (2,3) -- (4,3) to[R=$R_2$, i>_=$I_2$, color=red] (4,0) to[short, -*] (2,0)--(0,0);
        \end{circuitikz}
        """,
        stroke_width=3,
        fill_opacity=0,
        stroke_opacity=1,
        stroke_color=YELLOW,
        tex_template = template)
        self.play(FadeIn(circuit, shift=UP*3, target_position=ORIGIN), run_time=2)
        self.play(circuit.animate.scale(0.6).to_edge(UR), run_time=3)
        self.wait()