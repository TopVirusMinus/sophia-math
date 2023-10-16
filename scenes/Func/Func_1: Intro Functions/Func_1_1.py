# Import necessary libraries and modules
from abc import ABCMeta, abstractmethod
from sophialib.page_prototypes.prototype import PagePrototypeQuestion, PagePrototypeVideo
from sophialib.styles.sophiascene import (CursorMoveToCurved, CursorPositionTracker,
                                          CursorPositionTracking,
                                          CursorResizeDefault, SophiaScene, SophiaQuestionInfo,
                                          assets_folder, AltCursor,
                                          SophiaCursorScene, CursorMoveTo,
                                          CursorMoveResize, Notepad, Bubble, CursorMarkAxis)
from sophialib.styles.styleconstants import *
from sophialib.styles.sophiaobjects import *
from manim import *
from PIL import Image
import numpy as np
from pathlib import Path
from sophialib.tasks.sophiataskdefinition import SophiaTaskDefinition

##################################################################

# Function to create piecewise linear function based on given points
def create_piecewise_linear(points):
    def piecewise_linear(x):
        # Sort the points based on x-coordinate
        sorted_points = sorted(points, key=lambda p: p[0])

        # Find the closest two points for interpolation
        left_point, right_point = None, None
        for point in sorted_points:
            if x < point[0]:
                right_point = point
                break
            left_point = point

        # Extrapolate if x is outside the range of points
        if right_point is None:
            return sorted_points[-1][1]
        if left_point is None:
            return sorted_points[0][1]

        # Linear interpolation
        x1, y1 = left_point
        x2, y2 = right_point
        slope = (y2 - y1) / (x2 - x1)
        interpolated_value = y1 + slope * (x - x1)

        return interpolated_value

    return piecewise_linear


#####################################
#####################################

class Func_1_1_I_1_q(SophiaCursorScene, SophiaQuestionInfo):

    def task_definition(self) -> SophiaTaskDefinition:
        return SophiaTaskDefinition(
            answerOptions = [self.translate("Func_1_1.1I1q.question.the-blue-representation"), self.translate("Func_1_1.1I1q.question.the-red-representation")],
            correctAnswerIndex = 0,
            questionText = self.translate("Func_1_1.1I1q.question.which-representation-describes-a-realistic-temperature-trend") 
        )


    # Main method for constructing the animation
    def construct(self):
        # Adding initial components to the scene
        super().construct()
        self.add_mathgrid()

        # Load and position images
        picnic = ImageMobject(assets_folder / "img" / "picnic.png")
        picnic = picnic.scale(3.5/picnic.get_width()).move_to([-5.2, 1, 0])
        wetter = ImageMobject(assets_folder / "img" / "weatherreport.png")
        wetter = wetter.scale(3.5/wetter.get_width()).move_to([-5, 1, 0])
        q = ImageMobject(assets_folder / "img" / "qmark.png")
        q = q.scale(2.5/q.get_width()).move_to([-5.2, 1, 0])

        # Create a notepad with texts

        # Create the coordinate system
        cords = self.add_cords([6, 24, 3], [5, 25, 5], x_ticks=[6, 12, 18, 24], y_ticks=[10, 15, 20, 25],
                               x_labels=[6, 12, 18, 24], y_labels=[5, 10, 15, 20, 25]).shift(DOWN*1.4)
        plane = cords[0]
        # self.add(cords)

        # Add title to the scene
        self.add_title(self.translate("Func_1_1.1I1q.main.title"))

        # Create and plot piecewise linear function
        func = create_piecewise_linear([[6, 9], [8, 12], [10, 17], [12, 19], [14, 22], [16, 18], [18, 13], [20, 11], [22, 8], [24, 7]])
        func_plotted = plane.plot(func, color=BLUE)
        func_plotted_wrong = plane.plot(func, color=RED).rotate(90 * DEGREES)

        # Initialize a cursor
        xo, yo, _ = plane.x_axis.n2p(6)
        cursor = AltCursor(stroke_width=0.0)
        cursor.autoFadeBackground = True
        cursor.move_to([xo, yo, 0])
        cursor.add_updater(lambda m, dt: self.bring_to_front(cursor))


        # Action Sequence
        with self.voiceover(
                text=self.translate("Func_1_1.1I1q.main.voiceover")
        ) as tracker:
            
            self.add_shift_sound(0.5)
            self.play(q.animate.shift(RIGHT*5), run_time=0.5)

            self.wait_until_bookmark("qOut")
            self.add_shift_sound(0.5)
            self.play(q.animate.shift(RIGHT*5), run_time=0.5)

            # Animate the picnic image moving to the right.
            self.wait_until_bookmark("picnicIn")
            self.add_shift_sound(0.5)
            self.play(picnic.animate.shift(RIGHT*5), run_time=0.5)

            # Animate the wetter image moving to the right.
            self.wait_until_bookmark("WetterIn")
            self.add_shift_sound(0.5)
            self.play(wetter.animate.shift(RIGHT*5), picnic.animate.shift(RIGHT*5), run_time=0.5)

            # Change note colors to highlight first Block and animate wetter image moving out while writing cords.
            self.wait_until_bookmark("CordsInWetterOut")
            self.add_shift_sound(0.5)
            self.play(wetter.animate(run_time=0.5).shift(RIGHT*5), Write(cords), run_time=0.8)
            cursor.idle = True

            # Highlight the x-axis using the cursor
            self.wait_until_bookmark("ShowXAxis")
            cursor.idle = False
            self.add_move_sound("forward", duration = 0.5, target_volume=0.1)
            self.play(CursorMoveResize(cursor, plane.x_axis.n2p(15)[0], yo, 2.6, 0.3), run_time=0.5)

            # Highlight the y-axis using the cursor
            self.wait_until_bookmark("ShowYAxis")
            self.add_move_sound("forward", duration = 0.5, target_volume=0.1)
            self.play(CursorMoveResize(cursor, xo, plane.y_axis.n2p(15)[1], 0.3, 2.6), run_time=0.5)

            # Reset the cursor size and position after "ResetCursor1" bookmark.
            self.wait_until_bookmark("ResetCursor1")
            self.add_move_sound("backward", duration = 0.5, target_volume=0.1)
            self.play(CursorMoveResize(cursor, xo, yo, 0.2, 0.2), run_time=0.5)
            cursor.idle=True

            # Draw the blue function plot after "BlueFuncIn" bookmark.
            self.wait_until_bookmark("BlueFuncIn")
            cursor.idle = False
            x,y,_ = func_plotted.get_start()
            self.play(CursorMoveTo(cursor,x,y), run_time=.3)
            self.add(cursor.copy().add_updater(lambda m: m.move_to(func_plotted.get_end()))._start_fading(1.5))
            self.add_pencil_sound(1)
            cursor.set_opacity(c_bg_opacity)
            self.play(Create(func_plotted), run_time=1)

            # Draw the red function plot (incorrect one) after "RedFuncIn" bookmark.
            self.wait_until_bookmark("RedFuncIn")
            x,y,_ = func_plotted_wrong.get_start()
            cursor.set_opacity(c_fg_opacity)
            self.play(CursorMoveTo(cursor,x,y), run_time=.3)
            self.add(cursor.copy().add_updater(lambda m: m.move_to(func_plotted_wrong.get_end()))._start_fading(1.5))
            self.add_pencil_sound(1)
            cursor.idle=True
            self.play(Create(func_plotted_wrong), run_time=1)


        # Wait for 4 seconds at the end of animation
        self.wait(4)



