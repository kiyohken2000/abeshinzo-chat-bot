import os
from flask import Flask, request
import torch
from transformers import T5Tokenizer, AutoModelForCausalLM #安倍晋三発言生成用
import pyopenjtalk

#安倍晋三モデル読み込み
tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium")#入出力文をトークンに変換する際の基準
tokenizer.do_lower_case = True #計算量を軽減
model = AutoModelForCausalLM.from_pretrained("./trainingData")

app = Flask(__name__)

@app.route('/', methods=['POST'])
def post_response():
  # 受信したテキストを代入
  request_dict = request.get_json()
  req_data = str(request_dict['data'])

  #入力テキストをトークン化
  input_text = '<s>' + req_data + '[SEP]'
  input_ids = tokenizer.encode(input_text, return_tensors='pt', add_special_tokens=False)
  
  #。で終了する文章ができるまで生成
  while True:
    out = model.generate(
      input_ids,
      do_sample = True,
      top_k = 100,
      top_p = 0.95,
      max_length = 35,
      temperature = 0.95,
      num_return_sequences = 1,
      bad_words_ids = [[tokenizer.bos_token_id], [tokenizer.sep_token_id], [tokenizer.unk_token_id]],
      repetition_penalty = 1.2,
    )
    #生成した文章トークンをstrに変換して不要部削除
    outlit = str(tokenizer.batch_decode(out))
    outlit = outlit.replace('<s>', '')
    outlit = outlit.split('[SEP]')[1]
    outlit = outlit.replace('</s>', '').strip()

    #生成した文に。が含まれていたら生成を終了
    if '。' in outlit:
      break
  
  #生成した文章を一文にして。を付け直す
  outlist = outlit.split('。')
  outlit = outlist[0]+'。'
  romaji = pyopenjtalk.g2p(outlit)

  result = {}
  result['origin'] = outlit
  result['romaji'] = romaji
  result['question'] = req_data

  print('result', result)

  return result

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))