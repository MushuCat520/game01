# 定义角色
define a = Character("爱丽丝", color="#ffc0cb")
define b = Character("我", color="#ffffff")

# 使用纯色背景，避免缺失图片导致报错
image bg black = Solid("#000000")
image bg white = Solid("#ffffff")
image bg pink = Solid("#ffc0cb")

label start:
    scene bg black
    "（清晨，阳光透过窗帘洒在房间里）"
    b "今天又是新的一天呢。"
    
    show bg pink with dissolve
    "突然，一个粉色头发的少女出现在眼前。"
    
    a "早上好！你今天看起来精神不错。"
    a "你今天有空吗？要不要一起出去逛逛？"
    
    menu:
        "当然有空！":
            jump yes_route
        "抱歉，我今天很忙。":
            jump no_route
            
label yes_route:
    scene bg white
    a "太好了！那我们去公园吧！"
    "于是，我们在公园度过了一个愉快的下午。"
    jump end
    
label no_route:
    scene bg black
    a "这样啊……那下次再说吧。"
    "看着爱丽丝失落的背影，我有点后悔了。"
    jump end
    
label end:
    "（第一章 完）"
    return
