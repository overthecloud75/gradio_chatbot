import time 
import requests
import copy

from configs import LLM_DOMAIN, logger

class LLM():
    def __init__(self):
        self.logger = logger
        self.headers = {
            'User-Agent': 'Mozilla/5.0',
            'Content-Type': 'application/json'
        }
        self.model = self.get_llm_model()

    def get_base_result_from_llm(self, url, method='GET', data=[]):
        timestamp = time.time()
        try:
            if method == 'GET':
                response = requests.get(url, headers=self.headers)
            else:
                response = requests.post(url, json=data, headers=self.headers)
            # 응답 데이터 처리
            if response.status_code == 200:
                result = response.json()
            else:
                self.logger.error(f'Failed to fetch data: {response.status_code}')
                self.logger.error(response.text)
                result = ''     
        except Exception as e:
            self.logger.error(e)
            result = ''
        self.logger.info(f'LMM resposne_time: {round(time.time() - timestamp, 2)}')
        return result
    
    def get_llm_model(self):
        llm_url = LLM_DOMAIN + '/v1/models'
        result = self.get_base_result_from_llm(llm_url, method='GET')
        if result and result['data']:
            llm_model = result['data'][0]['id']
        else:
            llm_model = ''
        return llm_model
    
def get_result_from_llm(self, prompt, history):
    llm_url = LLM_DOMAIN + '/v1/chat/completions'
    if history:
        messages = copy.deepcopy(history)
        messages.append({'role': 'user', 'content': prompt})
    else:
        messages = [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': prompt}
        ]
    if self.model:
        data = {'model': self.model, 'messages': messages}
        result = self.get_base_result_from_llm(llm_url, method='POST', data=data)
        if result:
            try:
                result = result['choices'][0]['message']['content']
            except Exception as e:
                self.logger.error(e)
                result = ''
    else:
        result = ''
    return result
