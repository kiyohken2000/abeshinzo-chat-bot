import torch
from transformers import T5Tokenizer, AutoModelForCausalLM #安倍晋三発言生成用
import re #名前を変更する際に正規表現を使用
import pyopenjtalk

#安倍晋三モデル読み込み
tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium")#入出力文をトークンに変換する際の基準
tokenizer.do_lower_case = True #計算量を軽減
model = AutoModelForCausalLM.from_pretrained("./trainingData")

#漢字の正規表現
chinese_chr = re.compile('[\u2E80-\u2FDF\u3005-\u3007\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\U00020000-\U0002EBEF]+')

print('torch version:', torch.__version__)

def hello():
  #入力テキストをトークン化
  input_text = '<s>' + 'あなたは安倍晋三ですか' + '[SEP]'
  input_ids = tokenizer.encode(input_text, return_tensors='pt', add_special_tokens=False)
  
  #。で終了する文章ができるまで生成
  while True:
    out = model.generate(
      input_ids,
      do_sample = True,
      top_k = 100,
      top_p = 0.95,
      max_length = 100,
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
  outlist=outlit.split('。')
  outlit=outlist[0]+'。'
  
  #生成した文章を関数の戻り値に
  result = {}
  result['origin'] = outlit
  result['romaji'] = pyopenjtalk.g2p(outlit)
  print(result)

  return outlit