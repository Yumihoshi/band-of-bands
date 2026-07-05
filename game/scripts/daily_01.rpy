# 日常互动1：第一次排练

label daily_01:

    stop music fadeout 1.0
    play music "bgm/bgm_humor.mp3" fadein 2.0

    # 背景：练习室（后续替换）
    scene bg 超市
    with fade

    # ===== 表情切换测试 =====
    show kanna_1 at pos2
    with dissolve
    ""
    show kanna_2 at pos2
    with dissolve
    ""
    show kanna_3 at pos2
    with dissolve
    ""
    hide kanna_3
    with dissolve
    # ===== 测试结束 =====

    "——那是玲加入乐队的第一个周末。"
    
    "然后就看到了她，玲已经在等着了。"

    "我比约定时间早了十五分钟到超市门口。"

    show mhk_normal at pos1
    with dissolve
    
    mhk "哼嗯哼~今天也是第一名"
    mhk "——诶、玲？！"

    show rei_normal at pos4
    with dissolve

    mhk "我还特意提前了十五分钟呢——"

    rei "……嗯。第一印象很重要。"

    mhk "诶嘿嘿,这么认真啊。"

    "我一边掏钥匙开门，一边忍不住多看了她一眼。"

    mhk "哇，玲的贝斯盒好新啊——边角一点磕碰都没有。"

    rei "……嗯,有在保养。"

    "进了练习室，我轻车熟路地打开空调，把散落的乐谱归拢到桌上。"
    "玲站在房间中央，目光缓缓扫过墙角那把落灰的旧吉他、键盘架上缠成一团的连接线、还有鼓凳上随手搭着的毛巾。"
    
    hide mhk
    hide rei
    with dissolve

    show mhk_normal at pos1
    with dissolve

    show rei_normal at pos4
    with dissolve

    rei "……你们平时，就这样放着吗。"

    mhk "嗯？啊——是啊，反正下次还要用嘛。"
    mhk "……呃，被你一说好像确实有点乱？"

    "话说出口我就后悔了。这回答听起来好随便。"

    "玲没有接话，只是把贝斯盒轻轻靠在墙边——很慢，很小心，像是在找一个最稳妥的角度。"

    #其他人到达

    hide mhk
    show yuka_normal at pos1
    with dissolve

    yuka "久等了——美步子可以来帮我提一下可以吗?我给大家买了点饮料。"
    yuka "啊，玲你也来的好早啊"

    mhk "对啊，我还以为今天的第一还是我呢。"
    mhk "哇,好鼓的塑料袋"
    mhk "玲你看,我就说吧,友歌很会照顾人的"

    rei "……今天也请多指教了。"

    yuka "啊嘞啊嘞，以后就是一家人啦，不用太拘谨的～"

    "我偷偷瞄了一眼玲——她的眉头似乎舒展开了一些。"

    #晶和神奈到场
    hide rei
    show akr_normal at pos4
    with dissolve

    #"晶抱着一本书,跟在友歌身后进来"

    rei "早。"
    akr "!"
    akr "……你好"
    #"晶只抬了一下眼，又迅速垂下去。"
    
    yuka "嘛,等到大家熟悉以后就会很好相处了"

    mhk "按时间来看,神奈应该也快到了"

    #"神奈出场"
    hide akr
    show kanna_normal at pos4
    with dissolve

    "她推门进来的时候，脖子上挂着耳机，头发随意地扎在脑后，目光在玲身上停了两秒。"
    kanna "……"
    kanna "哦，新人。"

    "神奈径直走到吉他旁，拿起琴随意拨了几个音，没再多说什么。"
    kanna "……嗯"
    #"玲的视线在神奈的背影上停留了一瞬，然后移开了。"

    #开始练习
    hide yuka
    hide kanna
    with dissolve

    mhk "既然人都到齐了,大家就各就各位吧"
    "友歌坐到了鼓凳上，晶在键盘前调整着音色，神奈把吉他接上音箱。"
    "玲的贝斯斜挎在身前，姿势端正得像是要上台演出。"

    mhk "咳咳,上周给玲展示的新歌,大家先试着合一遍吧。"

    #练习正式开始


    mhk "啊哈哈，又破音了,不过好开心——大家一起演奏的感觉最棒了！"

    #玲提出建议
    show mhk_normal at pos1
    with dissolve

    mhk "好,大家辛苦了！"
    mhk "怎么样，第一遍就能这样，今天的状态还不错欸。"
    #"美步子展现出排练完特有的那种满足感。"
    "然后玲把贝斯放下，安静地开口了。"

    show rei_normal at pos4
    with dissolve

    rei "……副歌的节奏，鼓和吉他没对上。"

    #"美步子的笑容僵住,凝了一瞬。"

    rei "还有键盘的第三小节，应该是 F 大调，不是 G。"

    #"晶的肩膀微微一缩。友歌从鼓后面探出头来，挠了挠脸。"

    hide mhk
    show yuka_normal at pos1
    with dissolve

    yuka "啊……确实，那块我老是抢拍，哈哈。"

    "友歌笑得很轻松，美步子松了口气——果然还是友歌，气氛顿时缓和了许多。"

    "但神奈没有笑。"

    hide yuka
    show kanna_normal at pos1
    with dissolve

    kanna "……第一次练习，差不多就行了吧。"

    mhk "神奈……"
    mhk "好啦好啦！玲说得对，那一段确实有点小问题。不过毕竟是今天第一次嘛，先找找感觉，慢慢来～"

    rei "……"

    hide kanna
    show mhk_normal at pos1
    with dissolve

    "玲没有继续坚持。她低下头，重新拿起贝斯。"
    "指尖在琴弦上轻轻划过，没有发出声音。"

    "————"
    #休息时间
    hide mhk
    hide rei
    with dissolve

    "休息的时候，美步子坐到玲旁边。"

    show mhk_normal at pos1
    with dissolve
    mhk "玲，我跟你说——你知道我们当初是怎么凑到一起的吗？"

    rei "……啊,是怎么回事?"

    mhk "其实就是高二分班的时候——我们四个居然不在一个班。当时我就想，那可不行，得找个理由把大家聚在一起。"
    mhk "然后我就说，我们组乐队吧！这样不管分到哪个班，放学后都能在一起。"
    mhk "一开始只是想找个借口而已……结果莫名其妙就变成真的了。"

    "玲听着，偶尔点一下头。但美步子总觉得那双眼睛在看向别处。"

    mhk "……玲？"

    rei "……嗯。很有意思。"

    "玲把贝斯又往怀里拢了拢，像抱着一个只有自己知道的东西。"

    #"美步子看在眼里，有点不安。"
    #"她看了一眼练习室里的其他人——"

    mhk "友歌在发饮料，晶在练指法，神奈又戴耳机了……跟平时一模一样。"

    "但似乎，有什么东西跟平时不太一样了。"
    # 排练结束

    hide mhk
    hide rei
    with dissolve

    "第二次合的时候，友歌特意在副歌那里放慢了半拍。"
    "这次总算对上了。"

    mhk "……节奏是对了，但怎么感觉软绵绵的。"

    "神奈弹完最后一个音，把吉他往架子上一靠，甩了甩手。"

    show kanna_normal at pos3
    with dissolve

    kanna "今天就这样吧，手酸了。"

    mhk "神奈今天是不是比平时更急？"

    hide kanna
    show mhk_normal at pos3
    with dissolve

    mhk "嗯,大家辛苦了!  ——下周还是这个时间吧？"

    "友歌和晶都应了一声。神奈已经走到门口了，手插在口袋里，背影看不出什么表情。"

    rei "那我也准备收拾了"

    mhk "玲……"

    hide mhk
    show rei_normal at pos3
    with dissolve

    "玲低头看着琴弦，指腹轻轻按在第四弦上，没有声音。"

    "我从后面探过头去，尽量让自己的声音听起来明亮。"

    hide rei
    show mhk_normal at pos1
    with dissolve

    mhk "玲，今天感觉怎么样？大家人都很好吧～"

    "玲抬起头，看着我。"

    show rei_normal at pos4
    with dissolve

    rei "……嗯。"

    "她又低下去了。"
    "贝斯盒的卡扣发出清脆的一声「咔」。"
    "那个「嗯」后面还有很多没说完的话。"
    "但此时，已经开不了口了。"

    #结尾
    hide mhk
    hide rei
    with dissolve

    "走出练习室的时候，天色已经偏暗了。"
    "友歌和晶在路口等车，神奈已经走远了，耳机线在背后晃来晃去。"

    mhk "玲,今天一起回家吧"

    "我追上了前面的玲，和她并肩走着。"
    "但我却发现——我居然不知道该怎么开口"
    "平时最擅长找话题的我，此刻脑子里翻来覆去转了好几圈，却一个字也说不出来。"
    "夕阳把玲的轮廓描了一层金边，但那双眼——还是看不出什么情绪。"

    mhk "（没关系的。）"
    mhk "（才第一次排练而已。下次一定会更好。）"

    "但我在说服谁呢。"

    "我们的影子被夕阳拉得很长，一高一低，像是两根还没调好音的弦。"

    stop music fadeout 3.0

    "——玲加入乐队后的第一次排练，就这样结束了。"

    return