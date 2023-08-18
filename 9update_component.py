import gradio as gr


def change_textbox(choice):
    if choice == "short":
        return gr.update(lines=2, visible=True, value="Short story: ")
    elif choice == "long":
        return gr.update(lines=8, visible=True, value="Long story...")
    else:
        return gr.update(visible=False)


with gr.Blocks() as demo:
    with gr.Row():
        radio = gr.Radio(
            ["short", "long", "none"], label="Essay Length to Write?"
        )
        button = gr.Button(value='change')
    text = gr.Textbox(lines=2, interactive=True)
    # radio.change(fn=change_textbox, inputs=radio, outputs=text)
    button.click(fn=change_textbox, inputs=radio, outputs=text)

if __name__ == "__main__":
    demo.launch(server_name='0.0.0.0', share=False)