class Func_1_1_I_1_a(SophiaCursorScene):

    # Main method for constructing the animation
    def construct(self):
        # Adding initial components to the scene
        super().construct()
        self.add_mathgrid()


        # Create the coordinate system
        cords = self.add_cords([6, 24, 3], [5, 25, 5], x_ticks=[6, 12, 18], y_ticks=[10, 15, 20, 25], axisLabelX=self.translate("Func_1_1.1I1a.main.x-axis"), axisLabelY=self.translate("Func_1_1.1I1a.main.y-axis")).shift(DOWN*1.4)
        plane = cords[0]


        # Add title to the scene
        self.add_title(self.translate("Func_1_1.1I1a.main.title"))

        # Create and plot piecewise linear function
        func = create_piecewise_linear([[6, 9], [8, 12], [10, 17], [12, 19], [14, 22], [16, 18], [18, 13], [20, 11], [22, 8], [24, 7]])
        func_plotted = plane.plot(func, color=BLUE)
        func_plotted_wrong = plane.plot(func, color=RED).rotate(90 * DEGREES)

        # Initialize a cursor
        xo, yo, _ = plane.c2p(6,9)
        cursor = AltCursor(stroke_width=0.0)
        cursor.autoFadeBackground = True
        cursor.move_to([xo, yo, 0])
        cursor.add_updater(lambda m, dt: self.bring_to_front(cursor))

        # Action Sequence
        with self.voiceover(
                text=self.translate("Func_1_1.1I1_correct.main.voiceover")
        ) as tracker:
            
            # Animate the coordinate system being created
            self.play(Write(cords), run_time=0.5)
            self.add(cursor)

            # Draw the blue function plot after "BlueFuncIn" bookmark.
            self.wait_until_bookmark("BlueFuncIn")
            self.add_pencil_sound(1.5)
            cursor.idle=False
            c2 = cursor.copy().add_updater(lambda m: m.move_to(func_plotted.get_end()))._start_fading(1.5)
            self.add(c2)
            self.play(Write(func_plotted))

            # Follow the function with the cursor
            self.wait_until_bookmark("MoveAlongFunc")
            self.play(MoveAlongPath(cursor, func_plotted), run_time=14, rate_func=linear)
            cursor.idle=True

            # Draw the red function plot (incorrect one) after "RedFuncIn" bookmark.
            self.wait_until_bookmark("RedFuncIn")
            self.play(Unwrite(func_plotted))
            self.wait(0.2)
            self.add_pencil_sound(1.5)
            self.play(Write(func_plotted_wrong))

            self.wait_until_bookmark("notRed")
            x1, y1, _ = plane.c2p(14, 5)
            cursor.idle=False
            self.play(CursorMoveTo(cursor, x1, y1), run_time=0.5)
            cursor.idle=True

            self.wait_until_bookmark("VertLine")
            l = Line([x1, y1, 0], [x1, y1 + 2.4, 0], stroke_width=1.5, color=BLACK)
            self.add_pencil_sound(3)
            self.play(Write(l), run_time=3)

            self.wait_until_bookmark("intersect1")
            x1, y1, _ = plane.c2p(14, 8)
            cursor.idle=False
            self.play(CursorMoveTo(cursor, x1, y1), run_time=0.5)

            self.wait_until_bookmark("intersect2")
            x1, y1, _ = plane.c2p(14, 16.5)
            self.play(CursorMoveTo(cursor, x1, y1), run_time=0.5)
            self.wait(.5)
            cursor.idle = True

            self.play(Unwrite(func_plotted_wrong), Unwrite(l), run_time=0.5)
            func_plotted = plane.plot(func, color=BLUE)
            func_plotted_wrong = plane.plot(func, color=RED).rotate(90 * DEGREES)

            self.wait_until_bookmark("blueRecap")
            cursor.idle=False
            self.add_pencil_sound(0.5)
            self.play(Write(func_plotted), CursorMoveTo(cursor,0,1), run_time=0.5)
            b = Bubble(texts = [self.translate("Func_1_1.1I1a.bubble_1a"), self.translate("Func_1_1.1I1a.bubble_1b")], center=np.array([0,2.3, 0]), start_point=np.array([0,1,0]), width=2.5, height = 0.8)
            self.wait(0.2)
            self.add_bubble_sound(1.5)
            cursor.add_updater(lambda m: m.move_to(b.get_end()))
            self.play(Create(b), Create(b.text))
            cursor.idle=True
            cursor.remove_updater(lambda m: m.move_to(b.get_end()))

            self.wait_until_bookmark("redRecap")
            cursor.idle=False
            self.add_pencil_sound(0.5)
            self.play(Write(func_plotted_wrong), CursorMoveTo(cursor,-.2,-1), run_time=0.5)
            b = Bubble(texts = [self.translate("Func_1_1.1I1a.bubble_2a"), self.translate("Func_1_1.1I1a.bubble_2b")], center=np.array([-.5,-2.5, 0]), start_point=np.array([-.2,-1,0]), loc="t1", width=2.8, height=0.8)
            self.add_bubble_sound(1.5)
            cursor.add_updater(lambda m: m.move_to(b.get_end()))
            self.play(Create(b), Create(b.text))
            cursor.idle=True
            cursor.remove_updater(lambda m: m.move_to(b.get_end()))


        # Wait for 4 seconds at the end of animation
        self.wait(4)



class Func_1_1_I_1_b(SophiaCursorScene):

    # Main method for constructing the animation
    def construct(self):
        # Adding initial components to the scene
        super().construct()
        self.add_mathgrid()

        # Create the coordinate system
        cords = self.add_cords([6, 24, 3], [5, 25, 5], x_ticks=[6, 12, 18], y_ticks=[10, 15, 20, 25], axisLabelX=self.translate("Func_1_1.1I1a.main.x-axis"), axisLabelY=self.translate("Func_1_1.1I1a.main.y-axis")).shift(DOWN*1.4)
        plane = cords[0]

        # Add title to the scene
        self.add_title(self.translate("Func_1_1.1I1b.main.title"))

        # Create and plot piecewise linear function
        func = create_piecewise_linear([[6, 9], [8, 12], [10, 17], [12, 19], [14, 22], [16, 18], [18, 13], [20, 11], [22, 8], [24, 7]])
        func_plotted = plane.plot(func, color=BLUE)
        func_plotted_wrong = plane.plot(func, color=RED).rotate(90 * DEGREES)

        # Initialize a cursor
        xo, yo, _ = plane.c2p(6,9)
        cursor = AltCursor(stroke_width=0.0, idle=True, x=xo, y=yo)
        cursor.autoFadeBackground = True
        cursor.add_updater(lambda m, dt: self.bring_to_front(cursor))

        # Action Sequence
        with self.voiceover(
                text=self.translate("Func_1_1.1I1b.main.voiceover")
        ) as tracker:
            
            # Animate the coordinate system being created
            self.play(Write(cords), run_time=0.5)
            self.add(cursor)

            # Draw the red function plot (incorrect one) after "RedFuncIn" bookmark.
            self.wait_until_bookmark("RedFuncIn")
            self.add_pencil_sound(1.5)
            self.play(Write(func_plotted_wrong))

            self.wait_until_bookmark("notRed")
            x1, y1, _ = plane.c2p(14, 5)
            cursor.idle = False
            self.play(CursorMoveTo(cursor, x1, y1), run_time=0.5)

            self.wait_until_bookmark("VertLine")
            l = Line([x1, y1, 0], [x1, y1 + 2.4, 0], stroke_width=1.5, color=BLACK)
            self.add_pencil_sound(3)
            self.play(Write(l), run_time=3)

            self.wait_until_bookmark("intersect1")
            x1, y1, _ = plane.c2p(14, 8)
            self.play(CursorMoveTo(cursor, x1, y1), run_time=0.5)

            self.wait_until_bookmark("intersect2")
            x1, y1, _ = plane.c2p(14, 16.5)
            self.play(CursorMoveTo(cursor, x1, y1), run_time=0.5)
            self.wait(2)
            cursor.idle = True

            # Draw the blue function plot after "BlueFuncIn" bookmark.
            self.wait_until_bookmark("BlueFuncIn")
            cursor.idle=False
            self.add_pencil_sound(1.5)
            self.play(Unwrite(func_plotted_wrong), Unwrite(l), Write(func_plotted), CursorMoveTo(cursor, xo, yo))

            # Follow the func with the cursor
            self.wait_until_bookmark("MoveAlongFunc")
            self.play(MoveAlongPath(cursor, func_plotted), run_time=13, rate_func=linear)
            cursor.idle=True

        # Wait for 4 seconds at the end of animation
        self.wait(4)


