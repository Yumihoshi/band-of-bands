label memories_band_begin:

    #场景：学校外
    
    scene bg 公园路
    with fade
    play music "bgm/bgm_peaceful.ogg" fadein 1.5
    play sound "sfx/sfx_crowd.mp3"

    "高一的春天。"
    "我和友歌、神奈、晶——我们四个人从小一起长大。"
    "青梅竹马，这个说法或许有些老套，但确实就是如此。"

    stop sound fadeout 2.0

    yuka "今天开始就是高中生了呢，美步子。"

    show mhk smile at pos1
    with dissolve

    mhk "嗯！终于等到这一天了！我们要一直在一起哦！"

    show kanna normal at pos2
    with dissolve

    kanna "……说什么理所当然的话呢。我们又不是非要在一起不可。"

    show kanna tsundere at pos2

    "神奈虽然嘴上这么说，但她微微翘起的嘴角出卖了她。"

    show akr shy at pos3
    with dissolve

    akr "……嗯。"

    "晶安静地点了点头，抱紧了手中的文库本。"

    #场景：学校走廊

    scene bg 学校走廊
    with fade

    stop music fadeout 0.5
    pause 1.0
    play music "bgm/bgm_hope.ogg" fadein 1.5

    "然而——"

    "高一某次分班后，我们四个人没有分到同一个班级。"

    show mhk angry at pos2
    with dissolve

    mhk "啊……四个人居然不在一个班……"

    show yuka gentle at pos3
    with dissolve

    yuka "别担心，我们还是可以在一起的。"

    show kanna tsundere at pos1
    with dissolve

    show akr normal at pos4

    kanna "……确实有点不方便。"

    "神奈难得坦率地承认了。"
    "我看着她们的脸，脑海里浮出了一个念头。"

    show mhk excited at pos2

    mhk "有了！我们组建一个乐队吧！"

    mhk "这样不管分到哪个班，放学后都能聚在一起！"

    show kanna tsundere at pos1
    kanna "什么？——"
    extend "一辈子乐队吗？"

    show yuka smile at pos3

    yuka "乐队？好浪漫的想法。"

    show akr shy at pos4
    with dissolve

    akr "那个……我之前学过一点键盘。"

    show kanna tsundere at pos1

    kanna "……啊，也不是不行啦。正好我一直在学吉他。"

    mhk "那就这么定了！我是吉他主唱！友歌呢？"

    show yuka gentle at pos3

    yuka "我来打鼓吧，总觉得节奏很适合我。"

    "就这样，我们的乐队Anchor诞生了。"
    "寓意着——我们是彼此的锚，无论漂流到哪里，都会回到彼此身边。"

    stop music fadeout 1.0

    #场景：纯黑

    scene black
    with fade

    "然后，高二的夏天来了。"

    #场景：走廊

    scene bg 学校走廊
    with fade

    play music "bgm/bgm_peaceful.ogg" fadein 1.5

    "新的分班结果出来了。"

    "友歌、神奈和晶被分到了同一个班。"

    "而我——"
    
    extend "为什么只有我一个人一个班！！！！！！"

    show mhk normal at at_center
    with dissolve

    "说实话，一开始我并没有太在意。"
    "毕竟有友歌她们就在隔壁班，下课就能见面。"

    stop music fadeout 1.0

    jump after_training_day

