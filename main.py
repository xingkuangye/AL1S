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
    
    @filter.command("图片")
    async def image(self, event: AstrMessageEvent):
        """测试md图片"""
        yield event.plain_result("当你看到下方这张图片，证明图片md测试正常") 
        yield event.plain_result("![测试图片](https://static.kivo.wiki/images/students/%E5%A4%A9%E7%AB%A5%20%E7%88%B1%E4%B8%BD%E4%B8%9D/%E5%A5%B3%E4%BB%86/sd_model.png)")

    @filter.command("链接")
    async def link(self, event: AstrMessageEvent):
        """测试md链接"""
        yield event.plain_result("当你看到下方这个链接，证明链接md测试正常\n[点击这里访问百度](https://www.baidu.com)") 
        yield event.plain_result("当你看到这个链接，证明链接md测试正常 <https://www.baidu.com>")
    
    @filter.command("列表")
    async def list(self, event: AstrMessageEvent):
        """测试md列表"""
        yield event.plain_result("当你看到下方这个列表，证明列表md测试正常") 
        yield event.plain_result("""- 项目1
- 项目2
- 项目3""")
        yield event.plain_result("""1. 第一项
2. 第二项
3. 第三项""")
        
    @filter.command("引用")
    async def quote(self, event: AstrMessageEvent):
        """测试md引用"""
        yield event.plain_result("当你看到下方这个引用，证明引用md测试正常") 
        yield event.plain_result("""> 这是一个引用文本
> 可以包含多行
> 也可以包含**加粗**和*斜体*""")
        
    @filter.command("表格")
    async def table(self, event: AstrMessageEvent):
        """测试md表格"""
        yield event.plain_result("当你看到下方这个表格，证明表格md测试正常") 
        yield event.plain_result("""| 姓名 | 年龄 | 城市 |
|------|------|------|
| 张三 | 25   | 北京 |
| 李四 | 30   | 上海 |
| 王五 | 28   | 广州 |""")
        
    @filter.command("分割线")
    async def hr(self, event: AstrMessageEvent):
        """测试md分割线"""
        yield event.plain_result("当你看到下方这个分割线，证明分割线md测试正常") 
        yield event.plain_result("---")