#####################################
#####################################
class Func_1_1_I_2(SophiaCursorScene):

    # Main method for constructing the animation
    def construct(self):
        # Adding initial components to the scene
        super().construct()
        self.add_mathgrid()

        # Create a notepad with texts
        cords = self.add_cords([6, 24, 3], [5, 25, 5], x_ticks=[6, 12, 18, 24], y_ticks=[10, 15, 20, 25],
                               axisLabelX=self.translate("Func_1_1.1I1a.main.x-axis"), axisLabelY=self.translate("Func_1_1.1I1a.main.y-axis")).shift(DOWN*1.4)
        plane = cords[0]

        # Add title to the scene
        self.add_title(self.translate("Func_1_1.1I2.main.title"))

        # Create and plot piecewise linear function
        func = create_piecewise_linear([[6, 9], [8, 12], [10, 17], [12, 19], [14, 22], [16, 18], [18, 13], [20, 11], [22, 8], [24, 7]])
        func_plotted = plane.plot(func, color=BLUE)
        func_plotted_wrong = plane.plot(func, color=RED).rotate(90 * DEGREES)

        # Initialize a cursor
        xo, yo, _ = plane.c2p(6,9)
        cursor = AltCursor(stroke_width=0.0, idle=True, x=xo, y=yo)
        cursor.autoFadeBackground = True
        cursor.add_updater(lambda m, dt: self.bring_to_front(cursor))

        xToY = MathTex("x", "\,\,\,\\rightarrow\,\,\,", "y", color=c1t).next_to(cords, DOWN, buff=0.5)

        # Action Sequence
        with self.voiceover(
                text=self.translate("Func_1_1.1I2.main.voiceover")
        ) as tracker:
            
            # Animate the coordinate system being created
            self.play(Write(cords), run_time=0.5)
            self.add(cursor)

            # Draw the blue function plot after "BlueFuncIn" bookmark.
            self.wait_until_bookmark("BlueFuncIn")
            self.add_pencil_sound(1.5)
            self.play(Write(func_plotted))
            
            self.wait_until_bookmark("map1")
            self.play(Write(xToY[2]), run_time=0.5)
            cursor.idle=True

            self.wait_until_bookmark("map2")
            self.play(Write(xToY[0]), Write(xToY[1]), run_time=0.5)

            self.wait_until_bookmark("MoveAlongFunc")
            cursor.idle=False
            self.play(MoveAlongPath(cursor, func_plotted), run_time=12, rate_func=linear)
            self.wait(1)
            cursor.idle=True

            # Follow the func with the cursor
            self.wait_until_bookmark("RedFuncIn")
            self.add_pencil_sound(1.5)
            self.play(Write(func_plotted_wrong), Unwrite(func_plotted))

            self.wait_until_bookmark("VertLine")
            x1, y1, _ = plane.c2p(14, 5)
            l = Line([x1, y1, 0], [x1, y1 + 2.4, 0], stroke_width=1.5, color=BLACK)
            self.add_pencil_sound(3)
            self.play(Write(l), run_time=3)

            self.wait_until_bookmark("Memorize")
            self.wait(1)
            cursor.idle=False

            self.wait_until_bookmark("aY")
            x,y,_ = xToY[2].get_center()+0.4*DOWN
            self.play(CursorMoveTo(cursor,x,y), run_time=0.5)

            self.wait_until_bookmark("aX")
            x,y,_ = xToY[0].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.5)
            
        # Wait for 4 seconds at the end of animation
        self.wait(4)


#####################################
#####################################
class Func_1_1_I_3(SophiaCursorScene):

    # Main method for constructing the animation
    def construct(self):
        # Adding initial components to the scene
        super().construct()
        self.add_mathgrid()

        # Create the coordinate system
        cords = self.add_cords([-2,2,1], [0, 4, 1], x_ticks=[-2,2], x_labels=[-2,2], y_ticks=[2,4], y_labels=[2,4]).shift(.6*DOWN)
        plane = cords[0]

        # Add title to the scene
        self.add_title(self.translate("Func_1_1.1I3.main.title"))

        # Create and plot piecewise linear function
        def f(x):
            return x**2
        func_plotted = plane.plot(f, color=ORANGE)
        func_plotted2 = plane.plot(f, color=ORANGE)
        func_plotted_wrong = plane.plot(f, color=GREEN).rotate(90 * DEGREES)

        # Initialize a cursor
        xo, yo, _ = plane.c2p(0,0)
        cursor = AltCursor(stroke_width=0.0, idle=True, x=xo, y=yo)
        cursor.autoFadeBackground = True
        cursor.add_updater(lambda m, dt: self.bring_to_front(cursor))

        xToY = MathTex("x", "\,\,\,\\rightarrow\,\,\,", "y", color=c1t).next_to(cords, DOWN, buff=0.5)
        func_def = Tex(self.translate("Func_1_1.1I3.main.func_def"), color=c3t, font_size=fs3, tex_environment="flushleft").next_to(xToY, DOWN, buff=.7)

        # Action Sequence
        with self.voiceover(
                text=self.translate("Func_1_1.1I3.main.voiceover")
        ) as tracker:
            
            # Animate the coordinate system being created
            self.play(Write(cords), run_time=0.5)
            self.add(cursor)

            self.wait_until_bookmark("Memorize")
            self.play(Create(func_def), run_time=.5)

            self.wait_until_bookmark("map1")
            self.play(Write(xToY[2]), run_time=0.5)

            self.wait_until_bookmark("map2")
            self.play(Write(xToY[0]), Write(xToY[1]), run_time=0.5)

            # Draw the blue function plot after "BlueFuncIn" bookmark.
            self.wait_until_bookmark("OrangeFuncIn")
            self.add_pencil_sound(1.5)
            self.play(Write(func_plotted))

            self.wait_until_bookmark("orangeX")
            cursor.idle=False
            x,y,_ = xToY[0].get_center()+0.4*DOWN
            self.play(CursorMoveTo(cursor,x,y), run_time=0.5)

            self.wait_until_bookmark("orangeY")
            x,y,_ = xToY[2].get_center()+0.4*DOWN
            self.play(CursorMoveToCurved(cursor,x,y), run_time=0.5)

            self.wait_until_bookmark("MoveAlongFunc")
            xs, ys, _ = plane.c2p(-2, 4)
            self.play(CursorMoveTo(cursor, xs, ys), run_time=.5)
            self.play(MoveAlongPath(cursor, func_plotted), run_time=3.5, rate_func=linear)
            self.wait(1)
            cursor.idle=True

            # Follow the func with the cursor
            self.wait_until_bookmark("GreenFuncIn")
            self.add_pencil_sound(1.5)
            self.play(Write(func_plotted_wrong), Unwrite(func_plotted))
            x1, y1, _ = plane.c2p(0, 0)
            cursor.idle=False
            self.play(CursorMoveTo(cursor, x1, y1), run_time=0.5)
            cursor.idle=True

            self.wait_until_bookmark("VertLine")
            l = Line([x1, y1, 0], [x1, y1 + 2.4, 0], stroke_width=3, color=RED)
            self.add_pencil_sound(2)
            self.play(Write(l), run_time=2)
            cx1, cy1, _ = plane.c2p(0, 0.6)
            cx2, cy2, _ = plane.c2p(0, 3.35)
            circ1, circ2 = Circle(radius=0.1, color=RED).move_to([cx1, cy1, 0]), Circle(radius=0.1, color=RED).move_to([cx2, cy2, 0])
            self.play(Write(circ1), Write(circ2), run_time=2)

            self.wait_until_bookmark("TrueFct")
            self.play(Unwrite(l), Unwrite(circ1), Unwrite(circ2), Unwrite(func_plotted_wrong), Write(func_plotted2), run_time=0.8)
            cursor.idle=False
            self.play(CursorMoveTo(cursor, xs, ys), run_time=0.5)
            self.play(MoveAlongPath(cursor, func_plotted2), run_time=5, rate_func=linear)
            cursor.idle=True

        # Wait for 4 seconds at the end of animation
        self.wait(4)


################################
################################
########## Practice Part #######
################################
################################

