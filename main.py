from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import random

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
        yield event.plain_result(f"邦邦咔邦！老师，你要的随机光环图来啦！\n![随机光环 #350px #350px](https://xingkuangye-public.oss-cn-beijing.aliyuncs.com/halo/{random_num}.png)")

