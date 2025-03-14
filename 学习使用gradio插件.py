import random
import gradio as gr
import time
import qwen调用 as qwen

# 使用 gr.ChatInterface（）中，您应该做的第一件事是定义您的聊天函数。
# 你的 chat 函数应该接受两个参数： message 和 history （参数可以命名为任何名称，但必须按此顺序

# 最简单例子不思考历史记录
# def random_response(message, history):
#     return random.choice(["Yes", "No"])
# history的作用是保存聊天历史记录，下面是例子
# [
#     {"role": "user", "content": "What is the capital of France"},
#     {"role": "assistant", "content": "Paris"}
# ]

# 思考历史记录
# def alternatingly_agree(message, history):
#     if len([h for h in history if h['role'] == "assistant"]) % 2 == 0:
#         return "在历史记录中机器人回答次数是偶数"
#     else:
#         return "在历史记录中机器人回答次数是奇数"
# gr.ChatInterface(slow_echo, type="messages").launch(share=True)

# 流式输出
def slow_echo(message, history):
    for i in range(len(message)):
        time.sleep(0.02) # 模拟延迟0.03秒
        # yield 语句逐步返回消息
        # message[: i+1]是从0到i+1的切片字符用于流式输出
        yield "You typed: " + message[: i+1]

# 自定义gr.ChatInterface
gr.ChatInterface(
    slow_echo, # 指定处理逻辑的函数
    type="messages", #指定消息类型为“消息”格式，界面显示为对话框的样式。
    title="HB:文本放回功能",
    description="这是一个文字回放功能的网站，输入任何你想输入的文本内容吧！",
    theme="soft",   # 选择软色主题，界面的配色会比较柔和。
    cache_examples=True, # 启用示例缓存，以提高加载速度。
).launch(share=True)