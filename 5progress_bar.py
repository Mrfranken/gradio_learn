import gradio as gr
import time


def slowly_reverse(word, sleep, progress=gr.Progress()):
    # progress(0, desc="Starting")
    # time.sleep(1)
    # progress(0.05)
    new_string = ""
    for letter in progress.tqdm(word, desc="Reversing"):
        time.sleep(sleep)
        new_string = letter + new_string
    return new_string


# demo = gr.Interface(slowly_reverse, gr.Text(), gr.Text())

with gr.Blocks() as demo:
    # gr.Interface(slowly_reverse, gr.Text(), gr.Text())
    word = gr.Textbox('input word')
    submit_button = gr.Button('submit')
    progress = gr.Textbox()
    sleep = gr.Slider(1, 3, step=0.5, show_label=True)
    submit_button.click(slowly_reverse, [word, sleep], progress)

if __name__ == "__main__":
    demo.queue(concurrency_count=10).launch()
