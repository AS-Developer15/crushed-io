@namespace
class SpriteKind:
    Obstacle = SpriteKind.create()
def FallBig():
    BigFallingBlock.set_position(randint(20, 160), 0)
    BigFallingBlock.set_velocity(0, 60)
    animation.run_image_animation(BigFallingBlock,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . 2 . . . . . . . . . 
                        . . . . . 2 2 2 . . . . . . . . 
                        . . . . 2 2 2 2 2 . . . . . . . 
                        . . . 2 2 2 2 2 2 2 . . . . . . 
                        . . 2 2 2 2 5 2 2 2 2 . . . . . 
                        . . . 2 2 2 2 2 2 2 . . . . . . 
                        . . . . 2 2 2 2 2 . . . . . . . 
                        . . . . . 2 2 2 . . . . . . . . 
                        . . . . . . 2 . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . 2 . . . . . 
                        . . . . . . . . . 2 2 2 . . . . 
                        . . . . . . . . 2 2 2 2 2 . . . 
                        . . . . . . . 2 2 2 2 2 2 2 . . 
                        . . . . . . 2 2 2 2 5 2 2 2 2 . 
                        . . . . . . . 2 2 2 2 2 2 2 . . 
                        . . . . . . . . 2 2 2 2 2 . . . 
                        . . . . . . . . . 2 2 2 . . . . 
                        . . . . . . . . . . 2 . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        500,
        True)
    pause(1000)
def Fall():
    animation.run_image_animation(FallingBlock,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . 4 . . . . . . . . 
                        . . . . . . 4 4 4 . . . . . . . 
                        . . . . . 4 4 4 4 4 . . . . . . 
                        . . . . . . 4 4 4 . . . . . . . 
                        . . . . . . . 4 . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . 2 . . . . . . . . 
                        . . . . . . 2 2 2 . . . . . . . 
                        . . . . . 2 2 2 2 2 . . . . . . 
                        . . . . . . 2 2 2 . . . . . . . 
                        . . . . . . . 2 . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        500,
        True)
    FallingBlock.set_position(randint(20, 160), 0)
    FallingBlock.set_velocity(0, 30)
    pause(2000)

def on_on_overlap(sprite, otherSprite):
    info.set_score(abs(game.runtime()) / 1000)
    game.set_game_over_scoring_type(game.ScoringType.HIGH_SCORE)
    game.game_over(False)
    game.set_game_over_message(False,
        "Your High Score is :" + convert_to_text(info.score()) + "")
sprites.on_overlap(SpriteKind.player, SpriteKind.Obstacle, on_on_overlap)

def FallBig2():
    BiggerFallBlock.start_effect(effects.rings)
    animation.run_movement_animation(BigFallingBlock,
        animation.animation_presets(animation.parachute_right),
        1000,
        True)
    BiggerFallBlock.set_position(randint(20, 160), 0)
    BiggerFallBlock.set_velocity(randint(-10, 10), 79)
    pause(1500)

def on_left_pressed():
    Block.set_velocity(-50, 0)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    Block.set_velocity(0, 0)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    Block.set_velocity(0, 0)
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_right_pressed():
    Block.set_velocity(50, 0)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def FallBigEnd():
    Final_Fall.start_effect(effects.fire)
    Final_Fall.set_velocity(randint(-80, 80), 90)
def Fall2():
    animation.run_image_animation(BlockMulti,
        assets.animation("""
            newMultifall
        """),
        500,
        True)
    BlockMulti.set_position(randint(30, 150), 0)
    BlockMulti.set_velocity(0, 30)
    pause(2000)
BlockMulti: Sprite = None
Final_Fall: Sprite = None
BiggerFallBlock: Sprite = None
BigFallingBlock: Sprite = None
FallingBlock: Sprite = None
Block: Sprite = None
game.show_long_text("Welcome to Crushed.io", DialogLayout.CENTER)
game.show_long_text("Try not to get Crushed!!! " + "Accpet the challenge",
    DialogLayout.CENTER)
scene.set_background_image(assets.image("""
    Background
"""))
Block = sprites.create(assets.image("""
    Block
"""), SpriteKind.player)
FallingBlock = sprites.create(assets.image("""
    Falling Block
"""), SpriteKind.Obstacle)
BigFallingBlock = sprites.create(assets.image("""
    BigBlockF
"""), SpriteKind.Obstacle)
BiggerFallBlock = sprites.create(assets.image("""
    BiggerFallB
"""), SpriteKind.Obstacle)
Final_Fall = sprites.create(assets.image("""
    FancyBlog
"""), SpriteKind.Obstacle)
BlockMulti = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . 2 . . . . . . 2 . . . . 
            . . . . . 3 3 3 3 3 3 . . . . . 
            . . . . . 3 . . . . 3 . . . . . 
            . . . . . 3 . . . . 3 . . . . . 
            . . . . . 3 . . . . 3 . . . . . 
            . . . . . 3 . . . . 3 . . . . . 
            . . . . . 3 3 3 3 3 3 . . . . . 
            . . . . 2 . . . . . . 2 . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.Obstacle)
BlockMulti.y = -100
BigFallingBlock.y = -100
FallingBlock.x = -100
BiggerFallBlock.y = -100
Final_Fall.y = -100
Block.set_bounce_on_wall(True)
Final_Fall.set_bounce_on_wall(True)
Block.set_scale(2, ScaleAnchor.MIDDLE)

def on_forever():
    pause(3000)
    if game.runtime() >= 0 and game.runtime() < 30000:
        Fall()
        FallBig()
    elif game.runtime() >= 30000 and game.runtime() < 60000:
        Fall2()
        FallBig2()
    elif game.runtime() >= 60000 and game.runtime() < 120000:
        FallBigEnd()
    else:
        Fall()
        Fall2()
        FallBigEnd()
        FallBig2()
        FallBig()
forever(on_forever)
