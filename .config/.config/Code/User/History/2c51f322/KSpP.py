from manim import *

class Animation(Scene):
    def create_farm(self):
        farm_land = Square(color=GREEN, fill_color=GREEN, fill_opacity=0.5, side_length=5)
        text = Text("Original Farm Land", color=WHITE)
        text.scale(0.7)
        text.next_to(farm_land, UP)
        return VGroup(farm_land, text)
    
    def divided_land(self):
        side = 2.5
        offset = side/2
        sq1 = Square(side_length=side).shift(offset*UP + offset*LEFT).set_fill(GREEN, opacity=0.5)
        sq2 = Square(side_length=side).shift(offset*UP + offset*RIGHT).set_fill(GREEN, opacity=0.5)
        sq3 = Square(side_length=side).shift(offset*DOWN + offset*LEFT).set_fill(GREEN, opacity=0.5)
        sq4 = Square(side_length=side).shift(offset*DOWN + offset*RIGHT).set_fill(GREEN, opacity=0.5)
        t1 = Text("1").move_to(sq1.get_center())
        t2 = Text("2").move_to(sq2.get_center())
        t3 = Text("3").move_to(sq3.get_center())
        t4 = Text("4").move_to(sq4.get_center())

        divided_land = VGroup(sq1, sq2, sq3, sq4, t1, t2, t3, t4)
        return divided_land

    def initial_text(self):
        problem_statement = Text("Smart Crop Advisory System for Small and Marginal Farmers", color=WHITE)
        problem_statement.scale(0.7)
        problem_statement.set_stroke(color=BLUE, width=2)
        return problem_statement
    
    def highlight(self, lands):
        farmer = Text("Farmer", font_size=20)
        farmer.next_to(lands[0], UP)
        self.play(Write(farmer))
        for sq in range(4):
            if sq == 0 or sq == 1:
                self.play(farmer.animate.next_to(lands[sq], UP))
            else:
                self.play(farmer.animate.next_to(lands[sq], DOWN))
            self.play(Indicate(lands[sq], color=YELLOW))
            self.wait(0.5)




    def construct(self):
        grid = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-6, 6, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_opacity": 0.3,
                "stroke_width": 1
            },
            axis_config={"stroke_opacity": 0}
        )
        self.add(grid)

        # Creating all the variables
        problem_statement = self.initial_text()
        farm_land = self.create_farm()
        four_pieces = self.divided_land()
        Explanation = Text("Now dividing this into 4 individual pieces")
        Farmer_Explanation = Paragraph(
            "Farmers can monitor each piece of land",
            "in regular intervals",
            alignment="center",
            line_spacing=0.8
        ).scale(0.7)
        Farmer_Explanation.next_to(four_pieces, UP)


        self.play(Write(problem_statement))
        self.wait(1)
        self.play(AnimationGroup(
            Unwrite(problem_statement),
            FadeOut(problem_statement),
            lag_ratio=0
        ))

        self.play(Create(farm_land))
        self.wait(2)
        self.play(FadeOut(farm_land))

        self.play(Write(Explanation))
        self.wait(2)
        self.play(FadeOut(Explanation))


        self.play(Create(four_pieces))
        self.play(Write(Farmer_Explanation))
        self.wait(1)
        self.play(FadeOut(Farmer_Explanation))
        self.highlight(four_pieces)
