init -2 python:
    gui.init(1280, 720)

define config.name = "Fruit Candy Dream · 序幕"
define config.version = "0.1"
define config.save_directory = "FruitCandyDream-Prologue-Demo-01"
define config.window = "hide"
define config.window_title = "Fruit Candy Dream · 序幕"
define config.game_menu_action = ShowMenu("pause_menu")
define config.default_text_cps = 40
define config.default_music_volume = 0.55
define config.default_sfx_volume = 0.65
define gui.text_font = "fonts/NotoSerifCJKsc-Regular.otf"
define gui.interface_text_font = "fonts/NotoSerifCJKsc-Regular.otf"
define gui.system_font = "fonts/NotoSerifCJKsc-Regular.otf"

style default:
    font "fonts/NotoSerifCJKsc-Regular.otf"
    language "japanese-normal"

transform fit_background:
    xysize (1280, 720)

transform standing(horizontal, top):
    zoom 0.92
    xpos horizontal
    xanchor 0.5
    ypos top

# 旧页的右半边向书脊收拢，新页的左半边再从书脊展开。
transform fold_right:
    xpos 640
    xzoom 1.0
    easein 0.19 xzoom 0.001
    alpha 0.0

transform unfold_left:
    xpos 640
    xanchor 1.0
    xzoom 0.001
    pause 0.19
    easeout 0.23 xzoom 1.0

transform turn_page(*, old_widget=None, new_widget=None):
    delay 0.42
    events False
    Fixed(new_widget, Crop((0, 0, 640, 720), old_widget), fold_right(Crop((640, 0, 640, 720), old_widget)), unfold_left(Crop((0, 0, 640, 720), new_widget)))
    pause 0.42
    new_widget
    events True

default page_number = 1
default page_lines = ()
default page_split = 1

# 每次点击添加一句；已经显现的行保留到下一页。
label page_line(line):
    ink "[line!q]"
    $ page_lines = page_lines + (line,)
    return

init python:
    def book_position(page, index, split):
        if page == 1:
            return (142, 298)
        if page == 6:  # 插图只占左上方，文字从右页上方开始。
            return (700, 105 + 98 * index)
        top = 387 if page in (2, 5, 7, 9, 12) else 72
        column = index >= split
        row = index - split if column else index
        return (705 if column else 86, top + 91 * row)

style book_print is default:
    color "#422d20"
    size 26
    line_spacing 4
    xmaximum 487

screen book_say(who, what):
    for i, line in enumerate(page_lines):
        text line style "book_print" pos book_position(page_number, i, page_split) substitute False
    text what id "what" style "book_print" pos book_position(page_number, len(page_lines), page_split)

screen say(who, what, portrait=None):
    window:
        id "window"
        background Solid("#241f2cf2")
        xysize (1176, 176)
        align (0.5, 0.965)
        padding (29, 17)
        hbox:
            spacing 23
            if portrait:
                add portrait xysize (136, 136) yalign 0.5
            vbox:
                spacing 5
                xsize (940 if portrait else 1110)
                if who:
                    text who id "who" size 25 color "#ffc8b0"
                text what id "what" size 27 color "#fff7ee" line_spacing 5

style demo_button is button:
    background Solid("#fff8e9f4")
    hover_background Solid("#ffe1bfff")
    padding (28, 10)
    xminimum 205
style demo_button_text is button_text:
    color "#443023"
    hover_color "#7b382b"
    insensitive_color "#857d76"
    size 24
    xalign 0.5

screen choice(items):
    modal True
    vbox:
        align (0.5, 0.47)
        spacing 14
        for item in items:
            textbutton item.caption action item.action style "demo_button" xalign 0.5

screen main_menu():
    tag menu
    add "bg page_12" at fit_background
    vbox:
        xpos 102
        ypos 421
        spacing 6
        text "Fruit Candy Dream" size 39 color "#483024"
        text "序幕" size 32 color "#684735"
    vbox:
        xpos 799
        ypos 402
        spacing 9
        textbutton "开始序幕" action Start() style "demo_button"
        if FileLoadable(1, page="1"):
            textbutton "读取存档" action FileLoad(1, page="1", confirm=False) style "demo_button"
        textbutton "退出" action Quit(confirm=False) style "demo_button"

screen pause_menu():
    tag menu
    modal True
    add Solid("#211c28e8")
    vbox:
        align (0.5, 0.5)
        spacing 11
        textbutton "继续阅读" action Return() style "demo_button"
        textbutton "保存进度" action [FileSave(1, page="1", confirm=False), Return()] style "demo_button"
        if FileLoadable(1, page="1"):
            textbutton "读取存档" action FileLoad(1, page="1", confirm=False) style "demo_button"
        textbutton "回到标题" action MainMenu(confirm=False) style "demo_button"
    key "game_menu" action Return()