label after_training_day:

    scene bg 教室

    show rei normal at at_left

    show mhk normal at at_right

    mhk "玲今天也要去乐队吗？"

    rei "嗯。我们乐队几乎每天都有训练。"

    mhk "真是辛苦呢。明天见了。"

    scene bg 排练室
    with fade

    play music "bgm/bgm_peaceful.ogg" fadein 1.5

    "天色渐暗，Anchor结束了排练日。"

    show yuka smile at pos1
    with dissolve

    yuka "大家辛苦了！今天的练习状态真好呢。"

    show kanna normal at pos2
    with dissolve

    kanna "哼，还行吧。副歌部分的转换还是有点不顺畅。"

    show akr shy at pos3
    with dissolve

    akr "……嗯，我觉得节拍可以再稳一些。"

    show mhk excited at pos4
    with dissolve

    mhk "诶——我觉得已经很棒了嘛！大家都超厉害的！"

    show kanna tsundere at pos2

    kanna "你每次都说一样的话……"

    show yuka gentle at pos1

    yuka "对了，美步子，你那个高音部分今天唱得很稳呢。"

    show mhk smile at pos4

    mhk "真的吗！嘿嘿，我最近有在家偷偷练习哦！"

    show akr smile at pos3

    akr "……我也感觉比上周好了。"

    mhk "晶也这么觉得吗！谢谢！"

    
    menu:
        "今天的练习真的很开心呢。"

        "再来一首？":
            pass

        "休息一下吧？":
            pass

        "要不要喝点什么？":
            pass

    show yuka normal at pos1

    yuka "好了，今天就到这里吧。大家辛苦了。"

    show kanna normal at pos2

    kanna "嗯，辛苦了。"

    show akr normal at pos3

    akr "……辛苦了。"

    show mhk normal at pos4

    mhk "辛苦啦——！"

    "我们各自收拾好乐器。"
    "和大家告别后，我和晶一起走上了回家的路。"

    play audio "=sfx/sfx_walk.wav"

    #场景：回家路上
    scene bg 公园路
    with fade

    "晶和我家挨得很近，所以经常一起走。"

    show mhk normal at at_left
    with dissolve

    show akr normal at at_right
    with dissolve

    mhk "今天好热啊——晶你不热吗？穿这么长的袖子。"

    show akr shy at at_right

    akr "……习惯了。"

    mhk "真的假的？夏天也要穿长袖？不愧是晶！"

    akr "……这有什么好佩服的。"

    "晶轻轻叹了口气。"

    
    menu:
        "我们经过了回家路上的一家冰淇淋店。"

        "要不要买冰淇淋？":
            pass

        "那家店的招牌好可爱。":
            pass

        "今天走了好多路，脚好酸。":
            pass

    mhk "啊对了，晶今天的键盘solo部分超帅的！"

    show akr shy at at_right

    akr "……是吗。我觉得弹得不太好。"

    mhk "才不是呢！友歌都打鼓打high了，你没注意到吗？"

    show akr smile at at_right

    akr "……嗯。"

    "晶的回应虽然简短，但我能感觉到她的开心。"
    "和晶在一起的时候，沉默也不觉得尴尬。"

    show akr normal at at_right

    akr "……美步子。"

    mhk "嗯？"

    akr "……谢谢你总是来找我说话。"

    mhk "我们是青梅竹马嘛！"

    show akr shy at at_right

    akr "……嗯。"

    akr "……那——明天见。"

    mhk "嗯！明天见！"

    hide akr
    with dissolve

    stop music fadeout 1.0

    #场景：美步子的卧室

    scene bg 卧室
    with fade

    play music "bgm/bgm_peaceful.ogg" fadein 2.0

    "回到家，换好衣服，瘫在沙发上。"
    "正准备刷手机的时候——"

    play audio "sfx/sfx_tip.wav"
    pause 0.5

    "手机震动了一下。"

    show mhk smile at at_center
    with dissolve

    "是玲发来的消息。"

    rei "美步子，我退出了之前的乐队。"

    show mhk shocked at at_center

    mhk "……诶？？？？？"

    "我一下子坐直了身子。"

    show mhk normal at at_center

    mhk "退出了……？"

    "虽然平时玲偶尔会提到乐队里的矛盾，但我没想到真的会走到这一步。"

    rei "原因说来话长。"
    
    extend "总之，我和他们在音乐理念上合不来。"

    rei "不是什么大事。只是一部分的人际关系啦。"

    rei "不过我早就说过主唱要找女孩子啦!"

    show mhk shocked at at_center

    mhk "诶？为什么这么说呢？"

    rei "美步子你想啊，一个乐队有男有女的话，就会因为男女关系纠葛不清而解散了！"

    menu:
        mhk "……"

        "原来是这样吗？":
            mhk "原来是这样吗？"
            pass

        "这就是前辈留的教诲吗？":
            mhk "这就是前辈留的教诲吗？"
            pass

        "那可真是太坏了！":
            mhk "那可真是太坏了！"
            pass
    
    rei "也好，与其勉强在一起，不如早点放手。"

    rei "不过呢，看来我要组个新乐队了!"

    show mhk normal at at_center

    mhk "玲，你要不要来Anchor。"

    extend "我们的贝斯手的位置，一直空着呢。"

    "手指按下发送键的那一刻，心跳加速了。"
    "我觉得这是个好主意。"
    "但我也知道，这不是我一个人能决定的事。"

    rei "……你是认真的吗？"

    show mhk excited at at_center

    mhk "当然！"
    
    extend "不过我要跟其他三个人商量一下……"

    rei "…………好的。"
    
    extend "不管结果如何，谢谢你，美步子。"

    show mhk smile at at_center

    mhk "交给我吧！"

    "放下手机。明天要怎么说呢……"

    "友歌大概会温柔地同意。"
    "神奈可能会有意见……但她骨子里是个好人。"
    "晶的话……唔，她可能需要一点时间适应新人。"

    "不过没关系。"
    "我们会好好处理这件事的。"

    stop music fadeout 2.0

    #加人提案，场景：纯黑

    scene black
    with fade

    "第二天。"

    #场景：学校走廊

    scene bg 学校走廊
    with fade

    play music "bgm/bgm_peaceful.ogg" fadein 1.5

    play audio "=sfx/sfx_door.mp3"

    "放学后的走廊。四个人到齐了。"

    show yuka normal at pos1
    with dissolve

    show kanna normal at pos2
    with dissolve

    show akr normal at pos3
    with dissolve

    show mhk normal at pos4
    with dissolve

    "我站在三个人面前。"

    mhk "那个……米娜桑，我有件事想说。"

    show yuka smile at pos1

    yuka "嗯，说吧。"

    "友歌的声音一如既往地温柔。"

    show mhk smlie at pos4

    mhk "……我们的乐队，其实一直少一个贝斯手对吧？"

    show kanna puzzle at pos2

    kanna "美步子想找人帮忙拿外卖了吗？"

    akr "贝斯……还是很重要的。"

    kanna "比如贝斯不去拿外卖的话，我们今晚吃什么？"

    yuka "美步子，你已经有人选了吧？"

    "不愧是友歌,一如既往的敏锐呢！"

    show mhk normal at pos4

    mhk "嗯……是我班上的同学，白间玲。"

    show kanna normal at pos2

    kanna "……白间？我没听说过。"

    yuka "白间同学吗，我高一和她同班来着。"
    
    yuka "不过我们没什么交集就是了。"

    "这我倒是不奇怪。"

    show akr shy at pos3

    akr "美步子，你觉得她怎么样呢？"

    mhk "她是个很认真的人！对音乐非常有热情。而且……"

    mhk "而且我觉得，她如果加入的话，我们的演奏会变得更好。"

    akr "没有贝斯，低音部分一直有些薄弱呢。"

    show akr normal at pos3

    yuka "……美步子推荐的人，应该没问题的。"

    show kanna worreid at pos2
    kanna "……可是，我们四个人一直在一起的。加一个外人进来——"

    show yuka normal at pos1

    yuka "那么我们先见见这个人，然后再做决定吧。」"

    show mhk smile at pos4

    mhk "嗯！这样最好！"

    show akr shy at pos3

    akr "……我也觉得。先见面看看。"

    show kanna normal at pos2

    kanna "……哼。好吧，既然大家都这么说的话。"