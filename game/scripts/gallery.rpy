# ==============================================================================
# 画廊系统
# 展示游戏中使用到的背景和角色立绘
# ==============================================================================

init python:
    # 背景画廊列表
    gallery_bg_list = [
        ("bg 商店", "商店"),
        ("bg 书店", "书店"),
        ("bg 卧室", "卧室"),
        ("bg 学校走廊", "学校走廊"),
        ("bg 咖啡馆", "咖啡馆"),
        ("bg 桌椅1", "桌椅1"),
        ("bg 桌椅2", "桌椅2"),
        ("bg 桌椅3", "桌椅3"),
        ("bg 公园路", "公园路"),
        ("bg 河边", "河边"),
        ("bg 舞台", "舞台"),
        ("bg 练习室", "练习室"),
        ("bg 音乐商店", "音乐商店"),
        ("bg 商场", "商场"),
        ("bg 教室", "教室"),
        ("bg 排练室", "排练室"),
    ]
    
    # 角色立绘画廊列表
    gallery_char_list = [
        ("mhk normal", "美步子·通常"),
        ("mhk excited", "美步子·兴奋"),
        ("mhk shocked", "美步子·震惊"),
        ("mhk upset", "美步子·沮丧"),
        ("mhk smile", "美步子·微笑"),
        ("mhk angry", "美步子·生气"),
        ("mhk at_a_loss", "美步子·茫然"),
        ("mhk foolish_laugh", "美步子·傻笑"),
        ("mhk action_01", "美步子·动作"),
        ("rei normal", "玲·通常"),
        ("rei idle", "玲·待机"),
        ("rei upset", "玲·沮丧"),
        ("rei worry", "玲·担忧"),
        ("rei smile", "玲·微笑"),
        ("yuka normal", "友歌·通常"),
        ("yuka smile", "友歌·微笑"),
        ("yuka gentle", "友歌·温柔"),
        ("kanna normal", "神奈·通常"),
        ("kanna hostile", "神奈·敌意"),
        ("kanna tsundere", "神奈·傲娇"),
        ("akr normal", "晶·通常"),
        ("akr shy", "晶·害羞"),
        ("akr smile", "晶·微笑"),
        ("akr timid", "晶·胆怯"),
    ]


# 画廊主菜单
screen gallery():
    tag menu
    
    use game_menu(_("画廊"), scroll="viewport"):
        
        vbox:
            xalign 0.5
            spacing 30
            
            text _("选择要浏览的画廊"):
                size 28
                xalign 0.5
            
            textbutton _("背景画廊"):
                xalign 0.5
                action ShowMenu("gallery_bg")
                text_size 24
            
            textbutton _("角色画廊"):
                xalign 0.5
                action ShowMenu("gallery_char")
                text_size 24


# 背景画廊
screen gallery_bg():
    tag menu
    
    use game_menu(_("背景画廊"), scroll="viewport"):
        
        grid 4 4:
            spacing 15
            xalign 0.5
            
            for img, name in gallery_bg_list:
                
                button:
                    xsize 280
                    ysize 158
                    
                    action Show("gallery_view", gallery_img=img, gallery_title=name, is_char=False)
                    
                    add img:
                        xsize 280
                        ysize 158
                        fit "cover"
                    
                    text name:
                        align (0.5, 1.0)
                        yoffset -5
                        size 16
                        color "#ffffff"
                        outlines [(2, "#000000", 0, 0)]


# 角色画廊
screen gallery_char():
    tag menu
    
    use game_menu(_("角色画廊"), scroll="viewport"):
        
        grid 4 6:
            spacing 15
            xalign 0.5
            
            for img, name in gallery_char_list:
                
                button:
                    xsize 140
                    ysize 280
                    
                    action Show("gallery_view", gallery_img=img, gallery_title=name, is_char=True)
                    
                    add img:
                        xsize 140
                        ysize 280
                        fit "cover"
                    
                    text name:
                        align (0.5, 1.0)
                        yoffset -5
                        size 14
                        color "#ffffff"
                        outlines [(2, "#000000", 0, 0)]


# 全屏查看
screen gallery_view(gallery_img, gallery_title, is_char=False):
    
    # 点击图片任意位置关闭预览
    button:
        xfill True
        yfill True
        
        action Hide("gallery_view")
        
        if is_char:
            add "#ffffff"
        
        add gallery_img:
            xalign 0.5 yalign 0.5
            fit "contain"
    
    # 顶部返回按钮
    frame:
        style_prefix "gallery_top"
        align (0.0, 0.0)
        xpadding 20
        ypadding 10
        
        hbox:
            spacing 20
            
            textbutton _("← 返回"):
                action Hide("gallery_view")
                text_size 22
            
            text gallery_title:
                size 22
                color "#ffffff"
                outlines [(2, "#000000", 0, 0)]
                yalign 0.5


style gallery_top_frame is empty
style gallery_top_frame:
    background "#00000088"
