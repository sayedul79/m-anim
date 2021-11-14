from manim import *


class ExampleTikz(Scene):
    def construct(self):
        my_temp = TexTemplate()
        my_temp.add_to_preamble(r"\usepackage{circuitikz}")
        my_temp.tex_compiler = "pdflatex"
        my_temp.output_format = ".pdf"
        circuit = Tex(r"""
            \begin{circuitikz} \draw
            (0,0) to[ variable cute inductor ] (2,0); 
            \end{circuitikz}
            """,
            stroke_width=3,
            fill_opacity=0,
            stroke_opacity=1,
            tex_template = my_temp
            )
        self.play(Write(circuit))
        self.wait()