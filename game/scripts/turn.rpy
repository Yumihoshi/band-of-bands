# ==============================================================================
# 矛盾 & 转折
# label以turn_开头，表示剧情的转折点
# ==============================================================================

# 排练中原成员依旧插科打诨，认真系无法认同，
# 阐述自己的想法，再次被忽视，爆了
label turn_boom:
    # 前面练习了很多次，排练提前
    scene bg 卧室 with dissolve
    show character_action mhk excited at pos_center
    # 塑造元气笨蛋 & 社交依赖
    mhk "啊——又一天结束了，排练的日子可真辛苦啊。"
    mhk "终于可以好好休息了，嘿嘿~"
    hide character_action mhk with dissolve
    show character_action mhk action_01 at pos_center with dissolve
    mhk "软乎乎的被窝，我来啦~"
    hide character_action mhk with dissolve
    show character_action mhk excited at pos_center with dissolve
    "呼——，好舒服啊~大概谁都不会拒绝被窝的邀请吧。"
    "简直像是掉入了玲的怀抱一样。"
    "玲——"
    mhk "嘿嘿…嘿嘿嘿嘿……（傻笑）"
    play sound sfx_phone
    mhk "啊啊啊难道我想见玲的心情被传达出去了？来啦来啦~"
    rei "喂喂喂，是美步子吗？练习结束有件事忘记和你说了。"
    mhk "原来是玲啊，这么晚遇到什么事啦？"
    # 埋下特殊的练习伏笔：暴露乐队懒散，埋下玲已经失望过一次的暗示
    rei "明天的练习……我想提前一小时，不过如果你觉得没必要的话，照常也可以。"
    mhk "提前？！可是我本来打算明天睡个懒觉的。"
    rei "……那你来不来？"
    mhk "我…我当然会去啦，真是的，你就是太紧张了，大家不会太在意啦。"
    # 塑造玲负责、认真
    rei "总是这样偷懒的话什么都做不到的，有好好回听今天的合奏吗？"
    mhk "有…有啦，我刚刚听完，现在正准备睡觉呢。"
    rei "哎——之前也说了很多遍了，你到底有没有认真对待啊。"
    rei "稍微…多用点心啊。"
    hide character_action mhk with dissolve
    show character_action mhk upset at pos_center with dissolve
    mhk "呜…知道了啦。"
    mhk "不过我要是想认真的话，什么东西都能学会的。\n"
    extend "除了数学、国语、物理、化学、生物、政治、地理、历史、体育……"
    rei "……"
    mhk "好梦啦，熬夜会变成漏了气的汽水的。"
    mhk "哈——好困。"
    hide character_action mhk with dissolve
    show character_action mhk normal at pos_center with dissolve
    "我躺在床上，闭上眼睛，回想着过往。"
    "真庆幸玲那家伙没有当上学生会会长，不然连音乐老师都会被迫变成她那样的人。"
    "{size=+10}！简直是世界的灾难！{/size}" with vpunch
    "不过…"
    "要真是那样的话，这个世界的音乐会变得更加动听吧。"

    # 有问题的练习
    # 爆点1：
    # 玲爆的时候假装配合演奏贝斯实际根本没出声
    # 美步子对此表示大家一直都没有贝斯可能习惯了）
    # 
    # 塑造压抑的氛围和什么东西即将爆发的感觉
    scene bg 练习室 with dissolve
    show character_action mhk normal at pos2
    show character_action rei idle at pos3
    "练习室的窗帘紧拉着，早晨炽热的阳光从窗帘的缝隙中透出，空气十分闷热。"
    "我迈着有力的步伐走向窗口，拉开窗帘，大口呼吸着新鲜空气。"
    mhk "啦啦啦，新的一天就应该从打开所有的窗帘开始，还有窗户——"
    mhk "玲——来这边一起玩呀~"
    "……"
    mhk "玲？"
    "……"
    mhk "（走近玲身后）玲——"
    rei "啊！吓我一跳！"
    mhk "玲是昨晚没睡好吗？怎么一副没精神的样子。"
    rei "别在意，我只是刚刚在想接下来的练习曲子而已。\n"
    extend "反倒是你，这么热的天开窗是想怎样？"
    rei "真是拿你没办法，接下来趁着大家还没到，我们先开始练习吧。"
    play music bgm_humor
    "吉他、贝斯和哼唱声交织着，贝斯沉下去时，吉他浮起来，哼唱在最高点微微摇晃。"
    "单独和玲演奏的这段时间让我很怀念，小的时候，如果没有玲，或许我就没有办法像现在一样和大家一起玩耍。"
    "更没有办法…"
    extend "跟随玲到达现在和更远的地方。"
    "在外人看来，演奏中的我们或许很有默契。"
    "但其实与我而言…"
    extend "练习实在是好困啊——"
    # 大家到齐，开始练习
    play sound sfx_door
    show character_action yuka smile at pos1 with dissolve
    show character_action kanna normal at pos4 with dissolve
    show character_action akr shy at pos2 with dissolve
    show character_action mhk normal at pos_center with dissolve
    yuka "玲，美步子，早上好~今天这么早来练习啊。"
    rei "早上好。"
    # 塑造团宠
    mhk "友歌——你终于来了，那我不打扰，我回去睡觉了哈。"
    yuka "等等，给我回来！"
    "揪——"
    mhk "哎呀——被抓住了，呜呜如果放我回去睡觉的话，我什么都愿意做的。"
    akr "噗…"
    # 展现神奈和玲的不融洽关系
    kanna "谁让你吃那么多甜点，自作自受。"
    hide character_action kanna with dissolve
    show character_action kanna hostile at pos4 with dissolve
    kanna "不过既然来都来了……我才不是特意要陪你们练完，只是不想被说懒罢了。"
    "练习室里啪啪的拍手声响起，大家的目光都集中在友歌身上。"
    yuka "好！大家今天都很有精神，那就先从昨天的练习曲子开始吧。"
    rei "这首曲子大家都有些小问题，特别是神奈，乐队不是一个人的事情，要感受演奏中和大家的连接。"
    kanna "哈？当初选曲子我就说了，这首曲子不适合我们。"
    rei "但这是大家共同的选择。"
    kanna "啧，都练习多少遍了，只抱着一首不放，你们不嫌腻我还嫌烦呢，要不是看在"
    yuka "神奈，别说了，大家练习开心就好，以后Jam的机会还有很多。"
    akr "…我觉得玲说的挺对的，而且昨天的曲子…我挺喜欢的。"
    "但其实我不太在意选什么曲子，只要能和大家在一起就好。"
    "……"
    "…"
    # 演奏后的暴雷
    # 美步子的没有边界感和笨蛋
    "随着最后一个音符的消失，大家都停下了手中的乐器。"
    "这次的演奏和平时不太一样，是因为大家连续几天练习的原因，精力跟不上了吗？"
    "不行，得离近些，仔细看看大家的状态。"
    rei "……"
    yuka "美步子？"
    akr "太…太近了。"
    kanna "美步子你干嘛，这样很烦啊。"
    mhk "哼哼哼~完全没有露出笑容呢，但看到大家和我一样演奏完还有余力，真是太棒了~"
    kanna "谁说我有余力了，要不是为了早点结束练习，我才懒得演奏呢。"
    akr "不过，刚刚贝斯的声音我听不太清楚，也可能是我不够专注。"
    # 玲的爆点
    "大家的目光一同朝向那个方向。"
    "玲？"
    "原本沉默的玲像下定什么决心一样，开口了。"
    rei "其实我刚刚演奏的时候，根本没有弹贝斯。"
    "大家" "什么？！"
    rei "我只是把手放在贝斯上，假装演奏而已。"
    hide character_action rei with dissolve
    show character_action rei upset at pos3 with dissolve
    play music bgm_serious

    # 爆点2：
    # 大家居然真的接受了，玲为大家不认真的态度失望，开爆，各方表达自己的观点
    # 玲认真的态度没有被大家认同甚至忽视误解，甩门离开
    # 
    # 友歌的安慰，以及反效果的忽视
    yuka "诶？！……玲，原来是这样啊。不过没关系的，我们大家都懂你的。你一定是因为太累了，或者最近心里藏着什么事情吧？"
    "我注意到玲的嘴唇微微颤抖。"
    rei "……不是。"
    yuka "不用勉强自己，也不用道歉。我们练习又不是为了成为专业乐队，重要的是大家一起开开心心的。"
    rei "不。"
    yuka "神奈想的时候练神奈喜欢的曲子，玲也是，大家都是，时间上可能安排不太好，不用给自己那么大压力啦，放松点。"
    yuka "就算你不弹贝斯，我们也一样喜欢你。笑一笑，好吗？"
    # 玲的自述和真挚的想法
    rei "{size=+10}不是这样的！{/size}" with vpunch
    rei "我一直以为……像友歌说的那样，是我太较真了，把音乐看得太重了。"
    rei "所以我试着去放松自己，试着学学偷懒，试着说服自己“像这样的生活，只要大家在一起就好”"
    rei "我甚至想过要不要放弃音乐，去做一些更轻松的事情。"
    rei "但我从来没有觉得玩乐队开心过，每次练习都在犯同样的错误，我觉得好疲惫……"
    rei "我只是想…和大家一起去武道馆办一次live，哪怕最终只能在小一些的live house演出，我也想和大家一起。"
    rei "我已经受够了，反正有没有贝斯，你们都能继续演奏，那不如一走了之！"
    play sound sfx_door
    hide rei with dissolve
    kanna "终于走了，贝斯手本就是可有可无的存在。"
    yuka "神奈！"
    akr "玲…"
    mhk "玲！"
    "周围的声音变得模糊遥远，视野变得越来越狭窄。"
    hide character_action mhk with dissolve
    show character_action mhk shocked at pos_center with dissolve
    "只要伸出手。\n"
    extend "就能把乐队重新团结起来。"
    "还差一点，就能抓住玲的手。\n"
    extend "就能给乐队带来改变。"
    "我如此坚信着…但我还是没有抓住，玲的手就这样从我手中滑落。"

    hide all with dissolve
    jump turn_talk

