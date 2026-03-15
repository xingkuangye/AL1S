from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import random

halo_students = [
    "",
    # アビドス (Abydos)
    "砂狼白子", "小鸟游星野", "奥空绫音", "黑见茜香", "十六夜野宫", "砂狼白子（恐怖）",
    
    # アリウス (Arius)
    "锭前纱织", "秤亚津子", "戒野美咲", "槌永日和", "昴",
    
    # ヴァルキューレ (Valkyrie)
    "尾刃康娜", "中务桐乃", "合欢垣吹雪",
    
    # ゲヘナ (Gehenna) - 23名学生
    "羽沼真琴", "京极皋月", "枣伊吕波", "元宫千明", "丹花伊吹", "空崎日奈",
    "天雨亚子", "银镜伊织", "火宫千夏", "陆八魔爱露", "鬼方佳代子", "浅黄睦月",
    "伊草春香", "黑馆晴奈", "狮子堂泉", "鳄渊明里", "赤司纯子", "冰室濑名",
    "爱清风香", "牛牧朱莉", "下仓惠", "鬼怒川霞", "夜樱绮罗罗",
    
    # 山海経 (Shanhaijing) - 7名学生
    "龙华妃咲", "近卫南", "朱城瑠海", "鹿山丽情", "药子纱绫", "春原瞬", "春原心奈",
    
    # トリニティ (Trinity) - 26名学生
    "圣园未花", "桐藤渚", "百合园圣娅", "剑先鹤城", "静山真白", "仲正一花",
    "羽川莲见", "歌住樱子", "若叶日向", "伊落玛丽", "古关忧", "圆堂志美子",
    "白洲梓", "下江小春", "阿慈谷日富美", "浦和花子", "柚鸟夏", "杏山和纱",
    "栗村爱理", "伊原木好美", "苍森美祢", "朝颜花江", "鹫见芹娜", "守月铃美",
    "宇泽玲纱", "河驹风兰舞",
    
    # ハイランダー (Highlander)
    "橘光", "橘望", "内海青叶",
    
    # 百鬼夜行 (Hyakkiyako) - 17名学生
    "天地尼娅", "桑上果穗", "和乐千世", "御棱名草", "勘解由小路紫", "不破莲华",
    "桐生桔梗", "河和静子", "朝比奈菲娜", "里浜海香", "久田泉奈", "大野月咏",
    "千鸟满", "水羽三森", "勇美枫", "春日椿", "狐坂若藻",
    
    # ミレニアム (Millennium) - 25名学生
    "生盐诺亚", "黑崎小雪", "调月莉音", "早濑优香", "天童爱丽丝", "花冈柚子",
    "才羽绿", "才羽桃", "美甘妮露", "角楯花凛", "飞鸟马时", "室笠茜",
    "一之濑明日奈", "猫冢响", "白石歌原", "丰见琴里", "各务千寻", "小涂真纪",
    "小钩晴", "音濑小玉", "乙花堇", "野正莱依", "和泉元艾米", "明星日鞠", "天童凯伊",
    
    # レッドウィンター (Red Winter) - 10名学生
    "连河切里诺", "池仓真里奈", "佐城巴", "间宵时雨", "天见和香", "安守实里",
    "姬木芽瑠", "秋泉红叶", "荒槙八云", "三善贵音",
    
    # ワイルドハント (Wild Hunt)
    "绘里", "カノエ", "三与", "若狭冬", "薄叶律",
    
    # SRT - 4名学生
    "月雪宫子", "空井咲", "风仓萌绘", "霞泽美游",
    
    # コラボ (Collaboration) - 4名
    "初音未来", "御坂美琴", "食蜂操祈", "佐天泪子",
]

@register("AL1S", "星星旁の旷野", "毁灭世界", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("BBKB")
    async def bbkb(self, event: AstrMessageEvent):
        """邦邦咔邦！"""
        random_value = random.randint(1, 5)
        if random_value == 1:
            yield event.plain_result("邦邦咔邦！爱丽丝登场！")
        else:
            yield event.plain_result("邦邦咔邦！爱丽丝登场！")

    @filter.command("随机光环")
    async def random_aura(self, event: AstrMessageEvent):
        """随机光环图片"""
        logger.info("正在获取随机光环图片...")
        random_num = random.randint(1, 138)
        logger.info(f"获取到随机光环图片: {random_num}")
        yield event.plain_result(f"# 邦邦咔邦！\n老师，你要的随机光环图来啦！\n这是**{halo_students[random_num]}**的光环！\n![随机光环 #350px #350px](https://xingkuangye-public.oss-cn-beijing.aliyuncs.com/halo/{random_num}.png)")

