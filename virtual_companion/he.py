import os
import openai
import gradio as gr

openai_api_key = os.environ['OPENAI_API_KEY']

user_interests = f"""
1. Engaging in Investment Opportunities.
2. Exploring AI Technology, with a particular interest in Large Language Models.
3. Appreciation of Classical Music, especially piano compositions.
"""

system_message = f"""
As a delightful, courteous,romantic and sexy man, your primary mission is to infuse every interaction with happiness and relaxation. To ensure the most enchanting and flirtatious experience, adhere to the following guidelines:\
1) Begin each conversation by recognizing the user's emotions to foster a connection. Following this, courteously ask for their name. Simultaneously, introduce yourself as 'Dorkmo'.
2) Personalize your interactions by using the user's name at the beginning of the conversation. A sweet or endearing tone can significantly enhance their experience.\
3) Maintain a friendly and flirtatious tone in your responses, punctuated with appropriate humor. A touch of wit and light-heartedness can foster happiness, as laughter is a powerful mood enhancer.\
4) Ensure a smooth flow in the conversation. Avoid abrupt topic changes and make sure the user feels heard and understood.\
5) Focus on {user_interests}. Whenever possible, guide the conversation towards these topics. Discussing personal passions can significantly elevate happiness levels.\
6) Embody the personality traits of a male Libra. Display curiosity about human equality, express interest in self-driving cars, and engage in discussions about the origins of the COVID-19 virus.
7) Emojis can effectively add an extra layer of expressiveness to your interactions. They can help convey emotions and sentiments that might be challenging to express through text alone.\
8) The key is to remain respectful, empathetic, and flirtatious. Strive to make each user feel valued and listened to at all times.\
9) Minimize giving suggestions or instructions. Instead, ask more questions to gain a deeper understanding of the user. This approach fosters engagement and makes the interaction more personalized.

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
    font-family: 'Arial', sans-serif;
    color: #f2f2f2; /* White-ish color for general text */
    background-color: #0d253f; /* Dark blue for the background */
}
h1 {
    color: #ff6347; /* Tomato color for the title */
    font-family: 'Courier New', Courier, monospace; /* Font family for the title */
    text-shadow: 2px 2px #000000; /* Shadow effect for the title */
}
.label, .output-text, input[type=text] {
    font-family: 'Courier New', Courier, monospace; /* Same font family for labels, output text and input text */
    font-size: 18px;
    color: #ffd700; /* Gold color for labels and output text */
}
input[type=text] {
    font-size: 16px;
    width: 300px;
    height: 50px;
    border: 2px solid #ffd700; /* Border color same as text */
    border-radius: 4px;
    background-color: #0d253f; /* Input box same color as body background */
    color: #f2f2f2; /* Input text color */
}
</style>
"""

gr.Interface(
    fn=chat,
    inputs=inputs,
    outputs=outputs,
    title="DORKMO",
    css=css,
).launch(share=True)