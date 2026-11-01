
from manim import *

class DeltaAnimation(Scene):
    def construct(self):
        # 1. 创建坐标轴
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 4, 1],
            x_length=10,
            y_length=5,
            tips=False
        )

        labels = axes.get_axis_labels(
            x_label="x",
            y_label="y"
        )

        # 2. epsilon 控制函数宽度
        epsilon = ValueTracker(1.0)

        # 3. 定义近似 delta 的函数
        def kernel(x):
            e = epsilon.get_value()
            return e / (PI * (x**2 + e**2))

        # 4. 函数曲线随 epsilon 变化
        graph = always_redraw(
            lambda: axes.plot(
                kernel,
                x_range=[-4, 4, 0.01],
                color=YELLOW
            )
        )

        # 5. 显示数学公式
        formula = MathTex(
            r"K_{\varepsilon}(x)="
            r"\frac{1}{\pi}"
            r"\frac{\varepsilon}{x^2+\varepsilon^2}"
        ).to_edge(UP)

        # 6. 播放动画
        self.play(Create(axes), Write(labels))
        self.play(Write(formula))
        self.play(Create(graph))

        # epsilon 逐渐减小
        self.play(
            epsilon.animate.set_value(0.1),
            run_time=5,
            rate_func=linear
        )

        self.wait(2)
