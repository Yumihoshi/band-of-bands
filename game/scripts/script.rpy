label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    show eileen happy

    # 此处显示各行对话。

    akr "播放音乐。"
    play music "bgm/bgm_humor.ogg" fadein 2.0
    # 此处为游戏结尾。
    akr "好听。"
    menu:
        "接下来要测试的章节"

        "日常1":
            jump daily_01
    

    stop music fadeout 1.0

    return
