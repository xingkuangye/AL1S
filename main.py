from unittest import case

from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
import random

@register("md超级测试", "星星旁の旷野", "毁灭世界", "1.0.0")
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
        random_num = random.randint(1, 138)
        yield event.plain_result(f"![随机光环](https://xingkuangye-public.oss-cn-beijing.aliyuncs.com/halo/{random_num}.png)")

        