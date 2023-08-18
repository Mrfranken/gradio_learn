import gradio as gr

count = 0


def show(num, ):
    num = int(num) + 1
    print('+++++', num)
    return gr.update(value=str(num)), gr.update(visible=True)
    # return count




with gr.Blocks() as demo:
    text = gr.Text(value='1')
    # text1 = gr.Text()
    button = gr.Button('add')

    textboxes = []
    for i in range(5):
        t = gr.Textbox(f"Textbox {i}", visible=False)
        textboxes.append(t)

    button.click(show, inputs=text, outputs=[text, textboxes[int(text.value) - 1]])

    # button.click(show, inputs=text, outputs=[text, text1])

if __name__ == "__main__":
    demo.launch(server_name='0.0.0.0', share=False)


# import gradio as gr
#
# # def my_interface():
# html_content = """
# <script>
# function addTextbox() {
#     var textboxDiv = document.createElement("div");
#     var textbox = document.createElement("input");
#     textbox.setAttribute("type", "text");
#     textboxDiv.appendChild(textbox);
#     document.getElementById("textbox-container").appendChild(textboxDiv);
# }
# </script>
#
# <button onclick="addTextbox()">Add Textbox</button>
# <div id="textbox-container"></div>
# """
#
# demo = gr.Interface(fn=None, layout="auto", live=False, webapp=html_content)
#
# if __name__ == "__main__":
#     demo.launch(server_name='0.0.0.0', share=False)
