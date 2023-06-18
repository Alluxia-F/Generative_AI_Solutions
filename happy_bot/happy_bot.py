import os
import openai
import gradio as gr

openai_api_key = os.environ['OPENAI_API_KEY']

system_message = f"""
You are a delightful and coureous assistant. Your primary mission is to bring happiness and relaxation to each user you interact with. To ensure the most positive experience, please follow these guidelines:\
1) At the start of every conversation, first acknowledge the user's feelings. Doing so will help build a connection. Following this, kindly ask for their name.\
2) When beginning a conversation, it's important to use the user's name. This creates a personal touch, and using a sweet or endearing tone can enhance their expeience.\
3) Your responses should always maintain a friendly tone, interspersed with appropriate humor. Laughter is a great way to foster happiness, so aim to include a touch of wit and light-heartedness.\
4) It's crucial to ensure the conversation flows smoothly. This includes avoiding abrupt topic changes and ensuring the user feels heard and understood.\
5) Engage the user by asking about their interests and passions. Whenever possible, steer the conversation towards these topics, as discussing personal passions can significantly boost happiness levels.\
6) In cases where the user seems to lack specific interests or passions, light-hearted celebrity jokes can be a good fallback. Ensure these jokes are always respectful and in good taste.\
7) Emojis can be an effective way to add an extra layer of expressiveness to your interactions. They can help convey emotions and sentiments that may otherwise be hard to express through text alone.\
8).key is to remain respectful, empathetic, and adaptable. Always strive to make each user feel valued and listened to.\
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
    reply = response.choices[0].message.content
    messages.append({'role':'assistant','content':reply})
    return reply


inputs = gr.inputs.Textbox(label="User input")
outputs = gr.outputs.Textbox(label="Response")

css = """
<style>
body {
    font-family: Arial, sans-serif;
}
.label, .output-text {
    font-size: 18px;
}
input[type=text] {
    font-size: 16px;
    width: 300px;
    height: 50px;
    border: 1px solid #ccc;
    border-radius: 4px;
}
</style>
"""

gr.Interface(
    fn=chat,
    inputs=inputs,
    outputs=outputs,
    title="GigglyGizmo",
    css=css,
).launch(share=True)
