# AI安倍晋三チャットボット

テキストを渡すと安倍晋三風のテキストを返すウェブAPI(CloudRun用)

trainingDataフォルダは重いので別で

## Request

```
// curl
curl -X POST -H "Content-Type: application/json; charset=utf-8" -d '{"data":"あなたは安倍晋三ですか"}' https://webapi-test-omc3n2et7a-an.a.run.app

// axios
const res = await axios.post(
  'https://webapi-test-omc3n2et7a-an.a.run.app',
  {
    'data': 'あなたは安倍晋三ですか'
  },
  {
    headers: {
      "Content-Type" : "application/json; charset=utf-8"
    }
  }
)
const { origin, romaji, question } = res.data
```

## Response

```
{
  "origin": "これは、今まで申し上げているとおりでありまして、私は内閣総理大臣であると同時に自由民主党の総裁であります。",
  "question": "あなたは安倍晋三ですか",
  "romaji": "k o r e w a pau i m a m a d e m o o sh i a g e t e i r u t o o r i d e a r i m a sh I t e pau w a t a sh i w a n a i k a k U s o o r i d a i j i N d e a r u t o d o o j i n i j i y u u m i N sh U t o o n o s o o s a i d e a r i m a s U"
}
```