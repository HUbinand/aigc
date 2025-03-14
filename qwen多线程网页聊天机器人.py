# 需求：使用gradio稳定的调用阿里云的qwenLLM大模型，实现一个网页聊天机器人
# 需要实现不同用户访问对外开放的网站时候，可以独立对话，互不影响，实现多用户同时对话。
# 需要实现流式输出，即机器人回复的时候，可以逐字符输出，而不是一次性输出。
# 需要在本地保存用户的聊天记录。
# 注意启用的时候不要开VPN不然会gradio链接失败
import random
import gradio as gr
import time
import qwen调用 as qwen
import threading

# 一个字典用于存储每个会话的独立Qwen机器人实例
user_robots = {}

# 实例化Qwen机器人并为每个会话创建一个新的实例
def get_qwen_bot(session_hash):
    if session_hash not in user_robots:
        # 使用session_hash为每个用户创建独立的机器人
        user_robots[session_hash] = qwen.Qwen_LongLLM("qwen-plus")
    return user_robots[session_hash]

# qwen函数
def qwen_bot(message, history, request: gr.Request):
    session_hash = request.session_hash  # 获取当前用户会话的唯一标识
    bot = get_qwen_bot(session_hash)  # 获取当前会话的独立Qwen机器人

    # 这里模拟流式输出
    respon = bot.chat(message)
    # 你可以根据需要逐字符返回
    for i in range(1, len(respon) + 1):  # 循环逐步返回
        yield "Qwen_bot: " + str(respon)[:i]
        time.sleep(0.02)  # 模拟延迟0.02秒

# 自定义gr.ChatInterface
gr.ChatInterface(
    qwen_bot,  # 指定处理逻辑的函数
    type="messages",  # 指定消息类型为“消息”格式，界面显示为对话框的样式
    title="HB:网页聊天机器人",
    description="这是一个聊天机器人，输入任何你想输入的文本内容吧！",
    theme="soft",  # 选择软色主题，界面的配色会比较柔和
    cache_examples=True,  # 启用示例缓存，以提高加载速度
).launch(share=True)
