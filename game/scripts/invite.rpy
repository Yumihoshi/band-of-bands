label memories_band_begin:

    #场景：学校外
    
    # scene bg &学校外
    # with fade

    # play music &bgm_日常 fadein 1.5
    # play audio &sfx_人群声

    "高一的春天。"
    "我和友歌、神奈、晶——我们四个人从小一起长大。"
    "青梅竹马，这个说法或许有些老套，但确实就是如此。"

    yuka "今天开始就是高中生了呢，美步子。"

    # show mhk smile at left
    # with dissolve

    mhk "嗯！终于等到这一天了！我们要一直在一起哦！"

    # show kanna normal at left
    # with dissolve

    kanna "……说什么理所当然的话呢。我们又不是非要在一起不可。"

    # show kanna tsundere at right

    "神奈虽然嘴上这么说，但她微微翘起的嘴角出卖了她。"

    # show akr shy at farleft
    # with dissolve

    akr "……嗯。"

    "晶安静地点了点头，抱紧了手中的文库本。"

    #场景：学校走廊

    # scene bg &学校走廊
    # with fade

    # stop music fadeout 0.5
    # play audio &sfx_铃声
    # pause 1.0
    # play music &bgm_情感 fadein 1.5

    "然而——"

    "高一某次分班后，我们四个人没有分到同一个班级。"

    # show mhk angry at left
    # with dissolve

    mhk "啊……四个人居然不在一个班……"

    # show yuka gentle at center
    # with dissolve

    yuka "别担心，我们还是可以在一起的。"

    # show kanna tsundere at right
    # with dissolve

    kanna "……确实有点不方便。"

    "神奈难得坦率地承认了。"
    "我看着她们的脸，脑海里浮出了一个念头。"

    # show mhk excited at left

    mhk "有了！我们组建一个乐队吧！"
    mhk "这样不管分到哪个班，放学后都能聚在一起！"

    # show kanna tsundere at right

    kanna "什么？——"
    extend "一辈子乐队吗？"

    # show yuka smile at center

    yuka "乐队？好浪漫的想法。"

    # show akr shy at farleft
    # with dissolve

    akr "……我之前学过一点键盘。"

    # show kanna tsundere at right

    kanna "……啊，也不是不行。正好我一直在学吉他。"

    mhk "那就这么定了！我是吉他主唱！友歌呢？"

    # show yuka gentle at center

    yuka "我来打鼓吧，总觉得节奏很适合我。"

    "就这样，我们的乐队Anchor诞生了。"
    "寓意着——我们是彼此的锚，无论漂流到哪里，都会回到彼此身边。"

    # stop music fadeout 1.0

    #场景：纯黑

    # scene black
    # with fade

    "然后，高二的夏天来了。"

    #场景：走廊

    # scene bg &学校走廊
    # with fade

    # play music &bgm_日常 fadein 1.5

    "新的分班结果出来了。"

    "友歌、神奈和晶被分到了同一个班。"

    "而我——"
    
    extend "为什么只有我一个人一个班！！！"

    # show mhk normal at center
    # with dissolve

    "说实话，一开始我并没有太在意。"
    "毕竟有友歌她们就在隔壁班，下课就能见面。"

    jump after_training_day

