# ==============================================================================
# 角色名
# ==============================================================================
define yuka = Character("今若 友歌")#妈妈
define akr = Character("米野 晶")#内向
define kanna = Character("卫宫 神奈")#叛逆
define rei = Character("白间 玲")#认真
define mhk = Character("浅间 美步子")#外向

define band_name = "抛锚乐队"
define debug = True

# 背景
image bg 商店 = "background/snack_store.png"
image bg 书店 = "background/bookstore.png"
image bg 学校走廊 = "background/hallway.png"
image bg 咖啡馆 = "background/cafe.png"
image bg 桌椅1 = "background/desk_chair_01.png"
image bg 桌椅2 = "background/desk_chair_02.png"
image bg 桌椅3 = "background/desk_chair_03.png"
image bg 桌椅4 = "background/desk_chair_04.png"
image bg 公园路 = "background/street_park.png"
image bg 河边 = "background/street_river.png"
image bg 舞台 = "background/stage.png"
image bg 练习室 = "background/practice_room.png"
image bg 音乐商店 = "background/music_store.png"
image bg 商场 = "background/shopping_mall.png"


# 角色立绘
image rei normal = "images/rei_normal.png"
image akr normal = "images/akr_normal.png"
image yuka normal = "images/yuka_normal.png"
image kanna normal = "images/kanna_normal.png"
image mhk normal = "images/mhk_normal.png"

#表情差分

# character_action 目录下的动作/表情图片
# baiyu
image character_action baiyu action_01 = "images/character_action/baiyu/by_Action_01.png"
image character_action baiyu action_02 = "images/character_action/baiyu/by_Action_02.png"
image character_action baiyu normal = "images/character_action/baiyu/by_emotion_normal.png"
image character_action baiyu puzzle = "images/character_action/baiyu/by_emotion_puzzle.png"
image character_action baiyu shy = "images/character_action/baiyu/by_emotion_shy.png"
image character_action baiyu smile = "images/character_action/baiyu/by_emotion_smile.png"
image character_action baiyu timid = "images/character_action/baiyu/by_emotion_timid.png"

# hx
image character_action hx idle = "images/character_action/hx/character_hx_idle.png"
image character_action hx upset = "images/character_action/hx/hx_emotion_upset.png"
image character_action hx worry = "images/character_action/hx/hx_emotion_worry.png"

# ly
image character_action ly hostile = "images/character_action/ly/ly_emotion_hostile(dishi).png"
image character_action ly kill_u = "images/character_action/ly/ly_emotion_kill u.png"
image character_action ly normal = "images/character_action/ly/ly_emotion_normal.png"
image character_action ly speechless = "images/character_action/ly/ly_emotion_speechless.png"

# sk
image character_action sk action_01 = "images/character_action/sk/sk_Action_01.png"
image character_action sk angry = "images/character_action/sk/sk_emotion_angry.png"
image character_action sk normal = "images/character_action/sk/sk_emotion_normal.png"
image character_action sk nyjk = "images/character_action/sk/sk_emotion_nyjk.png"
image character_action sk puzzle = "images/character_action/sk/sk_emotion_puzzle.png"
image character_action sk smile = "images/character_action/sk/sk_emotion_smile.png"

# ymq
image character_action ymq action_01 = "images/character_action/ymq/ymq_Action_01.png"
image character_action ymq angry = "images/character_action/ymq/ymq_emotion_angry.png"
image character_action ymq at_a_loss = "images/character_action/ymq/ymq_emotion_at a loss.png"
image character_action ymq excited = "images/character_action/ymq/ymq_emotion_excited.png"
image character_action ymq foolish_laugh = "images/character_action/ymq/ymq_emotion_foolish-laugh.png"
image character_action ymq normal = "images/character_action/ymq/ymq_emotion_normal.png"
image character_action ymq shocked = "images/character_action/ymq/ymq_emotion_shocked.png"
image character_action ymq upset = "images/character_action/ymq/ymq_emotion_upset.png"# ============================================================
# 锚点与位置设置
# ============================================================

transform pos1:
    anchor (0.5, 0.5)
    zoom 0.8
    xalign 0.125
    yalign 0.50
    xoffset -180
    yoffset 300


transform pos2:
    anchor (0.5, 0.5)
    zoom 0.8
    xalign 0.375
    yalign 0.50
    xoffset -100
    yoffset 300

transform pos3:
    anchor (0.5, 0.5)
    zoom 0.8
    xalign 0.625
    yalign 0.50
    xoffset 100
    yoffset 300

transform pos4:
    anchor (0.5, 0.5)
    zoom 0.8
    xalign 0.875
    yalign 0.50
    xoffset 180
    yoffset 300

# ==============================================================================
# 音乐
# ==============================================================================
define bgm_citypop_01 = "bgm/bgm_city pop_01.ogg"
define bgm_citypop_02 = "bgm/bgm_city pop_02.ogg"
define bgm_humor = "bgm/bgm_humor.ogg"
define bgm_live = "bgm/bgm_live.ogg"
define bgm_peaceful = "bgm/bgm_peaceful.ogg"
define bgm_serious = "bgm/bgm_serious.ogg"
define bgm_hope = "bgm/bgm_hope.ogg"

# ==============================================================================
# 音效
# ==============================================================================
define sfx_book = "sfx/sfx_bookl.mp3"
define sfx_crowd = "sfx/sfx_crowd.mp3"
define sfx_dengdeng = "sfx/sfx_dengdeng.mp3"
define sfx_door = "sfx/sfx_door.mp3"
define sfx_phone = "sfx/sfx_phone.mp3"
define sfx_school = "sfx/sfx_scholl.mp3"
define sfx_tip = "sfx/sfx_tip.wav"
define sfx_walk = "sfx/sfx_walk.wav"