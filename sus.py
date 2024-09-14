from manim import *

class Test(Scene):
    def construct(self):
        zero = Text("Integer", font="monospace")
        self.play(Write(zero))
        one = VGroup(
            VGroup(
                heightlighting("i", "8"),
                heightlighting("i", "16"),
                heightlighting("i", "32"),
                heightlighting("i", "64"),
                heightlighting("i", "128"),
                heightlighting("i", "size"),
            ).arrange(RIGHT, buff=.3),


            VGroup(
                heightlighting("u", "8"),
                heightlighting("u", "16"),
                heightlighting("u", "32"),
                heightlighting("u", "64"),
                heightlighting("u", "128"),
                heightlighting("u", "size"),
            ).arrange(RIGHT, buff=.3)
        )
        one.arrange(DOWN, buff=.5)

        self.play(ReplacementTransform(zero, one))
        self.wait(1)
        two = VGroup(
            VGroup(
                heightlighting("i", "8", color=BLUE),
                heightlighting("i", "16", color=BLUE),
                heightlighting("i", "32", color=BLUE),
                heightlighting("i", "64", color=BLUE),
                heightlighting("i", "128", color=BLUE),
                heightlighting("i", "size"),
            ).arrange(RIGHT, buff=.3),


            VGroup(
                heightlighting("u", "8", color=BLUE),
                heightlighting("u", "16", color=BLUE),
                heightlighting("u", "32", color=BLUE),
                heightlighting("u", "64", color=BLUE),
                heightlighting("u", "128", color=BLUE),
                heightlighting("u", "size"),
            ).arrange(RIGHT, buff=.3)
        )
        two.arrange(DOWN, buff=.5)
        self.play(ReplacementTransform(one, two))

        self.wait(1)

def heightlighting(text, heightlighting, color = color.WHITE) -> VGroup:
    vg = VGroup(Text(text, font="monospace"), Text(heightlighting, color=color, font="monospace"))
    vg.arrange(RIGHT, buff=0.1)
    return vg