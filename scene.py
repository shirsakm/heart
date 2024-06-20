from manim import *

class SimpleHeart(Scene):
    def construct(self):
        heart = ParametricFunction(
            lambda t: np.array([
                (16 * np.sin(t) ** 3) / 8,
                (13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)) / 8,
                0
            ]), 
            t_range = [0, 2 * PI],
            color=RED,
        )

        self.play(FadeIn(heart))
        self.play(
            heart.animate.set_fill(PINK, opacity=0.7),
            run_time=2,
        )
        self.play(FadeOut(heart))

        self.play(Write(Text("I love you!").scale(2)))
        self.wait()