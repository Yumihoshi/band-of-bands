transform left_pos:
    anchor (0.5, 0.5)
    zoom 0.8
    xalign 0.1
    yalign 0.5
    yoffset 300
transform left_center:
    anchor (0.5, 0.5)
    zoom 0.8
    xalign 0.3
    yalign 0.5
    yoffset 300
transform center_pos:
    anchor (0.5, 0.5)
    zoom 0.8
    xalign 0.5
    yalign 0.5
    yoffset 300
transform right_center:
    anchor (0.5, 0.5)
    zoom 0.8
    xalign 0.7
    yalign 0.5
    yoffset 300
transform right_pos:
    anchor (0.5, 0.5)
    zoom 0.8
    xalign 0.9
    yalign 0.5
    yoffset 300

label bookstore:
    scene bg 回家路上
    with fade

    "某日的放学后。"

    play music bgm_日常 fadein 1.5

    show akr normal at left
    with dissolve

    show mhk normal at right
    with dissolve

    akr "美步子，这周末有空吗？我想去书店看看。"

    "晶经常邀请我一起去书店。"
    "我当然是每次都答应了。"

    mhk "好呀！"
    extend "不过……可以叫上玲一起吗？"

    akr "…………嗯，可以。"

    "虽然隔了很久才回答，但晶答应了。"
    "我立刻给玲也发了消息。"

    # ========== 场景：商场 ==========
    scene bg 商场
    with fade

    show akr normal at center
    with dissolve

    "晶看起来已经等候多时了。"

    show mhk normal at left
    with dissolve

    mhk "晶——等很久了吗？"

    akr "没有，我也才刚到一会。"

    mhk "晶刚才一直看着里面呢!这么迫不及待吗？"

    show akr shy at center

    akr "毕竟是期待了很久的作品！"

    show akr normal at center

    mhk "玲应该马上——啊，来了来了！"

    show rei normal at right
    with dissolve

    rei "久等了吗？"

    mhk "我是真的才到哦！"

    # ========== 场景：书店 ==========
    scene bg 书店
    with fade

    "晶一进书店简直像变了个人。"
    extend "这就是文学少女的开关吧！"

    akr "这个月的《现代诗手帖》到了……还有这本俳句集……"

    "晶的指尖轻轻划过书脊，眼神里闪着光。"

    rei "晶喜欢诗集吗？"

    show akr shy at center

    akr "……嗯。俳句和短歌，偶尔也看现代诗。"
    akr "十七个音节里能装下一整个世界……我觉得很了不起。"

    "晶难得说了这么长一段话。这就是文学少女吧——嗯~~~"

    show rei puzzle at right

    rei "十七个音节的世界……很有意思的说法。"

    show mhk normal at left

    mhk "呐呐，玲你平时看什么书呀？"

    show rei normal at right

    rei "我吗……主要是人物传记。偶尔也翻翻乐谱。"
    rei "比起虚构的故事，我更喜欢看真实的人是怎样走过他们的路的。"

    mhk "噢——好酷！"

    # 隐藏所有角色，准备新的布局
    hide rei
    hide mhk
    hide akr
    with dissolve

    "回过神来时，发现晶和玲站在同一个书架前。"

    show rei timid at right
    with dissolve

    show akr normal at left
    with dissolve

    akr "……这本，你看过吗？"

    "晶有些犹豫地抽出了一本书。"

    rei "……没有。这是写谁的？"

    akr "一位钢琴家。她曾经组建了一个乐队，后来解散了……"
    akr "但最后又重新聚在一起，完成了一场演出。"

    "晶说话时一直不太敢看玲的眼睛。"

    show rei smile at right

    rei "听起来很有意思。谢谢你的推荐，晶。"

    show akr shy at left

    akr "……不客气。"

    show akr normal at left
    show rei puzzle at right

    rei "晶，你推荐的这本传记……我可以买来看。"
    rei "作为交换，你有什么想看的吗？"

    show akr shy at left

    akr "交换……？"

    show rei normal at right

    rei "互相推荐各自喜欢的书。你觉得怎么样？"

    "晶愣了一下，然后轻轻点了点头。"

    akr "那……你有没有推荐的诗集？"

    show rei puzzle at right

    rei "诗集吗……我对这方面不太了解，可能没办法推荐好的。"

    "诶？这种时候不是应该顺势推荐一本然后增进感情吗？玲你也太实诚了！"

    rei "不过……如果你愿意的话，可以先让我看看你推荐的？"
    rei "我对俳句挺感兴趣的。刚才你说的——十七个音节的世界，让我很在意。"

    show akr happy at left

    "晶的眼睛一下子亮了起来。"

    akr "嗯……那、那我给你选一本入门的。"
    akr "那……美步子呢？"

    show mhk happy at center
    with dissolve

    mhk "哈哈，我是个文学白痴。可以不用管我啦！"

    "晶快步走向诗歌区，认真地挑选起来。"

    "与此同时，玲走到了乐谱专区。"

    "她拿起一本贝斯练习曲集，翻看了几页。表情认真而专注。"

    "然后，目光移向了旁边的人物传记区。"

    "犹豫了一下，她把乐谱放了回去。"

    rei "……还是选传记吧。"

    show akr smile at left  # 抱着书

    akr "谢谢你，玲！~~~"
    akr "下次我们在一起来吧！"

    stop music fadeout 1.0

    jump shopping_mall

