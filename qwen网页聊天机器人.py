import random
import gradio as gr
import time
import qwen调用 as qwen

# 实例化一次避免重复调用
Qwen_bot = qwen.Qwen_LongLLM("qwen-turbo")
# qwen函数
def qwen_bot(message, history):
    # 这里模拟流式输出
    respon = Qwen_bot.chat(message)
    # 你可以根据需要逐字符返回
    for i in range(1, len(respon) + 1):  # 循环逐步返回
        yield "Qwen_bot: " + str(respon)[:i]
        time.sleep(0.02)  # 模拟延迟0.02秒

print("打印框架返回内容",gr.Request.__dict__)
# 自定义gr.ChatInterface
gr.ChatInterface(
    qwen_bot, # 指定处理逻辑的函数
    type="messages", #指定消息类型为“消息”格式，界面显示为对话框的样式。
    title="HB:网页聊天机器人",
    description="这是一个聊天机器人，输入任何你想输入的文本内容吧！",
    theme="soft",   # 选择软色主题，界面的配色会比较柔和。
    cache_examples=True, # 启用示例缓存，以提高加载速度。
).launch(share=True)