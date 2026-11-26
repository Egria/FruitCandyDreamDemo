# 这里是唯一需要编辑的剧本，按游玩顺序排列。
label start:
    $ renpy.music.set_volume(1.0, channel="music")

    # 扉页
    $ page_lines = ()
    $ page_number = 1
    $ page_split = 1
    scene bg page_01 at fit_background
    with dissolve
    play music "audio/bgm/01_yellowed_pages.ogg" loop
    call page_line("很久很久以前") from page_return_book_01_01

    # 王国
    $ page_lines = ()
    $ page_number = 2
    $ page_split = 2
    scene bg page_02 at fit_background
    play sound "audio/sfx/page_turn.ogg"
    with turn_page
    call page_line("在一个遥远的王国") from page_return_book_02_01
    call page_line("有一个聪明又善良的公主") from page_return_book_02_02
    call page_line("她掌握着强大的魔法") from page_return_book_02_03
    call page_line("她用魔法帮助着人们") from page_return_book_02_04

    # 来客
    $ page_lines = ()
    $ page_number = 3
    $ page_split = 2
    scene bg page_03 at fit_background
    play sound "audio/sfx/page_turn.ogg"
    with turn_page
    call page_line("有一天，一位帅气的王子来到了公主的城堡") from page_return_book_03_01
    call page_line("王子说，自己在旅行途中弄丢了珍贵的宝石") from page_return_book_03_02
    call page_line("希望借助公主的魔力找回宝石") from page_return_book_03_03
    call page_line("公主很高兴自己的魔力能帮助别人") from page_return_book_03_04

    # 森林
    $ page_lines = ()
    $ page_number = 4
    $ page_split = 2
    scene bg page_04 at fit_background
    play sound "audio/sfx/page_turn.ogg"
    with turn_page
    call page_line("公主和王子一道") from page_return_book_04_01
    call page_line("循着宝石的踪迹") from page_return_book_04_02
    call page_line("来到了黑暗森林之中") from page_return_book_04_03

    # 古堡
    $ page_lines = ()
    $ page_number = 5
    $ page_split = 1
    scene bg page_05 at fit_background
    play sound "audio/sfx/page_turn.ogg"
    with turn_page
    call page_line("在黑暗森林的中心有一座古堡") from page_return_book_05_01
    call page_line("从远处就能看到塔顶上的宝石熠熠生辉") from page_return_book_05_02

    # 封印
    $ page_lines = ()
    $ page_number = 6
    $ page_split = 2
    scene bg page_06 at fit_background
    play sound "audio/sfx/page_turn.ogg"
    with turn_page
    call page_line("可当两人来到塔顶时") from page_return_book_06_01
    call page_line("发现宝石被黑暗的魔法封印在了台座上") from page_return_book_06_02
    call page_line("“我没有魔力，所以无法解开封印。”") from page_return_book_06_03
    call page_line("“你能帮我解开宝石的封印吗？”") from page_return_book_06_04

    # 红光
    $ page_lines = ()
    $ page_number = 7
    $ page_split = 3
    scene bg page_07 at fit_background
    play sound "audio/sfx/page_turn.ogg"
    with turn_page
    call page_line("公主欣然应允") from page_return_book_07_01
    call page_line("伸出手解开了宝石的封印") from page_return_book_07_02
    show bg page_07b at fit_background with Dissolve(0.25)
    call page_line("可就在这时，宝石突然亮起了不祥的红光") from page_return_book_07_03
    show bg page_07c at fit_background with Dissolve(0.25)
    call page_line("数道黑烟组成的锁链瞬间缠住了公主") from page_return_book_07_04
    call page_line("她感到自己的魔力被源源不断地吸走") from page_return_book_07_05

    # 锁门
    $ page_lines = ()
    $ page_number = 8
    $ page_split = 3
    scene bg page_08 at fit_background
    play sound "audio/sfx/page_turn.ogg"
    with turn_page
    call page_line("王子露出邪恶的笑容，对公主说") from page_return_book_08_01
    call page_line("“这样，你的魔力就全都是我的了。”") from page_return_book_08_02
    play sound "audio/sfx/door_lock.ogg"
    call page_line("他把塔顶的门反锁起来，大笑着离开了") from page_return_book_08_03
    call page_line("“等等……你的宝石！”") from page_return_book_08_04
    call page_line("门外的脚步声越来越远") from page_return_book_08_05

    # 塔中
    $ page_lines = ()
    $ page_number = 9
    $ page_split = 3
    scene bg page_09 at fit_background
    play sound "audio/sfx/page_turn.ogg"
    with turn_page
    call page_line("公主无力地昏倒在地上") from page_return_book_09_01
    call page_line("不知过了多久，她才从昏迷中醒来") from page_return_book_09_02
    call page_line("她想要出去，门却怎么也打不开") from page_return_book_09_03
    call page_line("想要使用魔法，却连一点魔力都没有了") from page_return_book_09_04
    call page_line("她又冷又饿，靠着门，孤独地啜泣") from page_return_book_09_05

    # 窗外
    $ page_lines = ()
    $ page_number = 10
    $ page_split = 2
    scene bg page_10 at fit_background
    play sound "audio/sfx/page_turn.ogg"
    with turn_page
    call page_line("不知过了多少个白天和黑夜") from page_return_book_10_01
    show bg page_10b at fit_background with Dissolve(0.25)
    call page_line("终于有一天，她下定了决心") from page_return_book_10_02
    call page_line("她迎着塔顶窗外一望无际的蓝天") from page_return_book_10_03
    call page_line("一跃而下") from page_return_book_10_04

    # 落地
    $ page_lines = ()
    $ page_number = 11
    $ page_split = 3
    scene bg page_11 at fit_background
    play sound "audio/sfx/page_turn.ogg"
    with turn_page
    call page_line("她折断了一条腿") from page_return_book_11_01
    call page_line("和两根肋骨") from page_return_book_11_02
    call page_line("她爬着") from page_return_book_11_03
    call page_line("扶着树，摇摇晃晃地站起来") from page_return_book_11_04
    call page_line("又单脚跳着，往前走了几步") from page_return_book_11_05

    # 启程
    $ page_lines = ()
    $ page_number = 12
    $ page_split = 3
    scene bg page_12 at fit_background
    play sound "audio/sfx/page_turn.ogg"
    with turn_page
    call page_line("她暗暗下了决心") from page_return_book_12_01
    call page_line("她要找回自己的魔法") from page_return_book_12_02
    call page_line("为此，她第一次拿起了武器") from page_return_book_12_03
    call page_line("即使一点魔力都没有了") from page_return_book_12_04
    call page_line("她也要靠自己的力量") from page_return_book_12_05
    call page_line("踏上未知的旅程") from page_return_book_12_06

    # 合上的书
    scene bg page_13 at fit_background
    with dissolve
    play sound "audio/sfx/book_close.ogg"
    stop music fadeout 0.65
    "嗯？这就结束了吗？"
    "这个故事好像没有写完的样子。"
    "不过，好像是个有点俗套的故事。"
    "……所以，她后来把魔法找回来了吗？"

    # 黑暗中的声音
    scene bg dream_01 at fit_background
    with dissolve
    voice "voice/pineapple/meet_01.ogg"
    pine_unknown "总算遇到你了。"
    play music "audio/bgm/02_finally_found_you.ogg" fadein 1.1 loop
    voice "voice/pineapple/meet_02.ogg"
    pine_unknown "我找你很久了。"
    menu:
        "你在找我吗？":
            pass
    voice "voice/pineapple/meet_04.ogg"
    pine_unknown "现在有一件只有你能做到的事。"
    voice "voice/pineapple/meet_05.ogg"
    pine_unknown "你愿意帮助我吗？"
    menu:
        "你是谁？":
            pass

    # 菠萝的请求
    show person_pine shadow at standing(0.5, -78)
    with dissolve
    voice "voice/pineapple/ask_01.ogg"
    pine_unknown "我是……你对我来说，是个很重要的人。"
    menu:
        "重要的人？":
            pass
    voice "voice/pineapple/ask_03.ogg"
    pine_unknown "你很快就会知道了。"
    voice "voice/pineapple/ask_04.ogg"
    pine_unknown "我找了很长时间，终于见到了你——拥有魔力的人。"
    menu:
        "我？我拥有魔力吗？":
            pass
    voice "voice/pineapple/ask_06.ogg"
    pine_unknown "有人弄丢了重要的东西，那是只有你能找到的东西。"
    voice "voice/pineapple/ask_07.ogg"
    pine_unknown "我希望你能帮帮我。"
    menu:
        "我要怎么帮你呢？":
            jump help_a
        "为什么我要帮你呢？":
            jump help_b