# 事后认真系向外向系理性阐述自己的想法，
# 大家因为梦想太宏大飘渺而浅尝辄止，
# 没有明确的方向；
# 外向系->认真系：认识到音乐的本质就是以音为乐
label turn_talk:
    # 老团还在，晶和美步子受到了玲的改变
    # 但是老团的日常回不到以前快乐的氛围，比如突然的沉思之类的
    # 美步子动机：1. 自身元气属性想让大家展露笑容 2. 觉得玲是乐队必不可缺的成员
    scene bg 公园路 with dissolve
    show character_action mhk at_a_loss at pos3
    play music bgm_peaceful
    "从那以后，大家回到了日常的练习中，但我总是心不在焉。"
    "要是大家能告诉我玲回来了就好了…"
    "期盼大家告诉我，想要挽回她的心情占据着我的内心。"
    "想要联系玲随时都行，但我始终不知道这样做的理由。"
    "时间就这样一天天流逝着。"
    play sound sfx_phone
    mhk "啊——玲！"
    "我匆忙跑去拿起手机接通电话。"
    yuka "美步子，今晚有空吗？之前那家咖啡厅还挺好的，要再去聚聚吗？"
    "像这样的电话我已经接了很多次了，但每次都不是玲。"
    "即便每次的结果相同，不知道为什么，只有模糊的感觉。"
    "我害怕那种感觉成为现实，一定要做点什么。"
    mhk "好，到时候见啦~"
    # 试图维护昔日开心随性的氛围，但总有瑕疵
    scene bg 咖啡馆 with dissolve
    show character_action yuka smile at pos1
    show character_action kanna normal at pos4
    show character_action akr normal at pos2
    show character_action mhk normal at pos3
    play music bgm_citypop_02
    yuka "美步子，这边这边~这样就都到齐了，真是太好了。"
    kanna "我先说好，我可不是因为想联系上玲才来的。"
    kanna "我只是——路过而已，这家店的抹茶蛋糕只有在这个时间段限定，给朋友带而已。"
    mhk "神奈还是老样子嘛~把心里话说出来有什么不好意思的。"
    kanna "烦死人了一边去。"
    "看来大家都还是老样子。"
    yuka "其实…昨天我和玲通了电话。"
    "我感觉心里有些不安。"
    yuka "她听起来没有什么精神，我问乐队的事，她只说了句“最近有点累”，就挂断了电话。"
    hide character_action akr with dissolve
    show character_action akr shy at pos2 with dissolve
    akr "……又是这样，上周我发消息问她要不要一起去书店，她到第二天才回我。"
    "原来大家都在小心翼翼地触碰着这个事实。"
    akr "你们觉得…玲会回来吗？"
    mhk "我觉得她会回来的，她不是那种会轻易放弃的人。"
    "没错，玲一直非常认真地对待着乐队的事。"
    "而且我也想让乐队的大家重新展露笑容。"
    "玲以前带领我走到了这里，现在我也想让玲重新回到乐队中，我们需要玲。"
    mhk "不好意思，我临时有点事，先走啦~"
    "玲就在那里，那个我们相遇的路口。"

    scene bg 公园路 with dissolve
    show character_action mhk normal at pos2
    show character_action rei idle at pos3
    play music bgm_serious
    # 玲和美步子谈心，了解到各自所需，打开心结
    mhk "玲——你果然还是在这里啊。"
    rei "美步子…你来了啊。是打算说服我回去乐队吗？"
    mhk "……"
    rei "我已经…没有理由回去了，我不是能把演奏音乐视为玩乐的人。"
    mhk "但你之前把我从这里带了出来，带我去参加其他乐队的live，当时真的很开心。"
    mhk "是你让我知道了……音乐的本质就是以音为乐。"
    rei "啊……以音为乐吗……"
    mhk "是啊，玲，这句话可是你告诉我的哦~当时live结束后，你还捏了我的脸颊说“像这样笑出来，就是音乐的魅力”"
    rei "……你说得对，那句话确实是我说的。可是——你知道我为什么会累吗？"
    "我愣住了，玲的眼神中闪过一丝我从未见过的感情。"
    hide character_action rei with dissolve
    show character_action rei upset at pos3 with dissolve
    rei "不是因为大家忽视我的想法，也不是因为练习量太大，而是因为我觉得大家都没有勇气。"
    rei "梦想除了想成为的样子，还要有自己的样子。"
    rei "只有抛下了锚，才能扬帆起航。"
    "……"
    "…"
    "还有说不玩的未说出口的话，以及重要的话。但我们已经理解了彼此。"
    hide character_action rei with dissolve
    show character_action rei idle at pos3 with dissolve
    hide character_action mhk with dissolve
    show character_action mhk smile at pos2 with dissolve
    play music bgm_hope
    mhk "对了，下个月就是校园文化祭了，我们一起去吧。"
    rei "……你真是，一点都没变。"
    hide all with dissolve
    jump turn_roadshow

