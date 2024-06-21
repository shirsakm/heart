from manim import *

class BeatingHeart(Scene):
    def construct(self):
        for a in range(70, 150, 1):
            heart = FunctionGraph(
                lambda x: (x ** 2) ** (1 / 3) + (3.3 - x ** 2) ** 0.5 * np.sin(a / 10 * PI * x),
                x_range=[-1.8, 1.8],
                color=RED,
            )

            self.add(heart)
            self.wait(1 / 30)
            self.remove(heart)

        self.wait()

        for a in range(150, 70, -1):
            heart = FunctionGraph(
                lambda x: (x ** 2) ** (1 / 3) + (3.3 - x ** 2) ** 0.5 * np.sin(a / 10 * PI * x),
                x_range=[-1.8, 1.8],
                color=RED,
            )

            self.add(heart)
            self.wait(1 / 30)
            self.remove(heart)

    """
    Old way of doing it, does not animate well

    def construct(self):
        heart_relaxed = FunctionGraph(
            lambda x: (x ** 2) ** (1 / 3) + (3.3 - x ** 2) ** 0.5 * np.sin(7 * PI * x),
            x_range=[-1.8, 1.8],
            color=RED,
        )

        heart_contracted = FunctionGraph(
            lambda x: (x ** 2) ** (1 / 3) + (3.3 - x ** 2) ** 0.5 * np.sin(15 * PI * x),
            x_range=[-1.8, 1.8],
            color=RED,
        )

        self.play(Create(heart_relaxed))
        self.play(
            ReplacementTransform(heart_relaxed, heart_contracted),
            run_time=2,
        )
        self.play(
            ReplacementTransform(heart_contracted, heart_relaxed),
            run_time=2,
        )
        self.play(FadeOut(heart_relaxed))
    """


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