# ========== 场景：商场（中转） ==========
label shopping_mall:
    # 简单过渡，直接跳转咖啡店
    jump coffee_shop

# ========== 场景：咖啡店 ==========
label coffee_shop:
    scene bg 咖啡店
    with fade

    # 播放咖啡店背景音乐
    play music bgm_cafe fadein 1.0

    # 同时显示所有角色，安排座位
    show mhk normal at left_pos
    show kanna normal at left_center
    show yuka normal at center_pos
    show akr normal at right_center
    show rei normal at right_pos
    with dissolve

    mhk "到了到了！就是这家！听说评价超好的！"

    kanna "你又在网上搜了多久？"

    mhk "三个小时！"

    kanna "……你真的很闲诶。"

    yuka "好啦好啦，进去吧。"

    "五个人在窗边的位置坐下，"
    "友歌和神奈坐一边，我和晶、玲坐另一边。"
    "晶坐在玲的旁边，身体微微僵硬。"

    yuka "总之，先看看菜单吧"

    "友歌把菜单递给大家。"

    menu:
        "要点些什么呢？"
        "焦糖玛奇朵 玛德琳蛋糕":
            mhk "我要焦糖玛奇朵和玛德琳蛋糕。"
        "浓缩咖啡 布朗尼蛋糕":
            mhk "我要浓缩咖啡和布朗尼蛋糕。"
        "拿铁 提拉米苏":
            mhk "我要拿铁和提拉米苏。"

    kanna "你每次都点一样的诶。"

    mhk "因为经典嘛！好吃就是高兴！"

    yuka "我就点伯爵茶吧，最近在控制咖啡因。甜点要抹茶芭菲。"

    mhk "友歌不也是和之前。"

    rei "我要点草莓奶昔和巧克力味闪电泡芙。"

    akr "我和玲一样。"

    rei "柏林炸面包？"

    akr "嗯……里面是奶油馅，外面裹着糖粉。很好吃的。"

    rei "原来如此。"

    kanna "晶之前不都是点柏林炸面包的嘛？"

    yuka "诶，晶想尝试新东西了呀。真好。"

    extend "我差点从椅子上站起来。"

    "我感觉神奈看向晶的目光里，闪过了一丝复杂的神色。"

    akr "只是……想试试看而已……"
    extend "不行吗……？"

    mhk "当然行啊！勇于尝试是好事！"

    rei "闪电泡芙很好吃的。你选对了。"

    kanna "我要美式咖啡和曲奇饼。"

    "甜点陆续端上了桌。"

    "晶面前摆着一份闪电泡芙，长长的，表面淋着巧克力酱。"
    "她拿着叉子，小心翼翼地切下了一小块。"

    akr "……嗯。好吃。"

    show akr happy at right_center

    akr "巧克力的苦味和奶油的甜味……平衡得很好。"

    rei "是吧。"

    "神奈低下头，搅动着杯中的咖啡。"

    menu:
        "这时候应该——"
        "提议大家干杯":
            pass
        "提议大家干杯":
            pass
        "提议大家干杯":
            pass

    mhk "来来来！大家干杯！"

    kanna "拿什么干杯？咖啡？"

    mhk "饮料也可以啊！"

    yuka "好呀~"

    "五个人举起各自的杯子，轻轻碰在一起。"

    "那天下午，五个人在咖啡厅里待了很久。"
    "聊了音乐，聊了书，聊了文化祭的事。"
    "也聊了一些有的没的——比如我的零花钱又花光了之类的。"

    kanna "每次都大手大脚的，你怎么活到现在的？"

    mhk "靠爱！"

    kanna "……无可救药。"

    yuka "下次我带便当来吧。"

    mhk "友歌的便当！期待！"

    rei "我也可以帮忙。"

    akr "……那我带点心。"

    kanna "你们要在学校里开野炊吗？"

    mhk "哇，好主意呢！"

    stop music fadeout 1.0
