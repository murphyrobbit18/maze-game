def on_overlap_tile(sprite, location):
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile)

def on_on_overlap(sprite2, otherSprite):
    info.change_score_by(1)
    sprites.destroy(otherSprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def on_on_overlap2(sprite3, otherSprite2):
    heroKrab.set_position(24, 24)
    tiles.place_on_random_tile(otherSprite2, sprites.dungeon.collectible_insignia)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

skeletonBoy: Sprite = None
mySprite: Sprite = None
heroKrab: Sprite = None
info.start_countdown(25)
heroKrab.set_position(24, 24)
heroKrab = sprites.create(img("""
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
    """),
    SpriteKind.player)
music.play(music.melody_playable(music.ba_ding),
    music.PlaybackMode.UNTIL_DONE)
controller.move_sprite(heroKrab, 75, 75)
scene.camera_follow_sprite(heroKrab)
tiles.set_current_tilemap(tilemap("""
    level2
"""))
info.set_score(0)
for index in range(5):
    mySprite = sprites.create(img("""
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
        """),
        SpriteKind.player)

def on_forever():
    global skeletonBoy
    skeletonBoy = sprites.create(img("""
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
        """),
        SpriteKind.enemy)
    tiles.place_on_random_tile(skeletonBoy, sprites.dungeon.collectible_insignia)
    skeletonBoy.follow(heroKrab, 75)
    pause(2000)
forever(on_forever)
