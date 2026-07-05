label bookstore:

    #场景:回家路上
    scene bg &回家路上
    with fade

    "某日的放学后。"

    play music &bgm_日常 fadein 1.5

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

    #场景:商场

    scene bg &商场
    with fade

    show akr normal at center

    "晶看起来已经等候多时了。"

    show mhk normal at left

    mhk "晶——等很久了吗？"

    akr "没有，我也才刚到一会。"

    mhk "晶刚才一直看着里面呢!这么迫不及待吗？"

    show akr shy at center

    akr "毕竟是期待了很久的作品！"

    show akr normal at center

    mhk "玲应该马上——啊，来了来了！"

    show rei normal at right

    rei "久等了吗？"

    mhk "我是真的才到哦！"

    #场景:书店

    scene bg &书店
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

    mhk "呐呐，玲你平时看什么书呀？"

    show rei normal at right

    rei "我吗……主要是人物传记。偶尔也翻翻乐谱。"

    rei "比起虚构的故事，我更喜欢看真实的人是怎样走过他们的路的。"

    mhk "噢——好酷！"

    hide rei
    hide mhk
    hide akr

    "回过神来时，发现晶和玲站在同一个书架前。"

    show rei timid at right

    show akr normal at left

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

    mhk "哈哈，我是个文学白痴。可以不用管我啦！"

    "晶快步走向诗歌区，认真地挑选起来。"

    "与此同时，玲走到了乐谱专区。"

    "她拿起一本贝斯练习曲集，翻看了几页。表情认真而专注。"

    "然后，目光移向了旁边的人物传记区。"

    "犹豫了一下，她把乐谱放了回去。"

    rei "……还是选传记吧。"

    show akr smile at left#抱着书

    akr "谢谢你，玲！~~~"

    jump shopping_mall
    
label shopping_mall:
    jump coffee_shop
label coffee_shop:

    return
