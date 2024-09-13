from manim import *

class Test(Scene):
    def construct(self):
        let = Text("Integer String Boolean Array", font="Monospace")
        self.play(Write(let))
        self.wait(1)
        lett = Text("Integer", font="Monospace")
        self.play(ReplacementTransform(let, lett))