# 解决方式：一场不期而遇的路演live（美步子分别邀请玲和其余三人，但不告诉互相要去）
# 让认真系明白音乐能带来快乐
# 让原成员看到实现梦想的希望
# 校园文化祭
label turn_roadshow:
    
    # 校园文化祭当天，美步子的千层套路
    # 主打一个坑蒙拐骗（划掉）把大家强行凑齐
    scene bg 商店 with dissolve
    show character_action mhk excited at pos3
    play sound sfx_crowd
    play music bgm_humor
    "章鱼小丸子！炒面！还有超大的棉花糖！"
    "呜哇，文化祭简直就是天堂！不过今天我可不是来单纯干饭的。"
    "我看了看手表，时间差不多了。猎物们……啊不，亲爱的伙伴们应该快到了吧？"

    if debug:
        "（不远处，神奈、友歌和晶走了过来）"
    show character_action yuka smile at pos1 with dissolve
    show character_action kanna normal at pos4 with dissolve
    show character_action akr shy at pos2 with dissolve
    yuka "美步子——这里这里！"
    kanna "真是的，大热天非要把人叫出来，要是没有好吃的限定甜点我绝对饶不了你。"
    akr "那个……文化祭的人真的好多啊……有点挤。"
    mhk "嘿嘿，放心吧！保证让你们今天终生难忘！"

    "就在这时，一个熟悉的身影出现在了约定的喷泉广场前。"
    if debug:
        "（玲登场，大家面面相觑）"
    show character_action rei idle at pos3 with dissolve
    rei "美步子，我到了。你说有很重要的东西要给我看……"
    rei "诶？"
    yuka "啊，是玲！"
    kanna "哈？你这家伙不是退……不是不玩了吗，怎么会在这里？"
    akr "玲……太好了。"

    # 众人懵逼，美步子开始强行带节奏
    rei "美步子，这是怎么回事？你不是说只有我们两个……"
    mhk "当当当当！惊不惊喜，意不意外？这就是我说的‘超绝重要大作战’！"
    kanna "我就知道你这家伙没安好心！早知道我就在家里吹空调了！"
    yuka "好啦好啦神奈，既然大家都碰面了，这不是挺好的嘛。"

    # 转移注意力，切入正题
    "我指向广场中央。那里搭着一个临时的路演舞台，上面放着几把吉他、一台架子鼓、键盘，还有一把孤零零的贝斯。"
    "旁边立着一块巨大的牌子：【自由舞台！任何人都可以上来Jam一曲！】"
    mhk "大好机会！冲啊！"
    rei "等等，你想干什么？！"
    mhk "上台啊！来都来了，不玩一把再走岂不是血亏！"
    kanna "你疯了吧？！几个月都没合练过了，上去丢人吗！"
    mhk "不怕不怕！我们不是有玲嘛！"
    "我一把抓住玲的手腕，另一只手拽住友歌，像火箭一样往舞台方向冲。"
    rei "喂！放手！我说了我已经……"
    mhk "不管不管！王牌贝斯手不发威，别人还以为我们是搞笑艺人呢！"

    # 爆点3：美步子一转攻势，赶鸭子上架
    scene bg 舞台 with dissolve
    show character_action yuka normal at stage_leftmost
    show character_action akr timid at stage_left
    show character_action mhk excited at stage_center
    show character_action rei idle at stage_right
    show character_action kanna normal at stage_rightmost
    "台下不知什么时候已经围了一圈人，好奇地打量着我们这群看起来像是被临时绑架上台的倒霉蛋。"
    kanna "啧……烦死了，看什么看啊！"
    "神奈虽然嘴上抱怨着，但身体还是很诚实地背起了吉他，顺手拨了个极具攻击性的和弦。"
    akr "那、那个……我会尽力的……"
    "晶小跑着站到了键盘位前，深吸了一口气。"
    yuka "哈哈，感觉心跳好快啊，既然推不掉，那就只能硬上了呢。"

    "大家不约而同地看向玲。"
    "玲站在贝斯前，手指悬在半空，平时那种冷酷认真的样子全不见了，看起来甚至有点不知所措。"
    rei "我……我不行的。没有排练过，不知道该弹什么，而且……"
    mhk "那就随便弹！弹你现在最想弹的音！"
    mhk "玲！音乐的本质，就是以音为乐啊！"
    "我冲她眨了眨眼，一把抓过麦克风，顺手猛地扫响了胸前的吉他。"
    "友歌心领神会，鼓棒高高扬起，重重落下！"
    "一、二、三、走起！"

    # 演奏开始，情绪释放
    play music bgm_live
    "没有预先定好的曲目，也没有完美的配合。神奈随手弹了一段失真riff，晶紧随其后加入了清亮的键盘音。"
    "友歌在后面凭着直觉猛砸架子鼓，完全把什么节拍器抛在了脑后。"
    "而我？我当然是扯开嗓子，就着粗糙的吉他扫弦大声唱出心里最想唱的旋律！"
    "乱七八糟的！"
    "但也……超级痛快！"
    hide character_action mhk with dissolve
    show character_action mhk foolish_laugh at stage_center with dissolve

    "就在这时，那个低沉、稳健，却又充满力量的声音加入了进来。"
    "是玲的贝斯。"
    "像是一只有力的手，瞬间把我们原本散乱的音符稳稳托住，串联成了一首粗糙却充满生命力的乐章。"
    "我抬起头，看到了玲的侧脸。"
    "她的眉头一开始紧紧皱着，但随着手指在琴弦上不断跳动，那股紧绷感慢慢化解开了。"
    "台下的观众开始跟着节奏拍手，有人甚至吹起了口哨。"

    # 原成员的感悟：梦想不是轻飘飘的空话
    "对于神奈、友歌和晶来说，这一刻，她们大概终于明白了玲口中的‘武道馆’并不只是个虚无缥缈的梦。"
    "当音乐真正传递到别人耳朵里，当台下的目光和欢呼声汇聚在我们身上时……那种灵魂共振的战栗感，是骗不了人的。"

    # 玲的释怀：音乐真的是用来快乐的
    "而对于玲……"
    "一曲终了，最后一个和弦在空气中缓缓消散。"
    "台下爆发出热烈的掌声和欢呼。"
    play sound sfx_crowd
    rei "呼……"
    "玲大口喘着气，胸口微微起伏。她愣愣地看着台下的人群，又转头看了看我们。"
    "随后，一个极其微小，却又无比耀眼的笑容，在她嘴角绽放开来。"
    rei "真是……被你们打败了。"
    rei "弹得简直一塌糊涂，神奈你进早了两拍，友歌你的鼓全靠力气大是吧？"
    rei "还有美步子，你后面高音全靠吼就算了，吉他也差点跑调！"
    kanna "哈？！你有什么资格说我，你中间不也弹错了一个音！"
    mhk "嘿嘿嘿，不管怎样，好爽啊！"
    yuka "嗯！大家能像这样一起演奏，真的是太棒了！"
    akr "下次……我们再一起弹吧。"
    hide character_action mhk with dissolve
    show character_action mhk smile at stage_center with dissolve
    hide character_action yuka with dissolve
    show character_action yuka smile at stage_leftmost with dissolve
    hide character_action akr with dissolve
    show character_action akr smile at stage_left with dissolve
    play music bgm_hope

    # 彻底和解，回到正轨（但是是地狱难度）
    rei "……"
    rei "没办法。既然你们这么需要我，那我就勉为其难，再陪你们胡闹一阵子吧。"
    rei "不过事先说好，从明天开始，地狱级特训要重新启动了。不想掉队的，就给我咬紧牙关跟上。"
    hide character_action mhk with dissolve
    show character_action mhk upset at stage_center with dissolve
    mhk "诶——？！刚和好就要特训？救命啊——"
    hide character_action mhk with dissolve
    show character_action mhk smile at stage_center with dissolve
    "虽然嘴上喊着救命，但我的心里却像是喝了冰镇汽水一样畅快。"
    "我们的锚，终于抛下了。"
    "接下来……就是要扬帆起航了！"

    stop music fadeout 3.0
    hide all with dissolve
    return
