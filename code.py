from manim import *

class Test(Scene):
    def construct(self):
        code = Code("main.rs", line_spacing=0.8, font="Monospace", tab_width=2, background="window", font_size=28)
        code2 = Code("main2.rs", line_spacing=0.8, font="Monospace", tab_width=2, background="window", font_size=28)
        self.play(Write(code))
        self.wait(1)
        self.play(ReplacementTransform(code, code2))
        self.wait(1)