class ValueTableQuestionScene(SophiaCursorScene, metaclass=ABCMeta):

    # Main method for constructing the animation
    @abstractmethod
    def construct(self):

        # Adding initial components to the scene
        super().construct()
        self.add_mathgrid()

        # Create the coordinate system
        plane = self.cords[0]

        # Add title to the scene
        self.add_title(self.title)

        # Create and plot piecewise linear function
        f1 = create_piecewise_linear(list(zip(self.xvals, self.yvals[0])))
        f2 = create_piecewise_linear(list(zip(self.xvals, self.yvals[1])))
        f3 = create_piecewise_linear(list(zip(self.xvals, self.yvals[2])))
        func_plotted1 = plane.plot(f1, color=ORANGE)
        func_plotted2 = plane.plot(f2, color=BLUE)
        func_plotted3 = plane.plot(f3, color=GREEN)

        tab = Table([[str(val) for val in self.xvals], [str(val) for val in self.yvals[self.correcty]]],
                    color=BLACK, line_config={"color":BLACK}, element_to_mobject_config={"color":BLACK},
                    row_labels=[Text(self.labels[0], color=BLACK, font_size = fs1), Text(self.labels[1], color=BLACK, font_size = fs1)])
        tab = tab.scale(3.3/tab.get_width()).next_to(plane, DOWN, buff=0.35)

        # Initialize a cursor
        xo, yo, _ = plane.c2p(*self.cursorStart)
        cursor = AltCursor(stroke_width=0.0, idle=True, x=xo, y=yo)
        cursor.autoFadeBackground = True

        # Action Sequence
        with self.voiceover(
                text=self.translate("Func_1_1.ValueTableQuestionScene.voiceover")
        ) as tracker:
            
            # Highlight first Text
            self.wait_until_bookmark("action")
            self.add_shift_sound(0.5)
            self.play(self.introImg.animate.shift(5*RIGHT), run_time=0.5)

            # Animate the coordinate system being created
            self.wait_until_bookmark("values")
            self.play(Write(tab))

            # Show the orange function
            self.wait_until_bookmark("orange")
            self.add_shift_sound(0.5)
            self.play(self.introImg.animate.shift(5*RIGHT), Write(self.cords), run_time=0.5)
            self.add_pencil_sound(1.5)
            self.play(Write(func_plotted1))

            # Show the blue function
            self.wait_until_bookmark("blue")
            self.add_pencil_sound(1.5)
            self.play(Write(func_plotted2))

            # Show the green function
            self.wait_until_bookmark("green")
            self.add_pencil_sound(1.5)
            self.play(Write(func_plotted3))

        # Wait for 4 seconds at the end of animation
        self.wait(4)

class ValueTableSolutionScene(SophiaCursorScene, metaclass=ABCMeta):

    # Main method for constructing the animation
    @abstractmethod
    def construct(self):


        # Adding initial components to the scene
        super().construct()
        self.add_mathgrid()

        # Create the coordinate system
        plane = self.cords[0]

        # Add title to the scene
        self.add_title(self.title)

        # Create and plot piecewise linear function
        f1 = create_piecewise_linear(list(zip(self.xvals, self.yvals[0])))
        f2 = create_piecewise_linear(list(zip(self.xvals, self.yvals[1])))
        f3 = create_piecewise_linear(list(zip(self.xvals, self.yvals[2])))
        fcorrect = create_piecewise_linear(list(zip(self.xvals, self.yvals[self.correcty])))
        func_plotted1 = plane.plot(f1, color=ORANGE)
        func_plotted2 = plane.plot(f2, color=BLUE)
        func_plotted3 = plane.plot(f3, color=GREEN)
        func_plotted_correct = plane.plot(fcorrect, color=RED)


        colors = [self.translate("Func_1_1.ValueTableSolutionScene.color-1"), self.translate("Func_1_1.ValueTableSolutionScene.color-2"), self.translate("Func_1_1.ValueTableSolutionScene.color-3")]
        funcs = [func_plotted1, func_plotted2, func_plotted3]

        tab = Table([[str(val) for val in self.xvals], [str(val) for val in self.yvals[self.correcty]]],
                    color=BLACK, line_config={"color":BLACK}, element_to_mobject_config={"color":BLACK},
                    row_labels=[Text(self.labels[0], color=BLACK, font_size = fs1), Text(self.labels[1], color=BLACK, font_size = fs1)])
        tab = tab.scale(3.3/tab.get_width()).next_to(plane, DOWN, buff=0.6)

        # Initialize a cursor
        xo, yo, _ = plane.c2p(*self.cursorStart)
        cursor = AltCursor(stroke_width=0.0, idle=True)
        cursor.autoFadeBackground = True
        cursor.move_to([xo, yo, 0])
        first_bit = self.evaluate_string(self.translate("Func_1_1.ValueTableSolutionScene.first_bit"))
        if self.idx_selected == self.correcty:
            first_bit = self.evaluate_string(self.translate("Func_1_1.ValueTableSolutionScene.first_bit_correct"))

        # Action Sequence
        with self.voiceover(
                text=self.translate("Func_1_1.ValueTableSolutionScene.voiceover")
        ) as tracker:
            
            # Create the Coordinate System
            self.play(Write(self.cords), Write(tab))

            # Highlight first Text
            self.wait_until_bookmark("Func")
            self.play(Write(funcs[self.idx_selected]))
            self.add(cursor)

            # Highlight x-Axis
            self.wait_until_bookmark("xaxis")
            cursor.idle=False
            self.play(CursorMarkAxis(cursor, plane, 'x'), run_time=0.5)

            # Highlight y-Axis
            self.wait_until_bookmark("yaxis")
            self.play(CursorMarkAxis(cursor, plane, 'y'), run_time=0.5)

            # Create first Value
            self.wait_until_bookmark("val1")
            x,y,_ = plane.c2p(self.xvals[0], self.yvals[self.correcty][0])
            self.play(CursorMoveResize(cursor, x, y, 0.2, 0.2))
            c2 = cursor.copy()
            self.add(c2)

            # Create second Value
            self.wait_until_bookmark("val2")
            x,y,_ = plane.c2p(self.xvals[1], self.yvals[self.correcty][1])
            self.play(CursorMoveTo(cursor, x, y))
            c3 = cursor.copy()
            self.add(c3)

            # Create third Value
            self.wait_until_bookmark("val3")
            x,y,_ = plane.c2p(self.xvals[2], self.yvals[self.correcty][2])
            self.play(CursorMoveTo(cursor, x, y))
            c4 = cursor.copy()
            self.add(c4)

            # Create fourth Value
            self.wait_until_bookmark("val4")
            x,y,_ = plane.c2p(self.xvals[3], self.yvals[self.correcty][3])
            self.play(CursorMoveTo(cursor, x, y))
            c5 = cursor.copy()
            self.add(c5)

            # Create fifth Value
            self.wait_until_bookmark("val5")
            x,y,_ = plane.c2p(self.xvals[4], self.yvals[self.correcty][4])
            self.play(CursorMoveTo(cursor, x, y))
            c6 = cursor.copy()
            self.add(c6)

            # Create the function
            self.wait_until_bookmark("TrueFunc")
            self.play(Write(func_plotted_correct), run_time=3)

        # Wait for 4 seconds at the end of animation
        self.wait(4)




#############################################
#               Hike Question               #
#############################################

