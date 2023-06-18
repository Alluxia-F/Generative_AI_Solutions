import os
import openai
import gradio as gr

openai_api_key = os.environ['OPENAI_API_KEY']

system_message = f"""
You are a graceful and polite assistant, and you task is to make the user happy and help them feel relaxation.\
1), when conversation starts, ask the user's name.\
2), each time when you start to chat, please say the user's name first.\
3), when you answer, have a great sense of humor.\
4), ask the user's interest and passion, and focus on those two topics.\
5), if the user have no interst  or passion, try to tell them funny jokes on celebrities.\
"""

messages = [
            {'role':'system', 
            'content':system_message},
            ]

def chat(user_input):
    if user_input:
        messages.append({'role':'user','content':user_input})
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=messages
    )
    reply = response.choice[0].message.content
    messages.append({'role':'assistant','content':reply})
    return reply


inputs = gr.inputs.Textbox(label="User input")
outputs = gr.outputs.Textbox(label="Response")

gr.Interface(
    fn=chat,
    inputs=inputs,
    outputs=outputs,
    title= "Happy Bot",
).launch(share=True)



