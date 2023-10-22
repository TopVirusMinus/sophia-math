# 6_2: Exponential Functions: Term & Graph

# Import necessary libraries and modules
from abc import ABCMeta, abstractmethod
from sophialib.page_prototypes.prototype import PagePrototypeQuestion, PagePrototypeVideo
from sophialib.styles.sophiascene import (CursorMoveToCurved, CursorPositionTracker,
                                          CursorPositionTracking,
                                          CursorResizeDefault, SophiaScene,
                                          assets_folder, AltCursor,
                                          SophiaCursorScene, CursorMoveTo,
                                          CursorMoveResize, Notepad, CursorMarkAxis, Bubble)
from sophialib.styles.styleconstants import *
from sophialib.styles.sophiaobjects import *
from manim import *
from PIL import Image
import numpy as np
from pathlib import Path
from sophialib.tasks.sophiataskdefinition import SophiaTaskDefinition
import ast


#####################################
#####################################
class Func_6_2_I_1(SophiaCursorScene):

    # Main method for constructing the animation
    def construct(self):
        # Adding initial components to the scene
        super().construct()
        self.add_mathgrid()

        self.add_title(self.translate("Func_6_2.I1.title"))

        cords = self.add_cords([0, 6, 1], [0, 64, 8], x_ticks=[2,4,6], y_ticks=[16,32,48,64])
        plane = cords[0]

        f_tex = MathTex("f","(x)", "=", "a", "^x", color=c1t, font_size=fs2).next_to(cords, DOWN, buff=0.4)

        a_tex_g1 = MathTex("a>1", color=BLUE, font_size=fs2).next_to(f_tex, DOWN, buff=0.2)
        f = lambda x:2**x
        f_plot = plane.plot(f, color=BLUE)

        cords_2 = self.add_cords([0, 6, 1], [0, 1, 0.25], x_ticks=[2,4,6], y_ticks=[0,0.25,0.5,0.75,1])
        plane_2 = cords_2[0]

        a_tex_l1 = MathTex("0<a<1", color=GREEN, font_size=fs2).next_to(f_tex, DOWN, buff=0.2)
        g = lambda x:0.5**x
        g_plot = plane_2.plot(g, color=GREEN)

        def cursor_sound_updater(mob, dt):
            if mob.needSound:
                mob.needSound = False
                self.add_cursor_sound()
        x,y,_ = plane.c2p(0,0)
        cursor = AltCursor(stroke_width=0.0, blinking=True, x=x, y=y)
        cursor.autoFadeBackground = True
        cursor.add_updater(cursor_sound_updater)
        self.add(cursor)


        # Action Sequence
        with self.voiceover(
                text=self.translate("Func_6_2.I1.voiceover")
        ) as tracker:
            
            self.wait_until_bookmark("f")
            x,y,_ = f_tex[0].get_center()+0.4*DOWN
            cursor.blinking=False
            self.play(Write(f_tex), CursorMoveTo(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fx")
            x,y,_ = f_tex[1].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fa")
            x,y,_ = f_tex[3].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fxx")
            x,y,_ = f_tex[4].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("a")
            cursor.blinking=False
            x,y,_ = f_tex[3].get_center()+0.4*DOWN
            self.play(CursorMoveTo(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("a_g1")
            cursor.blinking=False
            x,y,_ = a_tex_g1.get_center()+0.4*DOWN
            self.play(Write(a_tex_g1), CursorMoveToCurved(cursor,x,y), run_time=0.3)
            self.play(Write(cords))
            cursor.blinking=True

            self.wait_until_bookmark("plot_1")
            cursor.blinking=False
            x,y,_ = f_plot.get_start()
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            self.add(cursor.copy()._start_fading(2).add_updater(lambda m: m.move_to(f_plot.get_end())))
            self.add_pencil_sound(1.5)
            self.play(Create(f_plot))
            cursor.blinking=True

            self.wait_until_bookmark("a_l1")
            cursor.blinking=False
            x,y,_ = a_tex_l1.get_center()+0.4*DOWN
            self.play(ReplacementTransform(a_tex_g1, a_tex_l1), CursorMoveToCurved(cursor,x,y), run_time=0.3)
            self.play(ReplacementTransform(cords, cords_2), Unwrite(f_plot), run_time=0.5)
            cursor.blinking=True

            self.wait_until_bookmark("plot_2")
            cursor.blinking=False
            x,y,_ = g_plot.get_start()
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            self.add(cursor.copy()._start_fading(2).add_updater(lambda m: m.move_to(g_plot.get_end())))
            self.add_pencil_sound(1.5)
            self.play(Create(g_plot))
            cursor.blinking=True

        self.wait(4)


#####################################
#####################################
class Func_6_2_I_2_q(SophiaCursorScene):

    def task_definition(self) -> SophiaTaskDefinition:
        return SophiaTaskDefinition(
            answerOptions = ["$a=1$", "$a=-1$", "$a=\frac{1}{2}$", "$a=2$"],
            correctAnswerIndex = 2,
            questionText=self.translate("Func_6_2.I2.q.question-text")
        )

    # Main method for constructing the animation
    def construct(self):
        # Adding initial components to the scene
        super().construct()
        self.add_mathgrid()

        self.add_title(self.translate("Func_6_2.I1.title"))

        def cursor_sound_updater(mob, dt):
            if mob.needSound:
                mob.needSound = False
                self.add_cursor_sound()
        cursor = AltCursor(stroke_width=0.0, blinking=True)
        cursor.autoFadeBackground = True
        cursor.add_updater(cursor_sound_updater)
        self.add(cursor)

        full_pizza = ImageMobject(assets_folder / "img" / "full_pizza.png")
        full_pizza = full_pizza.scale(2.5/full_pizza.get_width()).move_to([-5, 1, 0])
        
        half_pizza = ImageMobject(assets_folder / "img" / "half_pizza.png")
        half_pizza = half_pizza.scale(2.5/half_pizza.get_width()).move_to([-5, 1, 0])

        quarter_pizza = ImageMobject(assets_folder / "img" / "quarter_pizza.png")
        quarter_pizza = quarter_pizza.scale(2.5/quarter_pizza.get_width()).move_to([-5, 1, 0])

        eigth_pizza = ImageMobject(assets_folder / "img" / "eigth_pizza.png")
        eigth_pizza = eigth_pizza.scale(2.5/eigth_pizza.get_width()).move_to([-5, 1, 0])

        all_pizza = Group(full_pizza, half_pizza, quarter_pizza, eigth_pizza)

        clock = ImageMobject(assets_folder / "img" / "clock.png")
        clock = clock.scale(2.5/clock.get_width()).move_to([-5, -2, 0])

        qmark = ImageMobject(assets_folder / "img" / "qmark.png")
        qmark = qmark.scale(2.5/qmark.get_width()).move_to([-5, 1, 0])

        minutes = self.translate("Func_6_2.I2.q.minutes")
        f_tex = MathTex("f","(x)", "=", "a", "^x", color=c1t, font_size=fs2).next_to(full_pizza, DOWN, buff=0.4).shift(RIGHT*5)
        x_minutes = Tex("$x$", f": \\# {minutes}", color=c1t, font_size=fs2).next_to(f_tex, DOWN, buff=0.2)

        

        # Action Sequence
        with self.voiceover(
                text=self.translate("Func_6_2.I2.q.voiceover")
        ) as tracker:
            
            self.wait_until_bookmark("full_pizza")
            self.play(all_pizza.animate.shift(RIGHT*5), run_time=0.5)

            self.wait_until_bookmark("late")
            self.play(clock.animate.shift(RIGHT*5), run_time=0.5)

            self.wait_until_bookmark("full")
            self.play(clock.animate.shift(RIGHT*5), FadeOut(full_pizza))

            self.wait_until_bookmark("half")
            self.play(FadeOut(half_pizza))

            self.wait_until_bookmark("quarter")
            self.play(FadeOut(quarter_pizza))

            self.wait_until_bookmark("f")
            x,y,_ = f_tex[0].get_center()+0.4*DOWN
            cursor.blinking=False
            self.play(Write(f_tex), CursorMoveTo(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fx")
            x,y,_ = f_tex[1].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fa")
            x,y,_ = f_tex[3].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fxx")
            x,y,_ = f_tex[4].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("qmark")
            self.play(qmark.animate.shift(RIGHT*5), run_time=0.5)

            self.wait_until_bookmark("x_minutes")
            cursor.blinking=False
            x,y,_ = x_minutes[0].get_center()+0.4*DOWN
            self.play(Write(x_minutes), CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("minutes")
            x,y,_ = x_minutes[1].get_center()+0.4*DOWN  
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

        self.wait(4)


class Func_6_2_I_2_a(SophiaCursorScene):

    # Main method for constructing the animation
    def construct(self):
        # Adding initial components to the scene
        super().construct()
        self.add_mathgrid()

        self.add_title(self.translate("Func_6_2.I1.title"))

        def cursor_sound_updater(mob, dt):
            if mob.needSound:
                mob.needSound = False
                self.add_cursor_sound()
        cursor = AltCursor(stroke_width=0.0, blinking=True)
        cursor.autoFadeBackground = True
        cursor.add_updater(cursor_sound_updater)
        self.add(cursor)

        full_pizza = ImageMobject(assets_folder / "img" / "full_pizza.png")
        full_pizza = full_pizza.scale(2.5/full_pizza.get_width()).move_to([0, 1, 0])
        
        half_pizza = ImageMobject(assets_folder / "img" / "half_pizza.png")
        half_pizza = half_pizza.scale(2.5/half_pizza.get_width()).move_to([0, 1, 0])

        quarter_pizza = ImageMobject(assets_folder / "img" / "quarter_pizza.png")
        quarter_pizza = quarter_pizza.scale(2.5/quarter_pizza.get_width()).move_to([0, 1, 0])

        eigth_pizza = ImageMobject(assets_folder / "img" / "eigth_pizza.png")
        eigth_pizza = eigth_pizza.scale(2.5/eigth_pizza.get_width()).move_to([0, 1, 0])

        all_pizza = Group(full_pizza, half_pizza, quarter_pizza, eigth_pizza)
        self.add(all_pizza)

        clock = ImageMobject(assets_folder / "img" / "clock.png")
        clock = clock.scale(2.5/clock.get_width()).move_to([-5, -2, 0])

        qmark = ImageMobject(assets_folder / "img" / "qmark.png")
        qmark = qmark.scale(2.5/qmark.get_width()).move_to([0, 1, 0])

        f_tex = MathTex("f","(x)", "=", "\\frac12", "^x", color=c1t, font_size=fs2).next_to(full_pizza, DOWN, buff=0.4)
        sol_a = MathTex("\\Rightarrow","a","=", "\\frac12", color=c1t, font_size=fs2).next_to(f_tex, DOWN, buff=0.2)

        pizza_left = self.translate("Func_6_2.I2.a.pizza-left")

        t = MathTable(
            [["x", f"\\text{{{pizza_left}}}"],
            
            ["1", "\\tfrac12"],
            ["2", "(\\tfrac12)^2"],
            ["3", "(\\tfrac12)^3"],
            ["...", "..."]], element_to_mobject_config={"color": c1t}, line_config={"color": c1t}).scale(0.35).next_to(full_pizza, DOWN, buff=0.4)
        
        rows = t.get_rows()
        t_structure = VGroup(t.get_horizontal_lines(), t.get_vertical_lines())
        

        

        # Action Sequence
        with self.voiceover(
                text=self.translate("Func_6_2.I2.a.voiceover")
        ) as tracker:
            
            self.wait_until_bookmark("minute")
            self.play(clock.animate.shift(RIGHT*5), run_time=0.5)

            self.wait_until_bookmark("half_1")
            self.play(clock.animate.shift(RIGHT*5), FadeOut(full_pizza))

            self.wait_until_bookmark("half_2")
            self.play(FadeOut(half_pizza))

            self.wait_until_bookmark("row_1")
            self.play(Write(t_structure), Write(rows[0]), run_time=0.5)
            x,y,_ = rows[1].get_right()+0.4*RIGHT
            cursor.blinking=False
            self.play(Write(rows[1]), CursorMoveTo(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("row_2")
            x,y,_ = rows[2].get_right()+0.4*RIGHT
            self.play(Write(rows[2]), CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("row_3")
            x,y,_ = rows[3].get_right()+0.4*RIGHT
            self.play(Write(rows[3]), CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("row_4")
            x,y,_ = rows[4].get_right()+0.4*RIGHT
            self.play(Write(rows[4]), CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("f")
            x,y,_ = f_tex[0].get_center()+0.4*DOWN
            cursor.blinking=False
            self.play(t.animate.shift(RIGHT*5), Write(f_tex), CursorMoveTo(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fx")
            x,y,_ = f_tex[1].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fa")
            x,y,_ = f_tex[3].get_center()+0.6*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fxx")
            x,y,_ = f_tex[4].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("sol_a")
            cursor.blinking=False
            x,y,_ = sol_a[1].get_center()+0.4*DOWN
            self.play(Write(sol_a), CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("sol_half")
            x,y,_ = sol_a[3].get_center()+0.6*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True


        self.wait(4)

class Func_6_2_I_2_b(SophiaCursorScene):

    # Main method for constructing the animation
    def construct(self):
        # Adding initial components to the scene
        super().construct()
        self.add_mathgrid()

        self.add_title(self.translate("Func_6_2.I1.title"))

        def cursor_sound_updater(mob, dt):
            if mob.needSound:
                mob.needSound = False
                self.add_cursor_sound()
        cursor = AltCursor(stroke_width=0.0, blinking=True)
        cursor.autoFadeBackground = True
        cursor.add_updater(cursor_sound_updater)
        self.add(cursor)

        full_pizza = ImageMobject(assets_folder / "img" / "full_pizza.png")
        full_pizza = full_pizza.scale(2.5/full_pizza.get_width()).move_to([0, 1, 0])
        
        half_pizza = ImageMobject(assets_folder / "img" / "half_pizza.png")
        half_pizza = half_pizza.scale(2.5/half_pizza.get_width()).move_to([0, 1, 0])

        quarter_pizza = ImageMobject(assets_folder / "img" / "quarter_pizza.png")
        quarter_pizza = quarter_pizza.scale(2.5/quarter_pizza.get_width()).move_to([0, 1, 0])

        eigth_pizza = ImageMobject(assets_folder / "img" / "eigth_pizza.png")
        eigth_pizza = eigth_pizza.scale(2.5/eigth_pizza.get_width()).move_to([0, 1, 0])

        all_pizza = Group(full_pizza, half_pizza, quarter_pizza, eigth_pizza)
        self.add(all_pizza)

        clock = ImageMobject(assets_folder / "img" / "clock.png")
        clock = clock.scale(2.5/clock.get_width()).move_to([-5, -2, 0])

        qmark = ImageMobject(assets_folder / "img" / "qmark.png")
        qmark = qmark.scale(2.5/qmark.get_width()).move_to([0, 1, 0])

        f_tex = MathTex("f","(x)", "=", "\\frac12", "^x", color=c1t, font_size=fs2).next_to(full_pizza, DOWN, buff=0.4)
        sol_a = MathTex("\\Rightarrow","a","=", "\\frac12", color=c1t, font_size=fs2).next_to(f_tex, DOWN, buff=0.2)

        pizza_left = self.translate("Func_6_2.I2.a.pizza-left")

        t = MathTable(
            [["x", f"\\text{pizza_left}"],
            ["1", "\\tfrac12"],
            ["2", "(\\tfrac12)^2"],
            ["3", "(\\tfrac12)^3"],
            ["...", "..."]], element_to_mobject_config={"color": c1t}, line_config={"color": c1t}).scale(0.35).next_to(full_pizza, DOWN, buff=0.4)
        
        rows = t.get_rows()
        t_structure = VGroup(t.get_horizontal_lines(), t.get_vertical_lines())
        

        

        # Action Sequence
        with self.voiceover(
                text=self.translate("Func_6_2.I2.a.voiceover")
        ) as tracker:
            
            self.wait_until_bookmark("minute")
            self.play(clock.animate.shift(RIGHT*5), run_time=0.5)

            self.wait_until_bookmark("half_1")
            self.play(clock.animate.shift(RIGHT*5), FadeOut(full_pizza))

            self.wait_until_bookmark("half_2")
            self.play(FadeOut(half_pizza))

            self.wait_until_bookmark("row_1")
            self.play(Write(t_structure), Write(rows[0]), run_time=0.5)
            x,y,_ = rows[1].get_right()+0.4*RIGHT
            cursor.blinking=False
            self.play(Write(rows[1]), CursorMoveTo(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("row_2")
            x,y,_ = rows[2].get_right()+0.4*RIGHT
            self.play(Write(rows[2]), CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("row_3")
            x,y,_ = rows[3].get_right()+0.4*RIGHT
            self.play(Write(rows[3]), CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("row_4")
            x,y,_ = rows[4].get_right()+0.4*RIGHT
            self.play(Write(rows[4]), CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("f")
            x,y,_ = f_tex[0].get_center()+0.4*DOWN
            cursor.blinking=False
            self.play(t.animate.shift(RIGHT*5), Write(f_tex), CursorMoveTo(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fx")
            x,y,_ = f_tex[1].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fa")
            x,y,_ = f_tex[3].get_center()+0.6*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fxx")
            x,y,_ = f_tex[4].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("sol_a")
            cursor.blinking=False
            x,y,_ = sol_a[1].get_center()+0.4*DOWN
            self.play(Write(sol_a), CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("sol_half")
            x,y,_ = sol_a[3].get_center()+0.6*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True


        self.wait(4)


class Func_6_2_I_2_c(SophiaCursorScene):

    # Main method for constructing the animation
    def construct(self):
        # Adding initial components to the scene
        super().construct()
        self.add_mathgrid()

        self.add_title(self.translate("Func_6_2.I1.title"))

        def cursor_sound_updater(mob, dt):
            if mob.needSound:
                mob.needSound = False
                self.add_cursor_sound()
        cursor = AltCursor(stroke_width=0.0, blinking=True)
        cursor.autoFadeBackground = True
        cursor.add_updater(cursor_sound_updater)
        self.add(cursor)

        full_pizza = ImageMobject(assets_folder / "img" / "full_pizza.png")
        full_pizza = full_pizza.scale(2.5/full_pizza.get_width()).move_to([0, 1, 0])
        
        half_pizza = ImageMobject(assets_folder / "img" / "half_pizza.png")
        half_pizza = half_pizza.scale(2.5/half_pizza.get_width()).move_to([0, 1, 0])

        quarter_pizza = ImageMobject(assets_folder / "img" / "quarter_pizza.png")
        quarter_pizza = quarter_pizza.scale(2.5/quarter_pizza.get_width()).move_to([0, 1, 0])

        eigth_pizza = ImageMobject(assets_folder / "img" / "eigth_pizza.png")
        eigth_pizza = eigth_pizza.scale(2.5/eigth_pizza.get_width()).move_to([0, 1, 0])

        all_pizza = Group(full_pizza, half_pizza, quarter_pizza, eigth_pizza)
        self.add(all_pizza)

        clock = ImageMobject(assets_folder / "img" / "clock.png")
        clock = clock.scale(2.5/clock.get_width()).move_to([-5, -2, 0])

        qmark = ImageMobject(assets_folder / "img" / "qmark.png")
        qmark = qmark.scale(2.5/qmark.get_width()).move_to([0, 1, 0])

        f_tex = MathTex("f","(x)", "=", "\\frac12", "^x", color=c1t, font_size=fs2).next_to(full_pizza, DOWN, buff=0.4)
        sol_a = MathTex("\\Rightarrow","a","=", "\\frac12", color=c1t, font_size=fs2).next_to(f_tex, DOWN, buff=0.2)


        pizza_left = self.translate("Func_6_2.I2.a.pizza-left")

        t = MathTable(
            [["x", f"\\text{pizza_left}"],
            ["1", "\\tfrac12"],
            ["2", "(\\tfrac12)^2"],
            ["3", "(\\tfrac12)^3"],
            ["...", "..."]], element_to_mobject_config={"color": c1t}, line_config={"color": c1t}).scale(0.35).next_to(full_pizza, DOWN, buff=0.4)
        
        rows = t.get_rows()
        t_structure = VGroup(t.get_horizontal_lines(), t.get_vertical_lines())
        

        

        # Action Sequence
        with self.voiceover(
                text=self.translate("Func_6_2.I2.c.voiceover")
        ) as tracker:
            
            self.wait_until_bookmark("minute")
            self.play(clock.animate.shift(RIGHT*5), run_time=0.5)

            self.wait_until_bookmark("half_1")
            self.play(clock.animate.shift(RIGHT*5), FadeOut(full_pizza))

            self.wait_until_bookmark("half_2")
            self.play(FadeOut(half_pizza))

            self.wait_until_bookmark("row_1")
            self.play(Write(t_structure), Write(rows[0]), run_time=0.5)
            x,y,_ = rows[1].get_right()+0.4*RIGHT
            cursor.blinking=False
            self.play(Write(rows[1]), CursorMoveTo(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("row_2")
            x,y,_ = rows[2].get_right()+0.4*RIGHT
            self.play(Write(rows[2]), CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("row_3")
            x,y,_ = rows[3].get_right()+0.4*RIGHT
            self.play(Write(rows[3]), CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("row_4")
            x,y,_ = rows[4].get_right()+0.4*RIGHT
            self.play(Write(rows[4]), CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("f")
            x,y,_ = f_tex[0].get_center()+0.4*DOWN
            cursor.blinking=False
            self.play(t.animate.shift(RIGHT*5), Write(f_tex), CursorMoveTo(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fx")
            x,y,_ = f_tex[1].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fa")
            x,y,_ = f_tex[3].get_center()+0.6*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fxx")
            x,y,_ = f_tex[4].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("sol_a")
            cursor.blinking=False
            x,y,_ = sol_a[1].get_center()+0.4*DOWN
            self.play(Write(sol_a), CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("sol_half")
            x,y,_ = sol_a[3].get_center()+0.6*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True


        self.wait(4)

class Func_6_2_I_2_d(SophiaCursorScene):

    # Main method for constructing the animation
    def construct(self):
        # Adding initial components to the scene
        super().construct()
        self.add_mathgrid()

        self.add_title(self.translate("Func_6_2.I1.title"))

        def cursor_sound_updater(mob, dt):
            if mob.needSound:
                mob.needSound = False
                self.add_cursor_sound()
        cursor = AltCursor(stroke_width=0.0, blinking=True)
        cursor.autoFadeBackground = True
        cursor.add_updater(cursor_sound_updater)
        self.add(cursor)

        full_pizza = ImageMobject(assets_folder / "img" / "full_pizza.png")
        full_pizza = full_pizza.scale(2.5/full_pizza.get_width()).move_to([0, 1, 0])
        
        half_pizza = ImageMobject(assets_folder / "img" / "half_pizza.png")
        half_pizza = half_pizza.scale(2.5/half_pizza.get_width()).move_to([0, 1, 0])

        quarter_pizza = ImageMobject(assets_folder / "img" / "quarter_pizza.png")
        quarter_pizza = quarter_pizza.scale(2.5/quarter_pizza.get_width()).move_to([0, 1, 0])

        eigth_pizza = ImageMobject(assets_folder / "img" / "eigth_pizza.png")
        eigth_pizza = eigth_pizza.scale(2.5/eigth_pizza.get_width()).move_to([0, 1, 0])

        all_pizza = Group(full_pizza, half_pizza, quarter_pizza, eigth_pizza)
        self.add(all_pizza)

        clock = ImageMobject(assets_folder / "img" / "clock.png")
        clock = clock.scale(2.5/clock.get_width()).move_to([-5, -2, 0])

        qmark = ImageMobject(assets_folder / "img" / "qmark.png")
        qmark = qmark.scale(2.5/qmark.get_width()).move_to([0, 1, 0])

        f_tex = MathTex("f","(x)", "=", "\\frac12", "^x", color=c1t, font_size=fs2).next_to(full_pizza, DOWN, buff=0.4)
        sol_a = MathTex("\\Rightarrow","a","=", "\\frac12", color=c1t, font_size=fs2).next_to(f_tex, DOWN, buff=0.2)

        pizza_left = self.translate("Func_6_2.I2.a.pizza-left")

        t = MathTable(
            [["x", f"\\text{pizza_left}"],
            ["1", "\\tfrac12"],
            ["2", "(\\tfrac12)^2"],
            ["3", "(\\tfrac12)^3"],
            ["...", "..."]], element_to_mobject_config={"color": c1t}, line_config={"color": c1t}).scale(0.35).next_to(full_pizza, DOWN, buff=0.4)
        
        rows = t.get_rows()
        t_structure = VGroup(t.get_horizontal_lines(), t.get_vertical_lines())
        

        

        # Action Sequence
        with self.voiceover(
                text=self.translate("Func_6_2.I2.a.voiceover")
        ) as tracker:
            
            self.wait_until_bookmark("minute")
            self.play(clock.animate.shift(RIGHT*5), run_time=0.5)

            self.wait_until_bookmark("half_1")
            self.play(clock.animate.shift(RIGHT*5), FadeOut(full_pizza))

            self.wait_until_bookmark("half_2")
            self.play(FadeOut(half_pizza))

            self.wait_until_bookmark("row_1")
            self.play(Write(t_structure), Write(rows[0]), run_time=0.5)
            x,y,_ = rows[1].get_right()+0.4*RIGHT
            cursor.blinking=False
            self.play(Write(rows[1]), CursorMoveTo(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("row_2")
            x,y,_ = rows[2].get_right()+0.4*RIGHT
            self.play(Write(rows[2]), CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("row_3")
            x,y,_ = rows[3].get_right()+0.4*RIGHT
            self.play(Write(rows[3]), CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("row_4")
            x,y,_ = rows[4].get_right()+0.4*RIGHT
            self.play(Write(rows[4]), CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("f")
            x,y,_ = f_tex[0].get_center()+0.4*DOWN
            cursor.blinking=False
            self.play(t.animate.shift(RIGHT*5), Write(f_tex), CursorMoveTo(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fx")
            x,y,_ = f_tex[1].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fa")
            x,y,_ = f_tex[3].get_center()+0.6*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fxx")
            x,y,_ = f_tex[4].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("sol_a")
            cursor.blinking=False
            x,y,_ = sol_a[1].get_center()+0.4*DOWN
            self.play(Write(sol_a), CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("sol_half")
            x,y,_ = sol_a[3].get_center()+0.6*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True


        self.wait(4)


#####################################
#####################################
class Func_6_2_I_3(SophiaCursorScene):

    # Main method for constructing the animation
    def construct(self):
        # Adding initial components to the scene
        super().construct()
        self.add_mathgrid()

        title = self.add_title(self.translate("Func_6_2.I3.title"))

        cords = self.add_cords([0, 6, 1], [0, 64, 8], x_ticks=[2,4,6], y_ticks=[16,32,48,64])
        plane = cords[0]

        f_tex = MathTex("f","(x)", "=", "a", "^x", color=c1t, font_size=fs2).next_to(cords, DOWN, buff=0.4)

        a_tex_g1 = MathTex("a>1", color=BLUE, font_size=fs2).next_to(f_tex, DOWN, buff=0.2)
        f = lambda x:2**x
        f_plot = plane.plot(f, color=BLUE)

        cords_2 = self.add_cords([0, 6, 1], [0, 1, 0.25], x_ticks=[2,4,6], y_ticks=[0,0.25,0.5,0.75,1])
        plane_2 = cords_2[0]

        a_tex_l1 = MathTex("0<a<1", color=GREEN, font_size=fs2).next_to(f_tex, DOWN, buff=0.2)
        g = lambda x:0.5**x
        g_plot = plane_2.plot(g, color=GREEN)

        def cursor_sound_updater(mob, dt):
            if mob.needSound:
                mob.needSound = False
                self.add_cursor_sound()
        x,y,_ = plane.c2p(0,0)
        cursor = AltCursor(stroke_width=0.0, blinking=True, x=x, y=y)
        cursor.autoFadeBackground = True
        cursor.add_updater(cursor_sound_updater)
        self.add(cursor)


        # Action Sequence
        with self.voiceover(
                text=self.translate("Func_6_2.I3.voiceover")
        ) as tracker:
            
            self.wait_until_bookmark("f")
            x,y,_ = f_tex[0].get_center()+0.4*DOWN
            cursor.blinking=False
            self.play(Write(f_tex), CursorMoveTo(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fx")
            x,y,_ = f_tex[1].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fa")
            x,y,_ = f_tex[3].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fxx")
            x,y,_ = f_tex[4].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("a")
            cursor.blinking=False
            x,y,_ = f_tex[3].get_center()+0.4*DOWN
            self.play(CursorMoveTo(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("growth")
            cursor.blinking=False
            x,y,_ = title.get_left()+0.4*DOWN+RIGHT
            self.play(CursorMoveTo(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("factor")
            x,y,_ = title.get_right()+0.4*DOWN+0.7*LEFT
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("plot_1")
            cursor.blinking=False
            x,y,_ = f_plot.get_start()
            self.play(CursorMoveToCurved(cursor,x,y), Write(cords), run_time=0.3)
            self.add(cursor.copy()._start_fading(2).add_updater(lambda m: m.move_to(f_plot.get_end())))
            self.add_pencil_sound(1.5)
            self.play(Create(f_plot))
            cursor.blinking=True

            self.wait_until_bookmark("plot_2")
            cursor.blinking=False
            x,y,_ = g_plot.get_start()
            self.play(ReplacementTransform(cords, cords_2), Unwrite(f_plot), CursorMoveToCurved(cursor,x,y), run_time=0.3)
            self.add(cursor.copy()._start_fading(2).add_updater(lambda m: m.move_to(g_plot.get_end())))
            self.add_pencil_sound(1.5)
            self.play(Create(g_plot))
            cursor.blinking=True

        self.wait(4)



#####################################
#####################################
######## Practice Part ##############
#####################################
#####################################




#####################################
#####################################
######## General Qs #################
#####################################
#####################################

#####################################
#####################################
class GraphToGrowthFactorQuestionScene(SophiaCursorScene, metaclass = ABCMeta):

    # Main method for constructing the animation
    @abstractmethod
    def construct(self):
        # Adding initial components to the scene
        super().construct()
        self.add_mathgrid()

        title = self.add_title(self.translate("Func_6_2.I3.title"))

        plane = self.cords[0]

        def cursor_sound_updater(mob, dt):
            if mob.needSound:
                mob.needSound = False
                self.add_cursor_sound()
        cursor = AltCursor(stroke_width=0.0, blinking=True)
        cursor.autoFadeBackground = True
        cursor.add_updater(cursor_sound_updater)
        self.add(cursor)

        qmark = ImageMobject(assets_folder / "img" / "qmark.png")
        qmark = qmark.scale(2.5/qmark.get_width()).move_to([-5, 1, 0])

        f_tex = MathTex("f","(x)", "=", "a", "^x", color=c1t, font_size=fs2).next_to(plane, DOWN, buff=0.4)
        xm1, xm2 = self.translate("Func_6_2.I3.x-minutes_1"), self.translate("Func_6_2.I3.x-minutes_2")
        x_minutes = VGroup(Tex("$\\Rightarrow$", xm1, color=c1t, font_size=fs3), Tex(xm2, " $a$?", color=c1t, font_size=fs3)).arrange(DOWN, buff=0.1, aligned_edge=RIGHT).next_to(f_tex, DOWN, buff=0.2)

        func = lambda x: self.a**x
        f = plane.plot(func, color=self.color)

        # Action Sequence
        with self.voiceover(
                text=self.evaluate_string(self.translate("Func_6_2.GraphToGrowthFactorQuestionScene.voiceover"))
        ) as tracker:
            
            self.play(Write(self.cords))
            
            self.wait_until_bookmark("plot")
            x, y, _ = f.get_start()
            self.play(CursorMoveToCurved(cursor, x, y), run_time=0.3)
            self.add(cursor.copy()._start_fading(2).add_updater(lambda m: m.move_to(f.get_end())))
            self.add_pencil_sound(1.5)
            self.play(Create(f))
            cursor.blinking=True

            self.wait_until_bookmark("function")
            x,y,_ = f_tex[0].get_center()+0.4*DOWN
            cursor.blinking=False
            self.play(Write(f_tex), CursorMoveTo(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fx")
            x,y,_ = f_tex[1].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fa")
            x,y,_ = f_tex[3].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("xx")
            x,y,_ = f_tex[4].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("q")
            x,y,_ = x_minutes[1].get_center()+0.4*DOWN
            cursor.blinking=False
            self.play(Write(x_minutes), CursorMoveTo(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("q_a")
            x,y,_ = x_minutes[1][1].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True


        self.wait(4)


class GraphToGrowthFactorAnswerScene(SophiaCursorScene, metaclass=ABCMeta):

    # Main method for constructing the animation
    @abstractmethod
    def construct(self):
        # Adding initial components to the scene
        super().construct()
        self.add_mathgrid()

        title = self.add_title(self.translate("Func_6_2.I3.title"))

        plane = self.cords[0]

        def cursor_sound_updater(mob, dt):
            if mob.needSound:
                mob.needSound = False
                self.add_cursor_sound()
        cursor = AltCursor(stroke_width=0.0, blinking=True)
        cursor.autoFadeBackground = True
        cursor.add_updater(cursor_sound_updater)
        self.add(cursor)

        qmark = ImageMobject(assets_folder / "img" / "qmark.png")
        qmark = qmark.scale(2.5/qmark.get_width()).move_to([-5, 1, 0])

        f_tex = MathTex("f","(x)", "=", "a", "^x", color=c1t, font_size=fs2).next_to(plane, DOWN, buff=0.4)
        sol = Tex("$\\Rightarrow$", f"a={self.a}", color=c1t, font_size=fs2).next_to(f_tex, DOWN, buff=0.2)
        func = lambda x: self.a**x
        f = plane.plot(func, color=self.color)

        verify_translated = self.translate("Func_6_2.I3.verify")
        verify = VGroup(Tex("$\\Rightarrow$", verify_translated, color=c1t, font_size=fs3), MathTex(f"f({self.x_max})", f"={self.a}^{self.x_max}", f"={self.a**self.x_max}", font_size=fs3, color=c1t))
        verify.arrange(DOWN, buff=0.2).next_to(sol, DOWN, buff=0.8)
        verify[0].shift(LEFT*0.6)

        self.add(f_tex)

        # Action Sequence
        with self.voiceover(
                text=self.evaluate_string(self.translate("Func_6_2.GraphToGrowthFactorAnswerScene.voiceover"))
        ) as tracker:
            
            self.play(Write(self.cords))
            self.play(Write(f))

            self.wait_until_bookmark("x_one")
            cursor.blinking=False
            x,y,_ = plane.c2p(1,0)
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("f_x_one")
            x,y,_ = plane.c2p(1,self.a)
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("sol")
            cursor.blinking=False
            x,y,_ = sol[1].get_center()+0.4*DOWN
            self.play(Write(sol), CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("verify")
            x,y,_ = verify[0].get_center()+0.4*DOWN
            cursor.blinking=False
            self.play(Write(verify[0]), CursorMoveTo(cursor,x,y), run_time=0.5)
            cursor.blinking=False

            self.wait_until_bookmark("x_max")
            cursor.blinking=False
            x,y,_ = verify[1][0].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), Write(verify[1][0]), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("x_max_graph")
            cursor.blinking=False
            x,y,_ = plane.c2p(self.x_max,self.a**self.x_max)
            self.play(CursorMoveTo(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("verify_2")
            cursor.blinking=False
            x,y,_ = verify[1][1].get_center()+0.4*DOWN
            self.play(Write(verify[1][1]), CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("verify_3")
            x,y,_ = verify[1][2].get_center()+0.4*DOWN
            self.play(Write(verify[1][2]), CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

        self.wait(4)


#####################################
#####################################
class GrowthFactorToGraphQuestionScene(SophiaCursorScene, metaclass = ABCMeta):

    # Main method for constructing the animation
    @abstractmethod
    def construct(self):
        # Adding initial components to the scene
        super().construct()
        self.add_mathgrid()

        title = self.add_title(self.translate("Func_6_2.I3.title"))

        plane = self.cords[0]

        def cursor_sound_updater(mob, dt):
            if mob.needSound:
                mob.needSound = False
                self.add_cursor_sound()
        cursor = AltCursor(stroke_width=0.0, blinking=True)
        cursor.autoFadeBackground = True
        cursor.add_updater(cursor_sound_updater)
        self.add(cursor)

        f_tex = MathTex("f","(x)", "=", str(self.a), "^x", color=c1t, font_size=fs2).next_to(plane, DOWN, buff=0.4)
        xm1, xm2 = self.translate("Func_6_2.GrowthFactorToGraphQuestionScene.x-minutes_1"), self.translate("Func_6_2.GrowthFactorToGraphQuestionScene.x-minutes_2")
        x_minutes = VGroup(Tex("$\\Rightarrow$", xm1, color=c1t, font_size=fs3), Tex(xm2, color=c1t, font_size=fs3)).arrange(DOWN, buff=0.1, aligned_edge=RIGHT).next_to(f_tex, DOWN, buff=0.6)
        x_minutes[1].shift(RIGHT*0.4)
        g_1 = plane.plot(self.f1, color=self.c1)
        g_2 = plane.plot(self.f2, color=self.c2)
        g_3 = plane.plot(self.f3, color=self.c3)

        # Action Sequence
        with self.voiceover(
                text=self.evaluate_string(self.translate("Func_6_2.GrowthFactorToGraphQuestionScene.voiceover"))
        ) as tracker:
            
            self.wait_until_bookmark("f")
            x,y,_ = f_tex[0].get_center()+0.4*DOWN
            cursor.blinking=False
            self.play(Write(f_tex), CursorMoveTo(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fx")
            x,y,_ = f_tex[1].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("fa")
            x,y,_ = f_tex[3].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("xx")
            x,y,_ = f_tex[4].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("which")
            x,y,_ = x_minutes[1].get_center()+0.4*DOWN
            cursor.blinking=False
            self.play(Write(x_minutes), CursorMoveTo(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("cords_in")
            self.play(Write(self.cords), run_time=0.3)

            self.wait_until_bookmark("plot_1")
            cursor.blinking=False
            x,y,_ = g_1.get_start()
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            self.add(cursor.copy()._start_fading(2).add_updater(lambda m: m.move_to(g_1.get_end())))
            self.add_pencil_sound(1.5)
            self.play(Create(g_1))
            cursor.blinking=True

            self.wait_until_bookmark("plot_2")
            cursor.blinking=False
            x,y,_ = g_2.get_start()
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            self.add(cursor.copy()._start_fading(2).add_updater(lambda m: m.move_to(g_2.get_end())))
            self.add_pencil_sound(1.5)
            self.play(Create(g_2))
            cursor.blinking=True

            self.wait_until_bookmark("plot_3")
            cursor.blinking=False
            x,y,_ = g_3.get_start()
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.3)
            self.add(cursor.copy()._start_fading(2).add_updater(lambda m: m.move_to(g_3.get_end())))
            self.add_pencil_sound(1.5)
            self.play(Create(g_3))
            cursor.blinking=True
            

        self.wait(4)


class GrowthFactorToGraphAnswerScene(SophiaCursorScene, metaclass=ABCMeta):

    # Main method for constructing the animation
    @abstractmethod
    def construct(self):
        # Adding initial components to the scene
        super().construct()
        self.add_mathgrid()

        title = self.add_title(self.translate("Func_6_2.I3.title"))

        plane = self.cords[0]
        f_tex = MathTex("f","(x)", "=", str(self.a), "^x", color=c1t, font_size=fs2).next_to(plane, DOWN, buff=0.4)
        self.intro_auto = self.translate("Func_6_2.GrowthFactorToGraphAnswerScene.i1") if self.a>1 else self.translate("Func_6_2.GrowthFactorToGraphAnswerScene.i2")
        intro_auto_tex = Tex("$a>1$",f"$\\Rightarrow${self.translate('Func_6_2.GrowthFactorToGraphAnswerScene.eg')}", color=c1t, font_size=fs3).next_to(f_tex, DOWN, buff=0.4) if self.a>1 else Tex("$0<a<1$",f"$\\Rightarrow${self.translate('Func_6_2.GrowthFactorToGraphAnswerScene.ed')}", color=c1t, font_size=fs3).next_to(f_tex, DOWN, buff=0.4)
        
        g_1 = plane.plot(self.f1, color=self.c1)
        g_2 = plane.plot(self.f2, color=self.c2)
        g_3 = plane.plot(self.f3, color=self.c3)

        gs = [g_1,g_2,g_3]
        g_correct = gs[self.idx_correct]
        self.color_correct = self.color_1_name if self.idx_correct==0 else self.color_2_name if self.idx_correct==1 else self.color_3_name


        def cursor_sound_updater(mob, dt):
            if mob.needSound:
                mob.needSound = False
                self.add_cursor_sound()
        cursor = AltCursor(stroke_width=0.0, blinking=True)
        cursor.autoFadeBackground = True
        cursor.add_updater(cursor_sound_updater)
        self.add(cursor)

        # Action Sequence
        with self.voiceover(
                text=self.evaluate_string(self.translate("Func_6_2.GrowthFactorToGraphAnswerScene.voiceover"))
        ) as tracker:
            
            self.play(Write(f_tex))

            self.wait_until_bookmark("intro_auto")
            x,y,_ = intro_auto_tex[0].get_center()+0.4*DOWN
            cursor.blinking=False
            self.play(Write(intro_auto_tex), CursorMoveTo(cursor,x,y), run_time=0.3)
            cursor.blinking=True

            self.wait_until_bookmark("cords_in")
            self.play(Write(self.cords), run_time=0.3)

            self.wait_until_bookmark("x_one")
            cursor.blinking=False
            x,y,_ = plane.c2p(1,0)
            self.play(CursorMoveTo(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("f_x_one")
            x,y,_ = plane.c2p(1,self.a)
            self.play(CursorMoveTo(cursor,x,y), run_time=0.3)
            point_1 = cursor.copy().clear_updaters()
            self.add(point_1)

            self.wait_until_bookmark("x_two")
            x,y,_ = plane.c2p(2,0)
            self.play(CursorMoveTo(cursor,x,y), run_time=0.3)

            self.wait_until_bookmark("f_x_two")
            x,y,_ = plane.c2p(2,self.a**2)
            self.play(CursorMoveTo(cursor,x,y), run_time=0.3)
            point_2 = cursor.copy().clear_updaters()
            self.add(point_2)

            self.wait_until_bookmark("x_max")
            x,y,_ = plane.c2p(self.x_max,0)
            self.play(CursorMoveTo(cursor,x,y), run_time=0.3)
            
            self.wait_until_bookmark("f_x_max")
            x,y,_ = plane.c2p(self.x_max,self.a**self.x_max)
            self.play(CursorMoveTo(cursor,x,y), run_time=0.3)
            point_3 = cursor.copy().clear_updaters()
            self.add(point_3)

            self.wait_until_bookmark("plot")
            cursors = [cursor.copy() for _ in range(3)]
            locs = [g.get_start() for g in gs]
            x,y,_ = plane.c2p(0,0)
            self.play(*[CursorMoveTo(c,l[0], l[1]) for c,l in zip(cursors,locs)], CursorMoveTo(cursor,x,y), run_time=1)
            cursors[1]._start_fading(2).add_updater(lambda m: m.move_to(g_1.get_end()))
            cursors[2]._start_fading(2).add_updater(lambda m: m.move_to(g_2.get_end()))
            cursors[0]._start_fading(2).add_updater(lambda m: m.move_to(g_3.get_end()))
            self.add_pencil_sound(1.5)
            self.play(*[Create(g) for g in gs])
            cursor.blinking=True

            self.wait_until_bookmark("erase")
            self.add(g_correct.copy())
            self.play(Uncreate(g_1), Uncreate(g_2), Uncreate(g_3),  run_time=0.3)


        self.wait(4)


#####################################
#####################################
######## Specific Qs ################
#####################################
#####################################

#####################################
#####################################
class Func_6_2_P_1_q(GraphToGrowthFactorQuestionScene):

    def task_definition(self) -> SophiaTaskDefinition:
        return SophiaTaskDefinition(
            answerOptions = ["$a=3$", "$a=1$", "$a=\frac{1}{3}$", "$a=-2$"],
            correctAnswerIndex = 2,
            questionText=self.translate("Func_6_2_P_1_q.questionText")
        )

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 81, 9], x_ticks=[1,2,3,4], y_ticks=[27,54,81])
        self.a = 3
        self.color=PURPLE
        self.intro = self.translate("Func_6_2_P_1_q.intro")

        super().construct()

class Func_6_2_P_1_a(GraphToGrowthFactorAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 81, 9], x_ticks=[1,2,3,4], y_ticks=[27,54,81])
        self.a = 3
        self.x_max = 4
        self.color=PURPLE
        self.intro = self.translate("Func_6_2_P_1_a.intro")

        super().construct()

class Func_6_2_P_1_b(GraphToGrowthFactorAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 81, 9], x_ticks=[1,2,3,4], y_ticks=[27,54,81])
        self.a = 3
        self.x_max = 4
        self.color=PURPLE
        self.intro = self.translate("Func_6_2_P_1_b.intro")

        super().construct()

class Func_6_2_P_1_c(GraphToGrowthFactorAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 81, 9], x_ticks=[1,2,3,4], y_ticks=[27,54,81])
        self.a = 3
        self.x_max = 4
        self.color=PURPLE
        self.intro = self.translate("Func_6_2_P_1_b.intro")

        super().construct()

class Func_6_2_P_1_d(GraphToGrowthFactorAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 81, 9], x_ticks=[1,2,3,4], y_ticks=[27,54,81])
        self.a = 3
        self.x_max = 4
        self.color=PURPLE
        self.intro = self.translate("Func_6_2_P_1_b.intro")

        super().construct()


#####################################
#####################################
class Func_6_2_P_2_q(GrowthFactorToGraphQuestionScene):

    def task_definition(self) -> SophiaTaskDefinition:
        return SophiaTaskDefinition(
            answerOptions=ast.literal_eval(self.translate("Func_6_2.P2.q.answer-options")),
            correctAnswerIndex=0,
            questionText=self.translate("Func_6_2.P2.q.questionText")
        )

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 81, 9], x_ticks=[1,2,3,4], y_ticks=[27,54,81])
        self.a = 2
        self.color=PURPLE
        self.intro = self.translate("Func_6_2_P_2_q.intro")

        self.f1 = lambda x: self.a**x
        self.f2 = lambda x: x**3
        self.f3 = lambda x: 50/(self.a**x)

        self.color_1_name = self.translate("Func_6_2_P_2_q.color_1_name")
        self.color_2_name = self.translate("Func_6_2_P_2_q.color_2_name")
        self.color_3_name = self.translate("Func_6_2_P_2_q.color_3_name")

        self.c1 = PURPLE
        self.c2 = BLUE
        self.c3 = GREEN

        super().construct()

class Func_6_2_P_2_a(GrowthFactorToGraphAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 81, 9], x_ticks=[1,2,3,4], y_ticks=[27,54,81])
        self.x_max = 4
        self.a = 2
        self.color=PURPLE
        self.intro = self.translate("Func_6_2_P_2_a.intro")

        self.f1 = lambda x: self.a**x
        self.f2 = lambda x: x**3
        self.f3 = lambda x: 50/(self.a**x)

        self.color_1_name = self.translate("Func_6_2_P_2_q.color_1_name")
        self.color_2_name = self.translate("Func_6_2_P_2_q.color_2_name")
        self.color_3_name = self.translate("Func_6_2_P_2_q.color_3_name")

        self.c1 = PURPLE
        self.c2 = BLUE
        self.c3 = GREEN

        self.idx_correct = 0

        super().construct()

class Func_6_2_P_2_b(GrowthFactorToGraphAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 81, 9], x_ticks=[1,2,3,4], y_ticks=[27,54,81])
        self.x_max = 4
        self.a = 2
        self.color=PURPLE
        self.intro = self.translate("Func_6_2_P_2_b.intro")

        self.f1 = lambda x: self.a**x
        self.f2 = lambda x: x**3
        self.f3 = lambda x: 50/(self.a**x)

        self.color_1_name = self.translate("Func_6_2_P_2_q.color_1_name")
        self.color_2_name = self.translate("Func_6_2_P_2_q.color_2_name")
        self.color_3_name = self.translate("Func_6_2_P_2_q.color_3_name")

        self.c1 = PURPLE
        self.c2 = BLUE
        self.c3 = GREEN

        self.idx_correct = 0

        super().construct()

class Func_6_2_P_2_c(GrowthFactorToGraphAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 81, 9], x_ticks=[1,2,3,4], y_ticks=[27,54,81])
        self.x_max = 4
        self.a = 2
        self.color=PURPLE
        self.intro = self.translate("Func_6_2_P_2_b.intro")

        self.f1 = lambda x: self.a**x
        self.f2 = lambda x: x**3
        self.f3 = lambda x: 50/(self.a**x)

        self.color_1_name = self.translate("Func_6_2_P_2_q.color_1_name")
        self.color_2_name = self.translate("Func_6_2_P_2_q.color_2_name")
        self.color_3_name = self.translate("Func_6_2_P_2_q.color_3_name")

        self.c1 = PURPLE
        self.c2 = BLUE
        self.c3 = GREEN

        self.idx_correct = 0

        super().construct()


#####################################
#####################################
class Func_6_2_P_3_q(GraphToGrowthFactorQuestionScene):

    def task_definition(self) -> SophiaTaskDefinition:
        return SophiaTaskDefinition(
            answerOptions = ["$a=3$", "$a=2$", "$a=\frac{1}{2}$", "$a=-2$"],
            correctAnswerIndex = 1,
            questionText=self.translate("Func_6_2.P3.q.question-text")
        )

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 16, 4], x_ticks=[1,2,3,4], y_ticks=[4,8,12,16])
        self.a = 2
        self.color=GREEN
        self.intro = self.translate("Func_6_2_P_3_q.intro")

        super().construct()

class Func_6_2_P_3_a(GraphToGrowthFactorAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 16, 4], x_ticks=[1,2,3,4], y_ticks=[4,8,12,16])
        self.a = 2
        self.x_max = 4
        self.color=GREEN
        self.intro = self.translate("Func_6_2_P_3_a.intro")

        super().construct()

class Func_6_2_P_3_b(GraphToGrowthFactorAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 16, 4], x_ticks=[1,2,3,4], y_ticks=[4,8,12,16])
        self.a = 2
        self.x_max = 4
        self.color=GREEN
        self.intro = self.translate("Func_6_2_P_3_b.intro")

        super().construct()

class Func_6_2_P_3_c(GraphToGrowthFactorAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 16, 4], x_ticks=[1,2,3,4], y_ticks=[4,8,12,16])
        self.a = 2
        self.x_max = 4
        self.color=GREEN
        self.intro = self.translate("Func_6_2_P_3_a.intro")

        super().construct()

class Func_6_2_P_3_d(GraphToGrowthFactorAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 16, 4], x_ticks=[1,2,3,4], y_ticks=[4,8,12,16])
        self.a = 2
        self.x_max = 4
        self.color=GREEN
        self.intro = self.translate("Func_6_2_P_3_a.intro")

        super().construct()


#####################################
#####################################
class Func_6_2_P_4_q(GrowthFactorToGraphQuestionScene):

    def task_definition(self) -> SophiaTaskDefinition:
        return SophiaTaskDefinition(
            answerOptions=ast.literal_eval(self.translate("Func_6_2.P4.q.answer-options")),
            correctAnswerIndex=2,
            questionText=self.translate("Func_6_2.P4.q.question-text")
        )

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 1, 0.25], x_ticks=[1,2,3,4], y_ticks=[0.25,0.5,0.75,1])
        self.a = 1/2
        self.intro = self.translate("Func_6_2_P_4_q.intro")

        self.f1 = lambda x: (4-self.a)**x
        self.f2 = lambda x: x/4
        self.f3 = lambda x: self.a**x

        self.color_1_name = self.translate("Func_6_2_P_4_q.color_1_name")
        self.color_2_name = self.translate("Func_6_2_P_4_q.color_2_name")
        self.color_3_name = self.translate("Func_6_2_P_4_q.color_3_name")

        self.c1 = BLUE
        self.c2 = GREEN
        self.c3 = ORANGE

        super().construct()

class Func_6_2_P_4_a(GrowthFactorToGraphAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 1, 0.25], x_ticks=[1,2,3,4], y_ticks=[0.25,0.5,0.75,1])
        self.x_max = 4
        self.a = 1/2
        self.intro = self.translate("Func_6_2_P_4_a.intro")

        self.f1 = lambda x: (4-self.a)**x
        self.f2 = lambda x: x/4
        self.f3 = lambda x: self.a**x

        self.color_1_name = self.translate("Func_6_2_P_4_q.color_1_name")
        self.color_2_name = self.translate("Func_6_2_P_4_q.color_2_name")
        self.color_3_name = self.translate("Func_6_2_P_4_q.color_3_name")

        self.c1 = BLUE
        self.c2 = GREEN
        self.c3 = ORANGE

        self.idx_correct = 2

        super().construct()

class Func_6_2_P_4_b(GrowthFactorToGraphAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 1, 0.25], x_ticks=[1,2,3,4], y_ticks=[0.25,0.5,0.75,1])
        self.x_max = 4
        self.a = 1/2
        self.intro = self.translate("Func_6_2_P_4_a.intro")

        self.f1 = lambda x: (4-self.a)**x
        self.f2 = lambda x: x/4
        self.f3 = lambda x: self.a**x

        self.color_1_name = self.translate("Func_6_2_P_4_q.color_1_name")
        self.color_2_name = self.translate("Func_6_2_P_4_q.color_2_name")
        self.color_3_name = self.translate("Func_6_2_P_4_q.color_3_name")

        self.c1 = BLUE
        self.c2 = GREEN
        self.c3 = ORANGE

        self.idx_correct = 2

        super().construct()

class Func_6_2_P_4_c(GrowthFactorToGraphAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 1, 0.25], x_ticks=[1,2,3,4], y_ticks=[0.25,0.5,0.75,1])
        self.x_max = 4
        self.a = 1/2
        self.intro = self.translate("Func_6_2_P_4_c.intro")

        self.f1 = lambda x: (4-self.a)**x
        self.f2 = lambda x: x/4
        self.f3 = lambda x: self.a**x

        self.color_1_name = self.translate("Func_6_2_P_4_q.color_1_name")
        self.color_2_name = self.translate("Func_6_2_P_4_q.color_2_name")
        self.color_3_name = self.translate("Func_6_2_P_4_q.color_3_name")
        self.c1 = BLUE
        self.c2 = GREEN
        self.c3 = ORANGE

        self.idx_correct = 2

        super().construct()

#####################################
#####################################
class Func_6_2_P_5_q(GraphToGrowthFactorQuestionScene):

    def task_definition(self) -> SophiaTaskDefinition:
        return SophiaTaskDefinition(
            answerOptions = ["$a=4$", "$a=2$", "$a=3$", "$a=-2$"],
            correctAnswerIndex = 0,
            questionText=self.translate("Func_6_2.P5.q.question-text")
        )

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 256, 64], x_ticks=[1,2,3,4], y_ticks=[64,128,192,256])
        self.a = 4
        self.color=PINK
        self.intro = self.translate("Func_6_2_P_5_q.intro")

        super().construct()

class Func_6_2_P_5_a(GraphToGrowthFactorAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 256, 64], x_ticks=[1,2,3,4], y_ticks=[64,128,192,256])
        self.a = 4
        self.x_max = 4
        self.color=PINK
        self.intro = self.translate("Func_6_2_P_5_a.intro")

        super().construct()

class Func_6_2_P_5_b(GraphToGrowthFactorAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 256, 64], x_ticks=[1,2,3,4], y_ticks=[64,128,192,256])
        self.a = 4
        self.x_max = 4
        self.color=PINK
        self.intro = self.translate("Func_6_2_P_5_b.intro")

        super().construct()

class Func_6_2_P_5_c(GraphToGrowthFactorAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 256, 64], x_ticks=[1,2,3,4], y_ticks=[64,128,192,256])
        self.a = 4
        self.x_max = 4
        self.color=PINK
        self.intro = self.translate("Func_6_2_P_5_b.intro")

        super().construct()

class Func_6_2_P_5_d(GraphToGrowthFactorAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 256, 64], x_ticks=[1,2,3,4], y_ticks=[64,128,192,256])
        self.a = 4
        self.x_max = 4
        self.color=PINK
        self.intro = self.translate("Func_6_2_P_5_b.intro")

        super().construct()


#####################################
#####################################
class Func_6_2_P_6_q(GrowthFactorToGraphQuestionScene):

    def task_definition(self) -> SophiaTaskDefinition:
        return SophiaTaskDefinition(
            answerOptions=ast.literal_eval(self.translate("Func_6_2.P6.q.answer-options")),
            correctAnswerIndex=1,
            questionText=self.translate("Func_6_2.P6.q.question-text")
        )

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 81, 9], x_ticks=[1,2,3,4], y_ticks=[27,54,81])
        self.a = 3
        self.intro = self.translate("Func_6_2_P_6_q.intro")

        self.f1 = lambda x: x**2
        self.f2 = lambda x: self.a**x
        self.f3 = lambda x: self.a**(4-x)

        self.color_1_name = self.translate("Func_6_2_P_6_q.color_1_name")
        self.color_2_name = self.translate("Func_6_2_P_6_q.color_2_name")
        self.color_3_name = self.translate("Func_6_2_P_6_q.color_3_name")

        self.c1 = PURPLE
        self.c2 = BLUE
        self.c3 = PINK

        super().construct()

class Func_6_2_P_6_a(GrowthFactorToGraphAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 81, 9], x_ticks=[1,2,3,4], y_ticks=[27,54,81])
        self.x_max = 4
        self.a = 3
        self.intro = self.translate("Func_6_2_P_6_a.intro")

        self.f1 = lambda x: x**2
        self.f2 = lambda x: self.a**x
        self.f3 = lambda x: self.a**(4-x)

        self.color_1_name = self.translate("Func_6_2_P_6_q.color_1_name")
        self.color_2_name = self.translate("Func_6_2_P_6_q.color_2_name")
        self.color_3_name = self.translate("Func_6_2_P_6_q.color_3_name")

        self.c1 = PURPLE
        self.c2 = BLUE
        self.c3 = PINK

        self.idx_correct = 1

        super().construct()

class Func_6_2_P_6_b(GrowthFactorToGraphAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 81, 9], x_ticks=[1,2,3,4], y_ticks=[27,54,81])
        self.x_max = 4
        self.a = 3
        self.intro = self.translate("Func_6_2_P_6_b.intro")

        self.f1 = lambda x: x**2
        self.f2 = lambda x: self.a**x
        self.f3 = lambda x: self.a**(4-x)

        self.color_1_name = self.translate("Func_6_2_P_6_q.color_1_name")
        self.color_2_name = self.translate("Func_6_2_P_6_q.color_2_name")
        self.color_3_name = self.translate("Func_6_2_P_6_q.color_3_name")

        self.c1 = PURPLE
        self.c2 = BLUE
        self.c3 = PINK

        self.idx_correct = 1

        super().construct()

class Func_6_2_P_6_c(GrowthFactorToGraphAnswerScene):

    def construct(self):

        self.cords = self.add_cords([0, 4, 1], [0, 81, 9], x_ticks=[1,2,3,4], y_ticks=[27,54,81])
        self.x_max = 4
        self.a = 3
        self.intro = self.translate("Func_6_2_P_6_a.intro")

        self.f1 = lambda x: x**2
        self.f2 = lambda x: self.a**x
        self.f3 = lambda x: self.a**(4-x)

        self.color_1_name = self.translate("Func_6_2_P_6_q.color_1_name")
        self.color_2_name = self.translate("Func_6_2_P_6_q.color_2_name")
        self.color_3_name = self.translate("Func_6_2_P_6_q.color_3_name")

        self.c1 = PURPLE
        self.c2 = BLUE
        self.c3 = PINK

        self.idx_correct = 1

        super().construct()



PROTOTYPES=[
    PagePrototypeVideo.from_scene(Func_6_2_I_1),
    PagePrototypeVideo.from_scene(Func_6_2_I_2_q),
    PagePrototypeQuestion.from_scene(Func_6_2_I_2_q),
    PagePrototypeVideo.from_scene(Func_6_2_I_2_a),
    PagePrototypeVideo.from_scene(Func_6_2_I_2_b),
    PagePrototypeVideo.from_scene(Func_6_2_I_2_c),
    PagePrototypeVideo.from_scene(Func_6_2_I_2_d),
    PagePrototypeVideo.from_scene(Func_6_2_I_3),
    PagePrototypeVideo.from_scene(Func_6_2_P_1_q),
    PagePrototypeQuestion.from_scene(Func_6_2_P_1_q),
    PagePrototypeVideo.from_scene(Func_6_2_P_1_a),
    PagePrototypeVideo.from_scene(Func_6_2_P_1_b),
    PagePrototypeVideo.from_scene(Func_6_2_P_1_c),
    PagePrototypeVideo.from_scene(Func_6_2_P_1_d),
    PagePrototypeVideo.from_scene(Func_6_2_P_2_q),
    PagePrototypeQuestion.from_scene(Func_6_2_P_2_q),
    PagePrototypeVideo.from_scene(Func_6_2_P_2_a),
    PagePrototypeVideo.from_scene(Func_6_2_P_2_b),
    PagePrototypeVideo.from_scene(Func_6_2_P_2_c),
    PagePrototypeVideo.from_scene(Func_6_2_P_3_q),
    PagePrototypeQuestion.from_scene(Func_6_2_P_3_q),
    PagePrototypeVideo.from_scene(Func_6_2_P_3_a),
    PagePrototypeVideo.from_scene(Func_6_2_P_3_b),
    PagePrototypeVideo.from_scene(Func_6_2_P_3_c),
    PagePrototypeVideo.from_scene(Func_6_2_P_3_d),
    PagePrototypeVideo.from_scene(Func_6_2_P_4_q),
    PagePrototypeQuestion.from_scene(Func_6_2_P_4_q),
    PagePrototypeVideo.from_scene(Func_6_2_P_4_a),
    PagePrototypeVideo.from_scene(Func_6_2_P_4_b),
    PagePrototypeVideo.from_scene(Func_6_2_P_4_c),
    PagePrototypeVideo.from_scene(Func_6_2_P_5_q),
    PagePrototypeQuestion.from_scene(Func_6_2_P_5_q),
    PagePrototypeVideo.from_scene(Func_6_2_P_5_a),
    PagePrototypeVideo.from_scene(Func_6_2_P_5_b),
    PagePrototypeVideo.from_scene(Func_6_2_P_5_c),
    PagePrototypeVideo.from_scene(Func_6_2_P_5_d),
    PagePrototypeVideo.from_scene(Func_6_2_P_6_q),
    PagePrototypeQuestion.from_scene(Func_6_2_P_6_q),
    PagePrototypeVideo.from_scene(Func_6_2_P_6_a),
    PagePrototypeVideo.from_scene(Func_6_2_P_6_b),
    PagePrototypeVideo.from_scene(Func_6_2_P_6_c),
]