label help_a:
    # 询问如何帮忙
    voice "voice/pineapple/help_a_01.ogg"
    pine_unknown "那件东西谁都看不见。但是你拥有魔力，应该可以看见。"
    voice "voice/pineapple/help_a_02.ogg"
    pine_unknown "等你看见了，应该就知道怎么做了。"
    menu:
        "我知道了。如果我看见了，我就帮你。":
            pass
    jump fog_start

label help_b:
    # 询问缘由
    voice "voice/pineapple/help_b_01.ogg"
    pine_unknown "请把它当作我的请求。我愿意为此付出一切代价。"
    voice "voice/pineapple/help_b_02.ogg"
    pine_unknown "因为我确信，你是唯一能帮到我的人了。"
    menu:
        "……我可以先帮你找找看。":
            pass
    jump fog_start

label fog_start:
    # 梦境消散
    hide person_pine
    with dissolve
    "诶？怎么消失了？刚才那是幻觉吗？"

    # 雾
    scene bg dream_02 at fit_background
    with dissolve
    "怎么什么都看不见了？这是起雾了吗？我在哪里呢？"
    "刚才是谁在和我说话？"
    "我好像要帮谁一个忙来着？可是怎么什么也想不起来了？"

    # 醒来
    scene bg dream_03 at fit_background
    with dissolve
    stop music fadeout 0.3
    voice "voice/mandarin/wake_01.ogg"
    mandarin_unknown "喂，醒醒！醒醒！你睡着了吗！"

    # 卧室桌边
    scene bg home_01 at fit_background
    with dissolve
    voice "voice/mandarin/desk_01.ogg"
    mandarin_unknown "姐，你怎么趴着就睡着了？是不是太累了？"

    # 卧室
    scene bg home_02 at fit_background
    show person_mandarin normal at standing(0.5, -163)
    with dissolve
    citrus "啊，蜜柑，真抱歉。我也不知道怎么就睡着了。"
    play music "audio/bgm/03_homework_tomorrow.ogg" fadein 0.8 loop
    voice "voice/mango/bed_02.ogg"
    mango_unknown "柚子！你干什么去了？拿水杯要这么久吗？"
    voice "voice/mandarin/bed_03.ogg"
    mandarin "大家发现你突然不见了，好像你说过要拿水杯，就派我来看看。"
    citrus "好，我马上过来！抱歉！"
    voice "voice/mandarin/bed_05.ogg"
    mandarin "下回可别这样了！哪有人早上五点起床给同学准备大餐的？"
    citrus "这不是他们要来家里赶作业嘛？"
    voice "voice/mandarin/bed_07.ogg"
    mandarin "行了行了，赶紧把这群闹腾的男生弄走吧。"

    # 客厅
    scene bg home_03 at fit_background
    show person_lemon normal at standing(0.16, -120)
    with dissolve
    voice "voice/lemon/living1_01.ogg"
    lemon_unknown "柚子，你是不是在里面睡着了？"

    # 苹果
    show person_apple normal at standing(0.385, -77)
    with dissolve
    voice "voice/apple/living2_01.ogg"
    apple_unknown "我带这两个家伙走吧，柚子。没事，今天玩得很开心。你得早点休息了。"
    citrus "诶嘿，也没有啦。我不累呢。"
    "这个男生是苹果，是我的同班同学，也是最好的朋友之一。"
    "至于这个……他是柠檬。是我的弟弟，和蜜柑是双胞胎，都比我小两岁。对，他也是男生。"

    # 牌局
    show person_mango normal at standing(0.635, -95)
    with dissolve
    voice "voice/mango/cards_01.ogg"
    mango_unknown "打着打着牌居然还能少个人，你真厉害！"
    citrus "喂，你说什么呢！我不是让柠檬代打了么。"
    voice "voice/mango/cards_03.ogg"
    mango_unknown "你自己问问你家柠檬都是怎么打牌的。东看看西看看，也不怕脖子扭断。"
    voice "voice/lemon/cards_04.ogg"
    lemon "去去去，打牌打不过就说人作弊。而且就算我看了，也是你自己没藏好的错。"
    "这个说话阴阳怪气的男生是芒果，也是我的同班同学和最好的朋友之一。"
    citrus "诶嘿。"
    voice "voice/lemon/cards_07.ogg"
    lemon "柚子你在笑我吗？你看他说话这么过分，你还笑我。"
    voice "voice/mango/cards_08.ogg"
    mango "只有干了坏事心虚的人才会觉得别人笑都是在笑自己。"
    voice "voice/apple/cards_09.ogg"
    apple "行了你们有完没完？都几点了？是不是该回家了啊？"
    citrus "我在笑……你们真的很可爱。"
    citrus "和你们在一起我好幸福啊。"
    voice "voice/mango/cards_12.ogg"
    mango "柚子，你脑子烧坏了吗？怎么开始说胡话了？"
    voice "voice/apple/cards_13.ogg"
    apple "行了行了，别嘴欠了，柚子肯定也累了。菠萝，收拾东西准备走吧。"
    voice "voice/pineapple/cards_14.ogg"
    pine_unknown "哦，好。走吧，柚子，不用送了。"

    # 认出菠萝
    show person_pine normal at standing(0.85, -78)
    with dissolve
    citrus_surprised "……"
    voice "voice/pineapple/recognize_02.ogg"
    pine_unknown "你瞪着我干什么？"
    voice "voice/mango/recognize_03.ogg"
    mango "喂喂，他有那么帅吗，你看我，看我。"
    citrus "……菠萝……"
    voice "voice/pineapple/recognize_05.ogg"
    pine "嗯？什么事？"
    citrus "哦哦没什么。就想问问你今天玩得开心吗？"
    "他……是菠萝，是我在班里的同桌。我们和苹果、芒果一直在一起玩。"
    show person_pine blush at standing(0.85, -78)
    voice "voice/pineapple/recognize_08.ogg"
    pine_blush "你这么问，想让我怎么回答嘛。"
    voice "voice/apple/recognize_09.ogg"
    apple "行了行了，今天说要一起赶作业，结果玩了一整天游戏和扑克牌，赶紧回家补吧。"
    voice "voice/apple/recognize_10.ogg"
    apple "明天别开学第一天就留堂补作业了。"
    voice "voice/mango/recognize_11.ogg"
    mango "走了走了，开学见。"

    # 苹果道别
    hide person_mango
    show person_pine normal at standing(0.85, -78)
    with dissolve
    voice "voice/apple/bye_apple_01.ogg"
    apple "柚子，你也早点休息，就别送我们了。再见哦，有什么想说的话随时可以给我发消息！"
    citrus "嗯嗯！到家给我发个消息！"

    # 菠萝道别
    hide person_apple
    with dissolve
    voice "voice/pineapple/bye_pine_01.ogg"
    pine "那我也走了。"
    citrus "菠萝……"
    voice "voice/pineapple/bye_pine_03.ogg"
    pine "有什么事吗，柚子？"
    citrus "嗯嗯，没事。菠萝，有不会的题目给我发消息哦。"
    voice "voice/pineapple/bye_pine_05.ogg"
    pine "嗯，我明天到学校再问你吧，你今晚早点睡。……还有，今天我玩得很开心。"

    # 姐弟妹
    hide person_pine
    show person_mandarin normal at standing(0.85, -163)
    with dissolve
    $ renpy.music.set_volume(0.65, delay=1.3, channel="music")
    voice "voice/mandarin/siblings_01.ogg"
    mandarin "姐，我给他们送到地铁站吧，你先洗澡吧。外面的烂摊子我和柠檬收拾就行了。"
    voice "voice/lemon/siblings_02.ogg"
    lemon "蜜柑你快去快回哦。"
    citrus "你们也要早点休息，明天你们也要开学的。"
    voice "voice/mandarin/siblings_04.ogg"
    mandarin "行，你别管我啦。"

    # 柠檬和柚子
    hide person_mandarin
    with dissolve
    voice "voice/lemon/lemon_01.ogg"
    lemon "柚子，你又做不好的梦了吗？"
    voice "voice/lemon/lemon_02.ogg"
    lemon "做不好的梦的话，跟我说说会不会好一点。"
    citrus "好像也算不上不好的梦……不过很奇怪，我一点都不记得梦到什么了。"
    voice "voice/lemon/lemon_04.ogg"
    lemon "嗯……那倒不太常见诶。不过应该没什么事，放宽心。想说的时候再跟我说吧。"
    citrus "好的，谢谢你柠檬。那我就先去洗澡了哦。"
    voice "voice/lemon/lemon_06.ogg"
    lemon "OK，我把客厅收拾收拾，等蜜柑回来再和她一起跟你打个招呼。"
    citrus "嗯嗯！"

    # 夜晚
    scene bg home_04 at fit_background
    with dissolve
    "呼……好忙碌的一天，说是要一起赶作业，结果就是做饭、吃饭、打游戏和打牌。"
    "不知不觉都这么晚了。"
    stop music fadeout 2
    "明天就要开学了。……早知道，今天应该真的写点作业的。"
    scene black with fade
    return
