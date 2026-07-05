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
image rei_normal = "images/rei_normal.png"
image akr_normal = "images/akr_normal.png"
image yuka_normal = "images/yuka_normal.png"
#image kanna_normal = "images/kanna_normal.png"
#image mhk_normal = "images/mhk_normal.png"

#表情差分
image kanna_1 = "images/kanna_1.png"
image kanna_2 = "images/kanna_2.png"
image kanna_3 = "images/kanna_3.png"


# ============================================================
# 锚点与位置设置
# ============================================================

transform pos1:
    anchor (0.5, 0.5)
    zoom 0.8
    xalign 0.125
    yalign 0.50
    yoffset 300

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