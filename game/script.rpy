image hospital = "images/bg/hospital.png"

define p = Character('玩家', color="#c8ffc8")
define a = Character('未知聲音A', color="#c8ffc8")
define karin = Character('橘 花凜', color="#c8ffc8", image="karin")

label start:
    p "嗯...這是哪..."
    p "啊,頭好痛，我這是怎麼了？"
    p "咦..？我這是..在醫院！？？為什麼？？究竟.."
    a "你終於醒了！太好了~！"

    scene hospital

    "沒等我緩過來，一把少女的聲音打斷了我的思緒。"
    a "昨天晚上你都跟我約了還不停嚷嚷着女朋友，女朋友的不跟我做，所以我才下了葯，沒想到居然有後遺症"
    a "真是嚇死我了，你可不要生我氣，我不是故意的"
    a "對了！該去叫醫生的，要等花凜喲~"
    p "唉..等等，我聽到了什麼？？！？"
    p "啊這.."
    p "我？？？我這是跟人來了一發之後第二天醒來失憶了？？"
    p "頭這麼痛是撞了嗎？還是我玩什麼激烈的play了嗎？"
    p "可惡我怎沒有記憶？？"
    p "不對，女朋友？"
    p "我有女朋友了？我女朋友誰？"
    p "有了女朋友我還跟人約*？"
    p "還有下藥，後遺症什麼的,這都什麼事啊..."
    "我開始思索起來了。"
    "......"
    "..."
    p "所以，結論是我在有女朋友的情況下還跟別的女生約*，但過程好像發生了什麼，我不願意，所以剛才那個女生給我下藥了？然後那個藥好像有副作用啥的"
    p "然後，我，現在完全沒有昨天的記憶，而且感覺...我還忘了什麼...這..這TM不就是失憶嗎！！"
    "看來槽點好像太多，讓我無從下手。"
    p "這不就打*打太嗨打到失憶，噢，還是個出軌渣男.."
    p "所以，現在為了男人的尊嚴，我不能讓人發現我打*打到失憶了，還要隱瞞我出軌的情況下找到我女朋友是誰..."
    p "聽着就好難..."
    "那麼現在我該幹嘛？"
    "總之先調查一下周圍。"

    #起床

    menu:
        "想要調查什麼呢"
        "查看床頭":
            $ known_pw = False
            jump search_sidetable
    return


label search_sidetable:
    #看向床頭櫃
    menu:
        "查看手機":
            if known_pw:
                p "唉，要密碼..."
                p "試什麼好？我生日？"
                "噠噠噠"
                "手機解鎖了。"
                "啊，成功了。"
                jump search_phone
            else:
                p "唉,不知道密碼。"
                p "先調查其他東西好了。"
                jump search_sidetable
        "查看錢包":
            "唉，果然有身份證。"
            "名字是XXX，出生XX年XX月XX日。"
            "唉，只有幾張100塊在裏面。"
            $ known_pw = True
            jump search_sidetable


label search_phone:
    menu:
        "由於劇情需要,現在只能選一樣。"
        "調查相册":
            $ searched_photo1 = False
            $ searched_photo2 = False
            $ searched_photo3 = False
            $ searched_photo4 = False
            jump search_photo
        "調查備忘錄":
            pass
        "調查手機聯絡人":
            pass

label search_photo:
    menu:
        "查看相冊一":
            if not searched_photo1:
                $ searched_photo1 = True
                p "咦？"
                p "全部相片内都有兩個人，其中一個是剛剛的那個女孩。"
                menu:
                    "是否繼續查看照片的詳情？"
                    "是":
                        p "有很多我和她的合照"
                        p "我們關係看起來很親密"
                        p "這究竟是怎麽一回事？我跟她看起來簡直就像是男女朋友的關係，那昨晚究竟是怎麽一回事？？"
                        jump out_hospital
                    "否":
                        jump search_photo
            else:
                "已查閲該相冊"
                jump search_photo
        "查看相冊二":
            if not searched_photo2:
                $ searched_photo2 = True
                p "咦？是很多兩個人的合照呢"
                p "其中那個金髮女孩是誰呢？沒有印象"
                menu:
                    "是否繼續查看照片的詳情？"
                    "是":
                        p "有好幾張也是我和她在抱在一起的合照"
                        p "難道我們的關係是...？"
                        jump out_hospital
                    "否":
                        jump search_photo
            else:
                "已查閲該相冊"
                jump search_photo
        "查看相冊三":
            if not searched_photo3:
                $ searched_photo3 = True
                p "咦？這個相冊有很多類似收據的物體"
                p "還有好幾張黑長直女性的照片"
                menu:
                    "是否繼續查看照片的詳情？"
                    "是":
                        p "仔細一看，原來那不是收據"
                        p "類似是告假紙"
                        p "但請假原因看得不是很清楚呢"
                        jump out_hospital
                    "否":
                        jump search_photo
            else:
                "已查閲該相冊"
                jump search_photo
        "查看相冊四":
            if not searched_photo4:
                $ searched_photo4 = True
                p "幾乎全部都是一個茶髮女孩的相片"
                p "當中也有幾張我和她的合照"
                menu:
                    "是否繼續查看照片的詳情？"
                    "是":
                        p "真的很多這個茶髮女孩笑顔的相片欸"
                        p "數量多的有點離譜欸"
                        p "難道她是我的女朋友？"
                        jump out_hospital
                    "否":
                        jump search_photo
            else:
                "已查閲該相冊"
                jump search_photo


label out_hospital:
    pass

#label contin_search_photo:
#    menu:
#        "是否繼續查看相冊？"
#        "是":
#            jump search_photo
#        "否":
#            jump
