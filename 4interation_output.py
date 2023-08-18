import gradio as gr
import numpy as np
import time


# define core fn, which returns a generator {steps} times before returning the image
def fake_diffusion(steps):
    for _ in range(steps):
        time.sleep(1)
        image = np.random.random((100, 100, 3))
        yield image
    image = r"https://img2.baidu.com/it/u=2630224817,3435808580&fm=253&fmt=auto&app=120&f=JPEG?w=231&h=500"
    yield image


demo = gr.Interface(fake_diffusion, inputs=gr.Slider(1, 10, 3), outputs="image")

# define queue - required for generators
demo.queue()

if __name__ == "__main__":
    demo.launch(server_name='0.0.0.0', share=False)
