Fruit Candy Dream · 序幕
Ren’Py 源码项目 | 1280 × 720 | 测试版本 8.4.1

启动
1. 安装并打开 Ren’Py SDK。在 Launcher 的 Preferences（偏好设置）里查看或选择 Projects Directory（项目目录）。
2. 将整个 FruitCandyDreamDemo 文件夹放入该目录。放好后，目录层级应为「项目目录 / FruitCandyDreamDemo / game / script.rpy」。
3. 回到 Launcher，刷新项目列表，选中 FruitCandyDreamDemo，点击 Launch Project（启动项目）。在书页上选择「开始序幕」。

操作
左键或空格推进一句，滚轮向上回看。选项用鼠标点击。Esc 或右键打开暂停菜单。「保存进度」使用单个存档位，再次保存会覆盖。序幕读完后回到标题。

第一次改剧本
打开 game/script.rpy，在 label start 下找到第一句「很久很久以前」，只修改引号中的文字，保存。重新启动项目并点「开始序幕」，第一页就会显示你的改动。
一般对白直接写角色和台词，例如 citrus "我马上过来！"。没有角色名的引号是旁白。想给某句配音，就在它的上一行写 voice "voice/pineapple/meet_01.ogg"。保留原有音频的台词，改字后配音仍是旧版，需要同时替换音频。

三个源文件
game/script.rpy       故事、选项、角色进出、音乐和语音，按阅读顺序排列。
game/cast.rpy         角色名、对话头像及图片路径。pine_unknown 显示“？？？”并使用菠萝头像。
game/presentation.rpy 标题、暂停菜单、书页、对话框和立绘站位。
图片、配音和音乐均随项目附带。替换美术或音频时可沿用原来的文件名。此版使用原生 Ren’Py 台词，运行和改词都不需要额外的 Python 包或数据转换步骤。

占位资源
配乐由 FluidSynth 和 TimGM6mb（Tim Brechbill、David Bolton）渲染；三个音效为合成音。日语对白使用 VOICEVOX 配音。思源宋体 Noto Serif CJK 简体中文字体的授权见 game/fonts/LICENSE.txt。

日语配音（VOICEVOX）
菠萝：VOICEVOX:離途（ノーマル）
蜜柑：VOICEVOX:もち子さん（CV：明日葉よもぎ）（ノーマル）
芒果：VOICEVOX:玄野武宏（喜び）
柠檬：VOICEVOX:ナースロボ＿タイプＴ（楽々）
苹果：VOICEVOX:猫使アル（ノーマル）
