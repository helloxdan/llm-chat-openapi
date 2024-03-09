import openai
from config import config

openai.api_key = config.OPENAI_API_KEY

'''
engine：指定使用的文本生成引擎。OpenAI的文本生成API支持多个引擎，包括GPT-3和GPT-2等。该参数是必需的，并且必须指定为字符串类型。

prompt：指定要生成文本的前缀，也就是要求OpenAI模型完成的任务描述。该参数是必需的，并且必须指定为字符串类型。

temperature：控制模型生成文本的创造性程度。值越高，生成的文本越随机和创造性；值越低，生成的文本越保守和可预测。该参数是可选的，其默认值为0.5。

max_tokens：控制生成文本的长度。该参数指定生成文本所需的最大令牌数。一个令牌可以是一个单词或一个标点符号。该参数是可选的，其默认值为2048。

n：指定要生成的文本数量。该参数指定要生成的不同文本序列的数量。该参数是可选的，其默认值为1。

stop：指定在生成文本时停止的标记，例如"</s>"。如果生成的文本包含了该停止标记，则OpenAI模型将停止生成更多的文本。该参数是可选的。

presence_penalty：控制模型是否避免在生成文本中多次使用相同的词语。该参数值越高，生成的文本中相同的词语出现的次数就越少。该参数是可选的，其默认值为0。

frequency_penalty：控制模型是否避免在生成文本中使用罕见的词语。该参数值越高，生成的文本中罕见的词语出现的次数就越少。该参数是可选的，其默认值为0。

best_of：指定在多个生成文本序列中选取最好的序列数量。该参数是可选的，其默认值为1。
'''


def chat(prompt):
    try:
        # 调用ChatGPT的api
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5,
        )
        # 获取返回的结果
        answer = response.choices[0].text.strip()
        return answer
    except Exception as e:
        print(e)
        return 'ERR'


def dialog(chat_list):
    # 避免对话次数过多，限制传到api的对话轮次不超过5次
    if len(chat_list) <= 10:
        prompt = " ".join(chat_list)
    else:
        prompt = " ".join(chat_list[-10:])
    # ChatGPT的回复
    answer = chat(prompt)
    return dict(context=answer)


def send_chat(data):
    cnt = data.get('cnt')
    return dialog(cnt)
