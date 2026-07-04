label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    show eileen happy

    # 此处显示各行对话。

    c_new_people "您好，我是乐队新人。是来加入这个乐队的。"

    c_player "我是新人邀请人。欢迎加入乐队！你都会些什么呢？"

    c_new_people "诶嘿~我什么都不会~"

    # 此处为游戏结尾。

    return
