from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register

@register("md超级测试", "星星旁の旷野", "毁灭世界", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("文字")
    async def helloworld(self, event: AstrMessageEvent):
        """测试md文字"""
        yield event.plain_result("当你看到这段话，证明纯文字md测试正常") 
        yield event.plain_result("""**当你看到这段被加粗，证明粗体文字md测试正常**
*当你看到这段被斜体，证明斜体文字md测试正常*
~~当你看到这段被删除线，证明删除线md测试正常~~
__当你看到这段被下划线，证明下划线md测试正常__
***当你看到这段被加粗斜体，证明加粗斜体md测试正常***
当你看到这段被代码块包裹，证明代码块md测试正常
```
print('Hello World')
```""") 