label after_training_day:

    # scene bg &排练室
    # with fade

    # play music &bgm_日常 fadein 1.5

    "天色渐暗，Anchor结束了排练日。"

    # show yuka smile at center
    # with dissolve

    yuka "大家辛苦了！今天的练习状态真好呢。"

    # show kanna normal at right
    # with dissolve

    kanna "哼，还行吧。副歌部分的转换还是有点不顺畅。"

    # show akr shy at farleft
    # with dissolve

    akr "……嗯，我觉得节拍可以再稳一些。"

    # show mhk excited at left
    # with dissolve

    mhk "诶——我觉得已经很棒了嘛！大家都超厉害的！"

    # show kanna tsundere at right

    kanna "你每次都说一样的话……"

    # show yuka gentle at center

    yuka "对了，美步子，你那个高音部分今天唱得很稳呢。"

    # show mhk smile at left

    mhk "真的吗！嘿嘿，我最近有在家偷偷练习哦！"

    # show akr smile at farleft

    akr "……我也感觉比上周好了。"

    mhk "晶也这么觉得吗！谢谢！"

    # 无意义选项
    menu:
        "今天的练习真的很开心呢。"

        "再来一首？":
            pass

        "休息一下吧？":
            pass

        "要不要喝点什么？":
            pass

    # show yuka normal at center

    yuka "好了，今天就到这里吧。大家辛苦了。"

    # show kanna normal at right

    kanna "嗯，辛苦了。"

    # show akr normal at farleft

    akr "……辛苦了。"

    # show mhk normal at left

    mhk "辛苦啦——！"

    # play audio &sfx_脚步

    "我们各自收拾好乐器。"
    "和大家告别后，我和晶一起走上了回家的路。"

    #场景：回家路上
    # scene bg &回家路上

    "晶和我家挨得很近，所以经常一起走。"

    # show mhk normal at left
    # with dissolve

    # show akr normal at right
    # with dissolve

    mhk "今天好热啊——晶你不热吗？穿这么长的袖子。"

    # show akr shy at right

    akr "……习惯了。"

    mhk "真的假的？夏天也要穿长袖？不愧是晶！"

    akr "……这有什么好佩服的。"

    "晶轻轻叹了口气。"

    # 无意义选项
    menu:
        "我们经过了回家路上的一家冰淇淋店。"

        "要不要买冰淇淋？":
            pass

        "那家店的招牌好可爱。":
            pass

        "今天走了好多路，脚好酸。":
            pass

    mhk "啊对了，晶今天的键盘solo部分超帅的！"

    # show akr shy at right

    akr "……是吗。我觉得弹得不太好。"

    mhk "才不是呢！友歌都打鼓打high了，你没注意到吗？"

    # show akr smile at right

    akr "……嗯。"

    "晶的回应虽然简短，但我能感觉到她的开心。"
    "和晶在一起的时候，沉默也不觉得尴尬。"

    # show akr normal at right

    akr "……美步子。"

    mhk "嗯？"

    akr "……谢谢你总是来找我说话。"

    mhk "我们是青梅竹马嘛！"

    # show akr shy at right

    akr "……嗯。"

    akr "……那——明天见。"

    mhk "嗯！明天见！"

    # hide akr
    # with dissolve

    # stop music fadeout 1.0

    #场景：美步子的卧室

    # scene bg &美步子的卧室
    # with fade

    # play music &bgm_日常 fadein 2.0

    "回到家，换好衣服，瘫在沙发上。"
    "正准备刷手机的时候——"

    # play audio &sfx_手机接收消息声
    # pause 0.5

    "叮。"

    extend "手机响了一下。"

    # show mhk smile at center
    # with dissolve

    "是玲发来的消息。"

    # ---- 消息演出 ----

    window hide

    show screen phone_message("白间玲", "美步子，我退出了之前的乐队。")

    pause 3.0

    hide screen phone_message

    window show

    show mhk thinking at center

    mhk "……诶？"

    "我一下子坐直了身子。"

    mhk "退出了……？"

    "虽然平时玲偶尔会提到乐队里的矛盾，但我没想到真的会走到这一步。"

    play audio se_phone
    pause 0.5

    window hide

    show screen phone_message("白间玲", "原因说来话长。\n总之，我和他们在音乐理念上合不来。")

    pause 3.0

    hide screen phone_message

    play audio se_phone
    pause 0.5

    show screen phone_message("白间玲", "不是什么大事。\n只是觉得，与其勉强在一起，不如早点放手。")

    pause 3.0

    hide screen phone_message

    window show

    "玲的文字一如既往地平静。"
    "但我知道，做出这个决定一定不容易。"

    show mhk normal at center

    "我看着天花板想了一会儿。"
    "然后，一个念头冒了出来。"

    # 无意义选项
    menu:
        "（……）"

        "等等，先冷静想一想。":
            pass

        "可是，这不是很自然的事情吗？":
            pass

        "深呼吸一下。":
            pass

    "我深吸一口气，打字。"

    play audio se_phone
    pause 0.5

    window hide

    show screen phone_message("浅间美步子", "玲，你要不要来Anchor？\n我们的贝斯手的位置，一直空着呢。")

    pause 3.0

    hide screen phone_message

    window show

    show mhk excited at center

    "手指按下发送键的那一刻，心跳加速了。"
    "我觉得这是个好主意。"
    "但我也知道，这不是我一个人能决定的事。"

    play audio se_phone
    pause 0.5

    window hide

    show screen phone_message("白间玲", "……你是认真的吗？")

    pause 2.0

    hide screen phone_message

    play audio se_phone
    pause 0.5

    show screen phone_message("浅间美步子", "认真的！\n不过我要跟其他三个人商量一下。\n明天给你答复！")

    pause 3.0

    hide screen phone_message

    play audio se_phone
    pause 0.5

    show screen phone_message("白间玲", "……好的。\n不管结果如何，谢谢你，美步子。")

    pause 3.0

    hide screen phone_message

    window show

    show mhk smile at center

    mhk "交给我吧！"

    "放下手机，我抱住了一个靠枕。"
    "明天要怎么说呢……"

    "友歌大概会温柔地同意。"
    "神奈可能会有意见……但她骨子里是个好人。"
    "晶的话……唔，她可能需要一点时间适应新人。"

    "不过没关系。"
    "我们是Anchor啊。"
    "我们会好好处理这件事的。"

    stop music fadeout 2.0
