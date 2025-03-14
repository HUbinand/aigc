# 最常用的基础模块
# 应用界面：gr.Interface(简易场景), gr.Blocks(定制化场景)

# 输入输出：gr.Image(图像), gr.Textbox(文本框), gr.DataFrame(数据框), gr.Dropdown(下拉选项), gr.Markdown, gr.Files

# 控制组件：gr.Button(按钮)

# 布局组件：gr.Tab(标签页), gr.Row(行布局), gr.Column(列布局)

import gradio as gr

# 定义一个函数，该函数接受两个参数：name和intensity，并返回一个字符串。
def greet(name, intensity):
    return "hello, " + name + "!" * int(intensity)
print(greet("Alice", 3))  # 确认输出 "Hello, Alice!!!"

#gr.Interface：用来定义一个简单的 Web 界面，连接函数与用户交互。
demo = gr.Interface(
    fn=greet, #指定处理逻辑的函数
    inputs=["text", "slider"], #指定输入组件类型
    outputs=["text"], #指定输出组件类型
)

#本地节点
# demo.launch() #默认仅限本地访问，外部设备无法直接访问。
#对外开放
demo.launch(share=True)