class Func_1_1_P_1_q(ValueTableQuestionScene):

    def task_definition(self) -> SophiaTaskDefinition:
        return SophiaTaskDefinition(
            answerOptions = [self.translate("Func_1_1.P_color-1"), self.translate("Func_1_1.P_color-2"), self.translate("Func_1_1.P_color-3")],
            correctAnswerIndex = 0,
            questionText = self.translate("Func_1_1.P_question-1") 
        )

    def construct(self):
        self.intro=self.translate("Func_1_1.P_intro")
        self.xvals = [0,1,2,3,4]
        self.yvals = [[4,1,0,1,4],[2,0,1,1,3],[1,3,4,1,2]]
        self.cords = self.add_cords([0,4,1], [0, 4, 1], x_ticks=[0,2,4], x_labels=[0,2,4], y_ticks=[2,4], y_labels=[2,4], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_title")
        self.cursorStart = [0,0]
        self.correcty = 0
        self.introImg = ImageMobject(assets_folder / "img" / "matterhorn.png")
        self.introImg = self.introImg.scale(7/self.introImg.get_width()).move_to([-5, 1, 0])
        self.labels=[self.translate("Func_1_1.P_x"), self.translate("Func_1_1.P_y")]
        super().construct()


class Func_1_1_P_1_a(ValueTableSolutionScene):

    def construct(self):

        self.correcty = 0
        self.idx_selected = 0
        self.xvals = [0,1,2,3,4]
        self.yvals = [[4,1,0,1,4],[2,0,1,1,3],[1,3,4,1,2]]
        self.cords = self.add_cords([0,4,1], [0, 4, 1], x_ticks=[0,2,4], x_labels=[0,2,4], y_ticks=[2,4], y_labels=[2,4], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_title")
        self.cursorStart = [0,0]
        self.labels=[self.translate("Func_1_1.P_x"), self.translate("Func_1_1.P_y")]
        self.Textlabels = [self.translate("Func_1_1.P_x_text"), self.translate("Func_1_1.P_y_text"),]

        super().construct()

class Func_1_1_P_1_b(ValueTableSolutionScene):

    def construct(self):

        self.correcty = 0
        self.idx_selected = 1
        self.xvals = [0,1,2,3,4]
        self.yvals = [[4,1,0,1,4],[2,0,1,1,3],[1,3,4,1,2]]
        self.cords = self.add_cords([0,4,1], [0, 4, 1], x_ticks=[0,2,4], x_labels=[0,2,4], y_ticks=[2,4], y_labels=[2,4], height=2).shift(0.4*DOWN)
        self.cursorStart = [0,0]
        self.labels=[self.translate("Func_1_1.P_x"), self.translate("Func_1_1.P_y")]
        self.Textlabels = [self.translate("Func_1_1.P_x_text"), self.translate("Func_1_1.P_y_text"),]

        super().construct()

class Func_1_1_P_1_c(ValueTableSolutionScene):

    def construct(self):

        self.correcty = 0
        self.idx_selected = 2
        self.xvals = [0,1,2,3,4]
        self.yvals = [[4,1,0,1,4],[2,0,1,1,3],[1,3,4,1,2]]
        self.cords = self.add_cords([0,4,1], [0, 4, 1], x_ticks=[0,2,4], x_labels=[0,2,4], y_ticks=[2,4], y_labels=[2,4], height=2).shift(0.4*DOWN)
        self.cursorStart = [0,0]
        self.labels=[self.translate("Func_1_1.P_x"), self.translate("Func_1_1.P_y")]
        self.Textlabels = [self.translate("Func_1_1.P_x_text"), self.translate("Func_1_1.P_y_text"),]

        super().construct()



#############################################
#               Rain Question               #
#############################################

class Func_1_1_P_2_q(ValueTableQuestionScene):

    def task_definition(self) -> SophiaTaskDefinition:
        return SophiaTaskDefinition(
            answerOptions = [self.translate("Func_1_1.P_color-1"), self.translate("Func_1_1.P_color-2"), self.translate("Func_1_1.P_color-3")],
            correctAnswerIndex = 2,
            questionText = self.translate("Func_1_1.P_question-1") 
        )

    def construct(self):
        self.intro = self.translate("Func_1_1.P_2_intro")
        self.xvals = [1,2,3,4,5]
        self.yvals = [[10, 20, 30, 40, 20], [30, 10, 40, 20, 30], [20, 30, 10, 40, 30]]
        self.cords = self.add_cords([1,5,1], [0, 40, 10], x_ticks=[1,3,5], x_labels=[1,3,5], y_ticks=[10,20,30,40], y_labels=[10,20,30,40], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_2_title")
        self.cursorStart = [1,0]
        self.correcty = 2
        self.introImg = ImageMobject(assets_folder / "img" / "rain.png").scale(0.35).move_to([-5, 1, 0])
        self.labels = [self.translate("Func_1_1.P_2_x"), self.translate("Func_1_1.P_2_y")]
        super().construct()

class Func_1_1_P_2_a(ValueTableSolutionScene):

    def construct(self):

        self.correcty = 2
        self.idx_selected = 0
        self.xvals = [1,2,3,4,5]
        self.yvals = [[10, 20, 30, 40, 20], [30, 10, 40, 20, 30], [20, 30, 10, 40, 30]]
        self.cords = self.add_cords([1,5,1], [0, 40, 10], x_ticks=[1,3,5], x_labels=[1,3,5], y_ticks=[10,20,30,40], y_labels=[10,20,30,40], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_2_title")
        self.cursorStart = [1,0]
        self.Textlabels = [self.translate("Func_1_1.P_2_x_text"), self.translate("Func_1_1.P_2_y_text")]
        self.labels = [self.translate("Func_1_1.P_2_x"), self.translate("Func_1_1.P_2_y")]

        super().construct()

class Func_1_1_P_2_b(ValueTableSolutionScene):

    def construct(self):

        self.correcty = 2
        self.idx_selected = 1
        self.xvals = [1,2,3,4,5]
        self.yvals = [[10, 20, 30, 40, 20], [30, 10, 40, 20, 30], [20, 30, 10, 40, 30]]
        self.cords = self.add_cords([1,5,1], [0, 40, 10], x_ticks=[1,3,5], x_labels=[1,3,5], y_ticks=[10,20,30,40], y_labels=[10,20,30,40], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_2_title")
        self.cursorStart = [1,0]
        self.Textlabels = [self.translate("Func_1_1.P_2_x_text"), self.translate("Func_1_1.P_2_y_text")]
        self.labels = [self.translate("Func_1_1.P_2_x"), self.translate("Func_1_1.P_2_y")]

        super().construct()

class Func_1_1_P_2_c(ValueTableSolutionScene):

    def construct(self):

        self.correcty = 2
        self.idx_selected = 1
        self.xvals = [1,2,3,4,5]
        self.yvals = [[10, 20, 30, 40, 20], [30, 10, 40, 20, 30], [20, 30, 10, 40, 30]]
        self.cords = self.add_cords([1,5,1], [0, 40, 10], x_ticks=[1,3,5], x_labels=[1,3,5], y_ticks=[10,20,30,40], y_labels=[10,20,30,40], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_2_title")
        self.cursorStart = [1,0]
        self.Textlabels = [self.translate("Func_1_1.P_2_x_text"), self.translate("Func_1_1.P_2_y_text")]
        self.labels = [self.translate("Func_1_1.P_2_x"), self.translate("Func_1_1.P_2_y")]

        super().construct()

#############################################
#               Snow Question               #
#############################################

class Func_1_1_P_3_q(ValueTableQuestionScene):

    def task_definition(self) -> SophiaTaskDefinition:
        return SophiaTaskDefinition(
            answerOptions = [self.translate("Func_1_1.P_color-1"), self.translate("Func_1_1.P_color-2"), self.translate("Func_1_1.P_color-3")],
            correctAnswerIndex = 1,
            questionText = self.translate("Func_1_1.P_question-1") 
        )

    def construct(self):
        self.intro = self.translate("Func_1_1.P_3_intro")
        self.xvals = [1, 2, 3, 4, 5]
        self.yvals = [[5, 10, 15, 10, 5], [10, 5, 15, 10, 15], [10, 15, 5, 15, 10]]
        self.cords = self.add_cords([1, 5, 1], [0, 15, 5], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[5, 10, 15], y_labels=[5, 10, 15], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_3_title")
        self.cursorStart = [1, 0]
        self.correcty = 1
        self.introImg = ImageMobject(assets_folder / "img" / "snow.png")
        self.introImg = self.introImg.scale(2.5/self.introImg.get_width()).move_to([-5, 1, 0])
        self.labels = [self.translate("Func_1_1.P_3_x"), self.translate("Func_1_1.P_3_y")]
        super().construct()

class Func_1_1_P_3_a(ValueTableSolutionScene):

    def construct(self):
        self.correcty = 1
        self.idx_selected = 0
        self.xvals = [1, 2, 3, 4, 5]
        self.yvals = [[5, 10, 15, 10, 5], [10, 5, 15, 10, 15], [10, 15, 5, 15, 10]]
        self.cords = self.add_cords([1, 5, 1], [0, 15, 5], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[5, 10, 15], y_labels=[5, 10, 15], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_3_title")
        self.cursorStart = [1, 0]
        self.correcty = 1
        self.introImg = ImageMobject(assets_folder / "img" / "snow.png")
        self.introImg = self.introImg.scale(2.5/self.introImg.get_width()).move_to([-5, 1, 0])
        self.labels = [self.translate("Func_1_1.P_3_x"), self.translate("Func_1_1.P_3_y")]
        self.Textlabels = [self.translate("Func_1_1.P_3_x_text"), self.translate("Func_1_1.P_3_y_text")]
        super().construct()

class Func_1_1_P_3_b(ValueTableSolutionScene):

    def construct(self):
        self.correcty = 1
        self.idx_selected = 1
        self.xvals = [1, 2, 3, 4, 5]
        self.yvals = [[5, 10, 15, 10, 5], [10, 5, 15, 10, 15], [10, 15, 5, 15, 10]]
        self.cords = self.add_cords([1, 5, 1], [0, 15, 5], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[5, 10, 15], y_labels=[5, 10, 15], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_3_title")
        self.cursorStart = [1, 0]
        self.correcty = 1
        self.introImg = ImageMobject(assets_folder / "img" / "snow.png")
        self.introImg = self.introImg.scale(2.5/self.introImg.get_width()).move_to([-5, 1, 0])
        self.labels = [self.translate("Func_1_1.P_3_x"), self.translate("Func_1_1.P_3_y")]
        self.Textlabels = [self.translate("Func_1_1.P_3_x_text"), self.translate("Func_1_1.P_3_y_text")]

        super().construct()

class Func_1_1_P_3_c(ValueTableSolutionScene):

    def construct(self):
        self.correcty = 1
        self.idx_selected = 2
        self.xvals = [1, 2, 3, 4, 5]
        self.yvals = [[5, 10, 15, 10, 5], [10, 5, 15, 10, 15], [10, 15, 5, 15, 10]]
        self.cords = self.add_cords([1, 5, 1], [0, 15, 5], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[5, 10, 15], y_labels=[5, 10, 15], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_3_title")
        self.cursorStart = [1, 0]
        self.correcty = 1
        self.introImg = ImageMobject(assets_folder / "img" / "snow.png")
        self.introImg = self.introImg.scale(2.5/self.introImg.get_width()).move_to([-5, 1, 0])
        self.labels = [self.translate("Func_1_1.P_3_x"), self.translate("Func_1_1.P_3_y")]
        self.Textlabels = [self.translate("Func_1_1.P_3_x_text"), self.translate("Func_1_1.P_3_y_text")]

        super().construct()

    

# Similar Answer Scenes for SnowQuestionScene can be created like RainAnswerScene1, RainAnswerScene2 and RainAnswerScene3


#############################################
#           Sunshine Hours Question         #
#############################################

class Func_1_1_P_4_q(ValueTableQuestionScene):

    def task_definition(self) -> SophiaTaskDefinition:
        return SophiaTaskDefinition(
            answerOptions = [self.translate("Func_1_1.P_color-1"), self.translate("Func_1_1.P_color-2"), self.translate("Func_1_1.P_color-3")],
            correctAnswerIndex = 0,
            questionText = self.translate("Func_1_1.P_question-1") 
        )

    def construct(self):
        self.intro = self.translate("Func_1_1.P_4_intro")
        self.xvals = [1, 2, 3, 4, 5]
        self.yvals = [[12, 10, 11, 12, 10], [10, 12, 10, 11, 12], [11, 12, 10, 12, 11]]
        self.cords = self.add_cords([1, 5, 1], [10, 12, 1], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[10, 11, 12], y_labels=[10, 11, 12], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_4_title")
        self.cursorStart = [1, 0]
        self.correcty = 0
        self.introImg = ImageMobject(assets_folder / "img" / "sun.png")
        self.introImg = self.introImg.scale(3/self.introImg.get_width()).move_to([-5, 1, 0])
        self.labels = [self.translate("Func_1_1.P_4_x"), self.translate("Func_1_1.P_4_y")]
        super().construct()

class Func_1_1_P_4_a(ValueTableSolutionScene):

    def construct(self):

        self.xvals = [1, 2, 3, 4, 5]
        self.yvals = [[12, 10, 11, 12, 10], [10, 12, 10, 11, 12], [11, 12, 10, 12, 11]]
        self.cords = self.add_cords([1, 5, 1], [10, 12, 1], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[10, 11, 12], y_labels=[10, 11, 12], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_4_title")
        self.cursorStart = [1, 10]
        self.correcty = 0
        self.idx_selected=0
        self.labels = [self.translate("Func_1_1.P_4_x"), self.translate("Func_1_1.P_4_y")]
        self.Textlabels = [self.translate("Func_1_1.P_4_x_text"), self.translate("Func_1_1.P_4_y_text")]
        super().construct()

class Func_1_1_P_4_b(ValueTableSolutionScene):

    def construct(self):

        self.xvals = [1, 2, 3, 4, 5]
        self.yvals = [[12, 10, 11, 12, 10], [10, 12, 10, 11, 12], [11, 12, 10, 12, 11]]
        self.cords = self.add_cords([1, 5, 1], [10, 12, 1], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[10, 11, 12], y_labels=[10, 11, 12], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_4_title")
        self.cursorStart = [1, 10]
        self.correcty = 0
        self.idx_selected=1
        self.labels = [self.translate("Func_1_1.P_4_x"), self.translate("Func_1_1.P_4_y")]
        self.Textlabels = [self.translate("Func_1_1.P_4_x_text"), self.translate("Func_1_1.P_4_y_text")]

        super().construct()

class Func_1_1_P_4_c(ValueTableSolutionScene):

    def construct(self):

        self.xvals = [1, 2, 3, 4, 5]
        self.yvals = [[12, 10, 11, 12, 10], [10, 12, 10, 11, 12], [11, 12, 10, 12, 11]]
        self.cords = self.add_cords([1, 5, 1], [10, 12, 1], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[10, 11, 12], y_labels=[10, 11, 12], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_4_title")
        self.cursorStart = [1, 10]
        self.correcty = 0
        self.idx_selected=2
        self.labels = [self.translate("Func_1_1.P_4_x"), self.translate("Func_1_1.P_4_y")]
        self.Textlabels = [self.translate("Func_1_1.P_4_x_text"), self.translate("Func_1_1.P_4_y_text")]

        super().construct()


#############################################
#           Wind Speed Question             #
#############################################
class Func_1_1_P_5_q(ValueTableQuestionScene):

    def task_definition(self) -> SophiaTaskDefinition:
        return SophiaTaskDefinition(
            answerOptions = [self.translate("Func_1_1.P_color-1"), self.translate("Func_1_1.P_color-2"), self.translate("Func_1_1.P_color-3")],
            correctAnswerIndex = 2,
            questionText = self.translate("Func_1_1.P_question-1") 
        )

    def construct(self):
        self.intro = self.translate("Func_1_1.P_5_intro")
        self.xvals = [1, 2, 3, 4, 5, 6]
        self.yvals = [[20, 30, 40, 50, 40, 30], [30, 20, 50, 40, 30, 50], [30, 40, 20, 50, 40, 30]]
        self.cords = self.add_cords([1, 6, 1], [0, 50, 10], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[20, 30, 40, 50], y_labels=[20, 30, 40, 50], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_5_title")
        self.cursorStart = [1, 20]
        self.correcty = 2
        self.introImg = ImageMobject(assets_folder / "img" / "wind.png").scale(0.35).move_to([-5, 1, 0])
        self.labels = self.translate("Func_1_1.P_5_labels")
        super().construct()

class Func_1_1_P_5_a(ValueTableSolutionScene):

    def construct(self):
        self.xvals = [1, 2, 3, 4, 5, 6]
        self.yvals = [[20, 30, 40, 50, 40, 30], [30, 20, 50, 40, 30, 50], [30, 40, 20, 50, 40, 30]]
        self.cords = self.add_cords([1, 6, 1], [0, 50, 10], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[20, 30, 40, 50], y_labels=[20, 30, 40, 50], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_5_title")
        self.cursorStart = [1, 20]
        self.correcty = 2
        self.idx_selected=0
        self.labels = self.translate("Func_1_1.P_5_labels")
        self.Textlabels = self.translate("Func_1_1.P_5_textlabels")
        super().construct()

class Func_1_1_P_5_b(ValueTableSolutionScene):

    def construct(self):
        self.xvals = [1, 2, 3, 4, 5, 6]
        self.yvals = [[20, 30, 40, 50, 40, 30], [30, 20, 50, 40, 30, 50], [30, 40, 20, 50, 40, 30]]
        self.cords = self.add_cords([1, 6, 1], [0, 50, 10], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[20, 30, 40, 50], y_labels=[20, 30, 40, 50], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_5_title")
        self.cursorStart = [1, 20]
        self.correcty = 2
        self.idx_selected=1
        self.labels = self.translate("Func_1_1.P_5_labels")
        self.Textlabels = self.translate("Func_1_1.P_5_textlabels")
        super().construct()

class Func_1_1_P_5_c(ValueTableSolutionScene):

    def construct(self):
        self.xvals = [1, 2, 3, 4, 5, 6]
        self.yvals = [[20, 30, 40, 50, 40, 30], [30, 20, 50, 40, 30, 50], [30, 40, 20, 50, 40, 30]]
        self.cords = self.add_cords([1, 6, 1], [0, 50, 10], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[20, 30, 40, 50], y_labels=[20, 30, 40, 50], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_5_title")
        self.cursorStart = [1, 20]
        self.correcty = 2
        self.idx_selected=2
        self.labels = self.translate("Func_1_1.P_5_labels")
        self.Textlabels = self.translate("Func_1_1.P_5_textlabels")
        super().construct()

#############################################
#            Temperature Question           #
#############################################

class Func_1_1_P_6_q(ValueTableQuestionScene):

    def task_definition(self) -> SophiaTaskDefinition:
        return SophiaTaskDefinition(
            answerOptions = [self.translate("Func_1_1.P_color-1"), self.translate("Func_1_1.P_color-2"), self.translate("Func_1_1.P_color-3")],
            correctAnswerIndex = 0,
            questionText = self.translate("Func_1_1.P_question-1") 
        )

    def construct(self):
        self.intro = self.translate("Func_1_1.P_6_intro")
        self.xvals = [1, 2, 3, 4, 5]
        self.yvals = [[10, 15, 12, 14, 13], [15, 10, 14, 13, 15], [13, 14, 10, 15, 14]]
        self.cords = self.add_cords([1, 5, 1], [10, 15, 1], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[10, 12, 14], y_labels=[10, 12, 14], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_6_title")
        self.cursorStart = [1, 10]
        self.correcty = 0
        self.introImg = ImageMobject(assets_folder / "img" / "spring.png").scale(0.35).move_to([-5, -0.3, 0])
        self.labels = self.translate("Func_1_1.P_6_labels")
        super().construct()

class Func_1_1_P_6_a(ValueTableSolutionScene):

    def construct(self):
        self.xvals = [1, 2, 3, 4, 5]
        self.yvals = [[10, 15, 12, 14, 13], [15, 10, 14, 13, 15], [13, 14, 10, 15, 14]]
        self.cords = self.add_cords([1, 5, 1], [10, 15, 1], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[10, 12, 14], y_labels=[10, 12, 14], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_6_title")
        self.cursorStart = [1, 10]
        self.correcty = 0
        self.idx_selected = 0
        self.labels = self.translate("Func_1_1.P_6_labels")
        self.Textlabels = self.translate("Func_1_1.P_6_textlabels")
        super().construct()

class Func_1_1_P_6_b(ValueTableSolutionScene):

    def construct(self):
        self.xvals = [1, 2, 3, 4, 5]
        self.yvals = [[10, 15, 12, 14, 13], [15, 10, 14, 13, 15], [13, 14, 10, 15, 14]]
        self.cords = self.add_cords([1, 5, 1], [10, 15, 1], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[10, 12, 14], y_labels=[10, 12, 14], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_6_title")
        self.cursorStart = [1, 10]
        self.correcty = 0
        self.idx_selected = 1
        self.labels = self.translate("Func_1_1.P_6_labels")
        self.Textlabels = self.translate("Func_1_1.P_6_textlabels")
        super().construct()

class Func_1_1_P_6_c(ValueTableSolutionScene):

    def construct(self):
        self.xvals = [1, 2, 3, 4, 5]
        self.yvals = [[10, 15, 12, 14, 13], [15, 10, 14, 13, 15], [13, 14, 10, 15, 14]]
        self.cords = self.add_cords([1, 5, 1], [10, 15, 1], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[10, 12, 14], y_labels=[10, 12, 14], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_6_title")
        self.cursorStart = [1, 10]
        self.correcty = 0
        self.idx_selected = 2
        self.labels = self.translate("Func_1_1.P_6_labels")
        self.Textlabels = self.translate("Func_1_1.P_6_textlabels")
        super().construct()

#############################################
#             Humidity Question             #
#############################################

class Func_1_1_P_7_q(ValueTableQuestionScene):

    def task_definition(self) -> SophiaTaskDefinition:
        return SophiaTaskDefinition(
            answerOptions = [self.translate("Func_1_1.P_color-1"), self.translate("Func_1_1.P_color-2"), self.translate("Func_1_1.P_color-3")],
            correctAnswerIndex = 1,
            questionText = self.translate("Func_1_1.P_question-1") 
        )

    def construct(self):
        self.intro = self.translate("Func_1_1.P_7_intro")
        self.xvals = [1, 2, 3, 4, 5, 6]
        self.yvals = [[70, 75, 80, 85, 80, 75], [75, 70, 85, 80, 75, 85], [75, 80, 70, 85, 80, 75]]
        self.cords = self.add_cords([1, 6, 1], [70, 90, 10], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[70, 75, 80, 85], y_labels=[70, 75, 80, 85], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_7_title")
        self.cursorStart = [1, 0]
        self.correcty = 1
        self.introImg = ImageMobject(assets_folder / "img" / "palmtree.png").scale(0.15).move_to([-5, 1.9, 0])
        self.labels = self.translate("Func_1_1.P_7_labels")
        super().construct()

class Func_1_1_P_7_a(ValueTableSolutionScene):

    def construct(self):
        self.xvals = [1, 2, 3, 4, 5, 6]
        self.yvals = [[70, 75, 80, 85, 80, 75], [75, 70, 85, 80, 75, 85], [75, 80, 70, 85, 80, 75]]
        self.cords = self.add_cords([1, 6, 1], [70, 90, 10], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[70, 75, 80, 85], y_labels=[70, 75, 80, 85], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_7_title")
        self.cursorStart = [1, 0]
        self.correcty = 1
        self.idx_selected = 0
        self.labels = self.translate("Func_1_1.P_7_labels")
        self.Textlabels = self.translate("Func_1_1.P_7_textlabels")
        super().construct()

class Func_1_1_P_7_b(ValueTableSolutionScene):

    def construct(self):
        self.xvals = [1, 2, 3, 4, 5, 6]
        self.yvals = [[70, 75, 80, 85, 80, 75], [75, 70, 85, 80, 75, 85], [75, 80, 70, 85, 80, 75]]
        self.cords = self.add_cords([1, 6, 1], [70, 90, 10], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[70, 75, 80, 85], y_labels=[70, 75, 80, 85], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_7_title")
        self.cursorStart = [1, 0]
        self.correcty = 1
        self.idx_selected = 1
        self.labels = self.translate("Func_1_1.P_7_labels")
        self.Textlabels = self.translate("Func_1_1.P_7_textlabels")
        super().construct()

class Func_1_1_P_7_c(ValueTableSolutionScene):

    def construct(self):
        self.xvals = [1, 2, 3, 4, 5, 6]
        self.yvals = [[70, 75, 80, 85, 80, 75], [75, 70, 85, 80, 75, 85], [75, 80, 70, 85, 80, 75]]
        self.cords = self.add_cords([1, 6, 1], [70, 90, 10], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[70, 75, 80, 85], y_labels=[70, 75, 80, 85], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_7_title")
        self.cursorStart = [1, 0]
        self.correcty = 1
        self.idx_selected = 2
        self.labels = self.translate("Func_1_1.P_7_labels")
        self.Textlabels = self.translate("Func_1_1.P_7_textlabels")
        super().construct()

#############################################
#             Apple Picking Question        #
#############################################
class Func_1_1_P_8_q(ValueTableQuestionScene):

    def task_definition(self) -> SophiaTaskDefinition:
        return SophiaTaskDefinition(
            answerOptions = [self.translate("Func_1_1.P_color-1"), self.translate("Func_1_1.P_color-2"), self.translate("Func_1_1.P_color-3")],
            correctAnswerIndex = 1,
            questionText = self.translate("Func_1_1.P_question-1") 
        )


    def construct(self):
        self.intro = self.translate("Func_1_1.P_8_intro")
        self.xvals = [1, 2, 3, 4, 5]
        self.yvals = [[15, 30, 20, 25, 18], [20, 15, 25, 18, 30], [25, 20, 15, 30, 18]]
        self.cords = self.add_cords([1, 5, 1], [0, 30, 5], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[10, 20, 30], y_labels=[10, 20, 30], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_8_title")
        self.cursorStart = [1, 0]
        self.correcty = 1
        self.introImg = ImageMobject(assets_folder / "img" / "apple.png").scale(0.5).move_to([-5, 1, 0])
        self.labels = self.translate("Func_1_1.P_8_labels")
        super().construct()

class Func_1_1_P_8_a(ValueTableSolutionScene):

    def construct(self):
        self.xvals = [1, 2, 3, 4, 5]
        self.yvals = [[15, 30, 20, 25, 18], [20, 15, 25, 18, 30], [25, 20, 15, 30, 18]]
        self.cords = self.add_cords([1, 5, 1], [0, 30, 5], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[10, 20, 30], y_labels=[10, 20, 30], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_8_title")
        self.cursorStart = [1, 0]
        self.correcty = 1
        self.idx_selected = 0
        self.labels = self.translate("Func_1_1.P_8_labels")
        self.Textlabels = self.translate("Func_1_1.P_8_textlabels")
        super().construct()

class Func_1_1_P_8_b(ValueTableSolutionScene):

    def construct(self):
        self.xvals = [1, 2, 3, 4, 5]
        self.yvals = [[15, 30, 20, 25, 18], [20, 15, 25, 18, 30], [25, 20, 15, 30, 18]]
        self.cords = self.add_cords([1, 5, 1], [0, 30, 5], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[10, 20, 30], y_labels=[10, 20, 30], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_8_title")
        self.cursorStart = [1, 0]
        self.correcty = 1
        self.idx_selected = 1
        self.labels = self.translate("Func_1_1.P_8_labels")
        self.Textlabels = self.translate("Func_1_1.P_8_textlabels")
        super().construct()

class Func_1_1_P_8_c(ValueTableSolutionScene):

    def construct(self):
        self.xvals = [1, 2, 3, 4, 5]
        self.yvals = [[15, 30, 20, 25, 18], [20, 15, 25, 18, 30], [25, 20, 15, 30, 18]]
        self.cords = self.add_cords([1, 5, 1], [0, 30, 5], x_ticks=[1, 3, 5], x_labels=[1, 3, 5], y_ticks=[10, 20, 30], y_labels=[10, 20, 30], height=2).shift(0.4*DOWN)
        self.title = self.translate("Func_1_1.P_8_title")
        self.cursorStart = [1, 0]
        self.correcty = 1
        self.idx_selected = 2
        self.labels = self.translate("Func_1_1.P_8_labels")
        self.Textlabels = self.translate("Func_1_1.P_8_textlabels")
        super().construct()



# # Add the scene to prototypes
# PROTOTYPES = [
#     PagePrototypeVideo.from_scene(Func_1_1_I_1_q),
#     PagePrototypeQuestion.from_task_definition(TASK_Func_1_1_I_1_q, Func_1_1_I_1_q.__name__),
#     PagePrototypeVideo.from_scene(Func_1_1_I_1_a),
#     PagePrototypeVideo.from_scene(Func_1_1_I_1_b),
#     PagePrototypeVideo.from_scene(Func_1_1_I_2),
#     PagePrototypeVideo.from_scene(Func_1_1_I_3),
#     PagePrototypeVideo.from_scene(Func_1_1_P_1_q),
#     PagePrototypeQuestion.from_task_definition(TASK_Func_1_1_P_1_q, Func_1_1_P_1_q.__name__),
#     PagePrototypeVideo.from_scene(Func_1_1_P_1_a),
#     PagePrototypeVideo.from_scene(Func_1_1_P_1_b),
#     PagePrototypeVideo.from_scene(Func_1_1_P_1_c),
#     PagePrototypeVideo.from_scene(Func_1_1_P_2_q),
#     PagePrototypeQuestion.from_task_definition(TASK_Func_1_1_P_2_q, Func_1_1_P_2_q.__name__),
#     PagePrototypeVideo.from_scene(Func_1_1_P_2_a),
#     PagePrototypeVideo.from_scene(Func_1_1_P_2_b),
#     PagePrototypeVideo.from_scene(Func_1_1_P_2_c),
#     PagePrototypeVideo.from_scene(Func_1_1_P_3_q),
#     PagePrototypeQuestion.from_task_definition(TASK_Func_1_1_P_3_q, Func_1_1_P_3_q.__name__),
#     PagePrototypeVideo.from_scene(Func_1_1_P_3_a),
#     PagePrototypeVideo.from_scene(Func_1_1_P_3_b),
#     PagePrototypeVideo.from_scene(Func_1_1_P_3_c),
#     PagePrototypeVideo.from_scene(Func_1_1_P_4_q),
#     PagePrototypeQuestion.from_task_definition(TASK_Func_1_1_P_4_q, Func_1_1_P_4_q.__name__),
#     PagePrototypeVideo.from_scene(Func_1_1_P_4_a),
#     PagePrototypeVideo.from_scene(Func_1_1_P_4_b),
#     PagePrototypeVideo.from_scene(Func_1_1_P_4_c),
#     PagePrototypeVideo.from_scene(Func_1_1_P_5_q),
#     PagePrototypeQuestion.from_task_definition(TASK_Func_1_1_P_5_q, Func_1_1_P_5_q.__name__),
#     PagePrototypeVideo.from_scene(Func_1_1_P_5_a),
#     PagePrototypeVideo.from_scene(Func_1_1_P_5_b),
#     PagePrototypeVideo.from_scene(Func_1_1_P_5_c),
#     PagePrototypeVideo.from_scene(Func_1_1_P_6_q),
#     PagePrototypeQuestion.from_task_definition(TASK_Func_1_1_P_6_q, Func_1_1_P_6_q.__name__),
#     PagePrototypeVideo.from_scene(Func_1_1_P_6_a),
#     PagePrototypeVideo.from_scene(Func_1_1_P_6_b),
#     PagePrototypeVideo.from_scene(Func_1_1_P_6_c),
#     PagePrototypeVideo.from_scene(Func_1_1_P_7_q),
#     PagePrototypeQuestion.from_task_definition(TASK_Func_1_1_P_7_q, Func_1_1_P_7_q.__name__),
#     PagePrototypeVideo.from_scene(Func_1_1_P_7_a),
#     PagePrototypeVideo.from_scene(Func_1_1_P_7_b),
#     PagePrototypeVideo.from_scene(Func_1_1_P_7_c),
#     PagePrototypeVideo.from_scene(Func_1_1_P_8_q),
#     PagePrototypeQuestion.from_task_definition(TASK_Func_1_1_P_8_q, Func_1_1_P_8_q.__name__),
#     PagePrototypeVideo.from_scene(Func_1_1_P_8_a),
#     PagePrototypeVideo.from_scene(Func_1_1_P_8_b),
#     PagePrototypeVideo.from_scene(Func_1_1_P_8_c)
# ]

