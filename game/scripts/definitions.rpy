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
image bg 便利店 = "background/snack_store.png"
image bg 书店 = "background/bookstore.png"
image bg 学校走廊 = "background/hallway.png"
image bg 咖啡馆 = "background/cafe.png"
image bg 桌椅1 = "background/desk_chair_01.png"
image bg 桌椅2 = "background/desk_chair_02.png"
image bg 桌椅3 = "background/desk_chair_03.png"
image bg 桌椅4 = "background/desk_chair_04.png"
image bg 公园路 = "background/street_park.png"
image bg 河边 = "background/street_river.png"
image bg 商店 = "background/store.png"
image bg 舞台 = "background/stage.png"

# 角色立绘
image rei_normal = "images/rei_normal.png"
image akr_normal = "images/akr_normal.png"
image yuka_normal = "images/yuka_normal.png"
image kanna_normal = "images/kanna_normal.png"
image mhk_normal = "images/mhk_normal.png"

#表情差分



# ============================================================
# 锚点与位置设置
# ============================================================

transform pos1:
    anchor (0.5, 0.5)
    zoom 0.8
    xalign 0.125
    yalign 0.50
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

transform pos2:
    anchor (0.5, 0.5)
    zoom 0.8
    xalign 0.375
    yalign 0.50
    yoffset 300

transform pos3:
    anchor (0.5, 0.5)
    zoom 0.8
    xalign 0.625
    yalign 0.50
    yoffset 300

transform pos4:
    anchor (0.5, 0.5)
    zoom 0.8
    xalign 0.875
    yalign 0.50
    yoffset 300