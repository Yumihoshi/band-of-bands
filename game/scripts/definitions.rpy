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
image bg 超市 = "background/store.png"

# 角色立绘
image rei 通常 = "images/rei.png"
image akr 通常 = "images/akr.png"

# ============================================================
# 锚点与位置设置
# ============================================================

transform at_left:
    anchor (0.5, 0.5)
    zoom 0.8
    xalign 0.10
    yalign 0.50
    yoffset 300

transform at_center:
    anchor (0.5, 0.5)
    zoom 0.8
    xalign 0.50
    yalign 0.50
    yoffset 300

transform at_right:
    anchor (0.5, 0.5)
    zoom 0.8
    xalign 0.90
    yalign 0.50
    yoffset 300