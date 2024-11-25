namespace SpriteKind {
    export const Obstacle = SpriteKind.create()
}
function FallBig () {
    BigFallingBlock.setPosition(randint(30, 100), 0)
    BigFallingBlock.setVelocity(0, 60)
    animation.runImageAnimation(
    BigFallingBlock,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
    pause(1000)
}
function Fall () {
    animation.runImageAnimation(
    FallingBlock,
    [img`
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
        `,img`
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
        `],
    500,
    true
    )
    FallingBlock.setPosition(randint(30, 140), 0)
    FallingBlock.setVelocity(0, 30)
    pause(2000)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Obstacle, function (sprite, otherSprite) {
    info.setScore(Math.abs(game.runtime()) / 1000)
    game.setGameOverScoringType(game.ScoringType.HighScore)
    game.gameOver(false)
    game.setGameOverMessage(false, "Your High Score is :" + convertToText(info.score()) + "")
})
function FallBig2 () {
    BiggerFallBlock.startEffect(effects.rings)
    animation.runMovementAnimation(
    BigFallingBlock,
    animation.animationPresets(animation.parachuteRight),
    1000,
    true
    )
    BiggerFallBlock.setPosition(randint(50, 110), 0)
    BiggerFallBlock.setVelocity(randint(-30, 30), 79)
    pause(1500)
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    Block.setVelocity(-50, 0)
})
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    Block.setVelocity(0, 0)
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    Block.setVelocity(0, 0)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    Block.setVelocity(50, 0)
})
function FallBigEnd () {
    Final_Fall.startEffect(effects.fire)
    Final_Fall.setVelocity(randint(-80, 80), 90)
}
function Fall2 () {
    animation.runImageAnimation(
    BlockMulti,
    assets.animation`newMultifall`,
    500,
    true
    )
    BlockMulti.setPosition(randint(30, 150), 0)
    BlockMulti.setVelocity(0, 30)
    pause(2000)
}
let BlockMulti: Sprite = null
let Final_Fall: Sprite = null
let BiggerFallBlock: Sprite = null
let BigFallingBlock: Sprite = null
let FallingBlock: Sprite = null
let Block: Sprite = null
game.showLongText("Welcome to Crushed.io", DialogLayout.Center)
game.showLongText("Try not to get Crushed!!! " + "Accpet the challenge", DialogLayout.Center)
scene.setBackgroundImage(assets.image`Background`)
Block = sprites.create(assets.image`Block`, SpriteKind.Player)
FallingBlock = sprites.create(assets.image`Falling Block`, SpriteKind.Obstacle)
BigFallingBlock = sprites.create(assets.image`BigBlockF`, SpriteKind.Obstacle)
BiggerFallBlock = sprites.create(assets.image`BiggerFallB`, SpriteKind.Obstacle)
Final_Fall = sprites.create(assets.image`FancyBlog`, SpriteKind.Obstacle)
BlockMulti = sprites.create(img`
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
    `, SpriteKind.Obstacle)
BlockMulti.y = -100
BigFallingBlock.y = -100
FallingBlock.x = -100
BiggerFallBlock.y = -100
Final_Fall.y = -100
Block.setBounceOnWall(true)
Final_Fall.setBounceOnWall(true)
scaling.scaleToPixels(Block, 40, ScaleDirection.Uniformly, ScaleAnchor.Middle)
forever(function () {
    pause(3000)
    if (game.runtime() >= 0 && game.runtime() < 30000) {
        Fall()
        FallBig()
    } else if (game.runtime() >= 30000 && game.runtime() < 60000) {
        FallBig2()
        Fall2()
        scaling.scaleToPixels(Block, 20, ScaleDirection.Horizontally, ScaleAnchor.Middle)
    } else if (game.runtime() >= 60000 && game.runtime() < 120000) {
        FallBigEnd()
    } else {
        Fall()
        Fall2()
        FallBigEnd()
        FallBig2()
        FallBig()
    }
})
