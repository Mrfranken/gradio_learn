import gradio as gr
import numpy as np


# def greet(name):
#     return "Hello " + name + "!"
#
# demo = gr.Interface(
#     fn=greet,
#     # inputs="text",
#     inputs=gr.Textbox(lines=2, placeholder='input here'),
#     outputs="text")

# def greet(name, is_morning, temperature):
#     salutation = "Good morning" if is_morning else "Good evening"
#     greeting = f"{salutation} {name}. It is {temperature} degrees today"
#     celsius = (temperature - 32) * 5 / 9
#     return greeting, round(celsius, 2)
#
#
# demo = gr.Interface(
#     fn=greet,
#     inputs=["text", "checkbox", gr.Slider(0, 100)],
#     outputs=["text", "number"],
# )

# def sepia(input_img):
#     sepia_filter = np.array([
#         [0.393, 0.769, 0.189],
#         [0.349, 0.686, 0.168],
#         [0.272, 0.534, 0.131]
#     ])
#     sepia_img = input_img.dot(sepia_filter.T)
#     sepia_img /= sepia_img.max()
#     return sepia_img
#
# demo = gr.Interface(sepia, gr.Image(type="filepath",shape=(200, 200)), "image")


def greet(name):
    return "Hello " + name + "!"


with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

if __name__ == "__main__":
    demo.launch(server_name='0.0.0.0', share=False)
