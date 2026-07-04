#日常互动1

# ============================================================
# 锚点与位置设置
# ============================================================

transform at_left:
    anchor (0.5, 0.5)
    zoom 0.6
    xalign 0.20
    yalign 0

transform at_center:
    anchor (0.5, 0.5)
    zoom 0.6
    xalign 0.50
    yalign 0

transform at_right:
    anchor (0.5, 0.5)
    zoom 0.6
    xalign 0.80
    yalign 0


# --- 入场/退场动画 ---
transform slide_in_left:
    xalign -0.3 yalign 0.5 alpha 0.0
    linear 0.5 xalign 0.20 alpha 1.0

transform slide_in_right:
    xalign 1.3 yalign 0.5 alpha 0.0
    linear 0.5 xalign 0.80 alpha 1.0

transform fade_in:
    alpha 0.0
    linear 0.5 alpha 1.0


# ============================================================
# 场景：日常01
# ============================================================

label daily_01:

    stop music fadeout 1.0
    
    #显示背景
    scene bg 超市
    with fade

    "——练习室里，乐队成员们陆续到齐。"

    #立绘显示
    show rei 通常 at at_left
    with dissolve

    # show akr 通常 at at_right
    # with dissolve

    
    play music "bgm/bgm_humor.mp3" fadein 2.0

    #---对话---
    "玲和晶先到了，两人聊了起来。"

    rei "今天的练习从基础热身开始吧。"

    akr "赞成。昨天的新曲子我回去练了一下，感觉副歌部分还需要再磨合。"

    rei "嗯，那我们今天就重点练副歌。等其他人到了就开始。"

    akr "好，我先热热身。"

    #场景结束，停止音乐
    stop music fadeout 2.0

    "——练习室的午后，乐队的日常才刚刚开始。"

    #清理所有立绘
    hide yuka
    hide akr
    with dissolve

    return