from manim import *

class Test(Scene):
    def construct(self):
        code = Code("main.rs", line_spacing=0.8, font="Monospace", tab_width=2, background="window", font_size=20).shift(UP * 0.5)
        self.play(Write(code))


        lines = [
            
        ] 
        integers = [
            Text("_").shift(DOWN*3),
            MathTex("2^{(8-1)}-1 = {127}").shift(DOWN*3),
            MathTex("2^{(16-1)}-1 = {32767}").shift(DOWN*3),
            MathTex("2^{(32-1)}-1 = {2147483647}").shift(DOWN*3),
            MathTex("2^{(64-1)}-1 = {9223372036854775807}").shift(DOWN*3),
            MathTex("2^{(128-1)}-1 = {170141183460469231731687303715884105727}").shift(DOWN*3),

            MathTex("2^{(8)}-1 = {255}").shift(DOWN*3),
            MathTex("2^{(16)}-1 = {65535}").shift(DOWN*3),
            MathTex("2^{(32)}-1 = {4294967295}").shift(DOWN*3),
            MathTex("2^{(64)}-1 = {18446744073709551615}").shift(DOWN*3),
            MathTex("2^{(128)}-1 = {340282366920938463463374607431768211455}").shift(DOWN*3),
            Text("END").shift(DOWN*3)
        ]


        for i in range(len(code.code)):
            lines.append(SurroundingRectangle(mobject=code.code[i], buff=0).set_fill(YELLOW).set_opacity(0.5).shift(DOWN*0.1))


        for i in range(1, len(lines)-1):
            self.play(ReplacementTransform(lines[i-1], lines[i]))
            self.play(ReplacementTransform(integers[i-1], integers[i]))
            self.wait(1)