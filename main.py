import gradio as gr

from ai import LLM
from configs import logger 

llm = LLM()
llm_model = llm.model

def chatbot_response(user_input, history):
    logger.info('user input: {}'.format(user_input))
    bot_reply = llm.get_result_from_llm(user_input, history)
    logger.info('bot reply: {}'.format(bot_reply))
    logger.info(history)
    return bot_reply

with gr.Blocks() as demo:
    gr.Markdown(f'''# 🤖 Chatbot''' )
    gr.Markdown(f'''## llm model: {llm_model}''' )
    gr.Markdown('아래에 메시지를 입력해 대화를 시작하세요!')
    gr.ChatInterface(
        fn=chatbot_response, 
        type='messages',
    )

if __name__ == '__main__':
    demo.launch(server_name='0.0.0.0')