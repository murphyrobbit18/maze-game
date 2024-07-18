scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestClosed, function (sprite, location) {
    game.gameOver(true)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    sprites.destroy(otherSprite, effects.spray, 500)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    heroKrab.setPosition(24, 24)
    tiles.placeOnRandomTile(otherSprite, sprites.dungeon.collectibleInsignia)
})
let skeletonBoy: Sprite = null
let mySprite: Sprite = null
let heroKrab: Sprite = null
info.startCountdown(25)
heroKrab.setPosition(24, 24)
heroKrab = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . c c c c c c . . . 
    . . . . . . c b 3 3 3 b c c . . 
    . . c c . c b c c 3 3 b b 3 c . 
    . b 7 7 c b c 7 7 c 3 3 3 3 3 c 
    . f f 7 c b c 7 f f 3 3 3 3 3 c 
    . f f 7 c b c 7 f f b 3 3 3 c c 
    . b 7 7 3 c 3 7 7 c b b b b c c 
    . . b 7 7 3 7 7 c 3 3 3 3 3 3 c 
    . c c 7 7 7 7 7 b c c 3 3 3 3 c 
    c 7 7 6 7 7 7 6 b 7 7 c 3 3 c . 
    b 7 6 b 6 6 6 6 b b 7 c b b . . 
    c 6 7 7 b 6 b 7 7 7 6 c 6 7 b . 
    c 7 7 7 c 6 c 7 7 7 c 6 c 7 c . 
    c 7 7 7 7 c 7 7 7 7 c 6 c 7 c . 
    . c c c c c c c c c . . c c c . 
    `, SpriteKind.Player)
music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.UntilDone)
controller.moveSprite(heroKrab, 75, 75)
scene.cameraFollowSprite(heroKrab)
tiles.setCurrentTilemap(tilemap`level2`)
info.setScore(0)
for (let index = 0; index < 5; index++) {
    mySprite = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . 4 4 4 4 . . . . . . 
        . . . . 4 4 4 5 5 4 4 4 . . . . 
        . . . 3 3 3 3 4 4 4 4 4 4 . . . 
        . . 4 3 3 3 3 2 2 2 1 1 4 4 . . 
        . . 3 3 3 3 3 2 2 2 1 1 5 4 . . 
        . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 . 
        . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 . 
        . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 . 
        . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 . 
        . . 4 2 3 3 2 4 4 4 4 4 2 4 . . 
        . . 4 2 2 3 2 2 4 4 4 2 4 4 . . 
        . . . 4 2 2 2 2 2 2 2 2 4 . . . 
        . . . . 4 4 2 2 2 2 4 4 . . . . 
        . . . . . . 4 4 4 4 . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.Player)
}
forever(function () {
    skeletonBoy = sprites.create(img`
        ........................
        ........................
        ........................
        ........................
        ..........ffff..........
        ........ff1111ff........
        .......fb111111bf.......
        .......f11111111f.......
        ......fd11111111df......
        ......fd11111111df......
        ......fddd1111dddf......
        ......fbdbfddfbdbf......
        ......fcdcf11fcdcf......
        .......fb111111bf.......
        ......fffcdb1bdffff.....
        ....fc111cbfbfc111cf....
        ....f1b1b1ffff1b1b1f....
        ....fbfbffffffbfbfbf....
        .........ffffff.........
        ...........fff..........
        ........................
        ........................
        ........................
        ........................
        `, SpriteKind.Enemy)
    tiles.placeOnRandomTile(skeletonBoy, sprites.dungeon.collectibleInsignia)
    skeletonBoy.follow(heroKrab, 75)
    pause(2000)
})
