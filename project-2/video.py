from manim import *

class BlackHoleFormation(Scene):
    def construct(self):
        # 1. Introduction: Massive Star
        star = Dot(radius=2.5, color=YELLOW)
        star.set_glow_factor(0.5)
        star_text = Text("Massive Star (Main Sequence)", font_size=24).to_edge(UP)
        
        self.play(FadeIn(star), Write(star_text))
        self.wait(1)

        # 2. Hydrostatic Equilibrium Arrows
        outward_arrows = VGroup(*[
            Arrow(ORIGIN, 1.5 * direction, color=ORANGE) 
            for direction in [UP, DOWN, LEFT, RIGHT, UL, UR, DL, DR]
        ])
        inward_arrows = VGroup(*[
            Arrow(3 * direction, 1.5 * direction, color=BLUE) 
            for direction in [UP, DOWN, LEFT, RIGHT, UL, UR, DL, DR]
        ])
        
        lbl_fusion = Text("Radiation Pressure", color=ORANGE, font_size=20).next_to(outward_arrows, RIGHT)
        lbl_gravity = Text("Gravity", color=BLUE, font_size=20).next_to(inward_arrows, LEFT)

        self.play(Create(outward_arrows), Create(inward_arrows))
        self.play(Write(lbl_fusion), Write(lbl_gravity))
        self.wait(2)

        # 3. Fuel Depletion (Red Supergiant Phase)
        self.play(
            star.animate.scale(1.5).set_color(RED),
            outward_arrows.animate.scale(1.2),
            lbl_fusion.animate.set_text("Iron Core Forming"),
            run_time=2
        )
        self.wait(1)

        # 4. The Collapse (Supernova)
        collapse_text = Text("Fusion Ceases: Gravity Wins", color=RED).to_edge(UP)
        self.play(
            FadeOut(star_text),
            FadeOut(outward_arrows),
            Transform(star_text, collapse_text)
        )
        
        # Fast inward collapse
        self.play(
            star.animate.scale(0.01).set_color(WHITE),
            inward_arrows.animate.scale(0.1).set_color(WHITE),
            run_time=0.8,
            rate_func=exponential_decay
        )
        
        # 5. The Event Horizon and Singularity
        singularity = Dot(radius=0.05, color=WHITE)
        event_horizon = Circle(radius=1.5, color=DARK_GRAY, fill_opacity=0.8).set_fill(BLACK)
        
        # Gravitational Lensing effect (Simplified)
        lensing_rings = VGroup(*[
            Circle(radius=r, color=BLUE_E, stroke_width=1).set_opacity(0.3)
            for r in np.arange(1.6, 2.5, 0.2)
        ])

        bh_text = Text("Black Hole Formed", font_size=32).to_edge(UP)
        
        self.play(
            ReplacementTransform(star, singularity),
            FadeIn(event_horizon),
            FadeIn(lensing_rings),
            FadeOut(inward_arrows),
            FadeOut(lbl_gravity),
            FadeOut(lbl_fusion),
            Transform(star_text, bh_text)
        )
        
        # 6. Final Logic: Schwarzschild Radius
        formula = MathTex(r"R_s = \frac{2GM}{c^2}", font_size=36).next_to(event_horizon, DOWN)
        self.play(Write(formula))
        self.play(Indicate(formula))
        
        self.wait(3)