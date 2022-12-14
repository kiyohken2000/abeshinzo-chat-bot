# AI安倍晋三チャットボット

テキストを渡すと安倍晋三風のテキストを返すウェブAPI(CloudRun用)

[trainingData](https://drive.google.com/file/d/1gHnvGmhyhE6fQ_3YT7l-x0AbeUcLluSI/view?usp=sharing)フォルダは展開してルートディレクトリに配置。

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

## ローカルでのテスト手順

### Requirements

- Python3
- CMake
- pip

### Install

```
pip install -r requirements.txt
```

### Run

```
python -c "import test; test.hello()"
```

## Commands

### パッケージの書き出し

```
pip freeze > requirements.txt
```

### Cloud Runにデプロイ

コマンド実行後、GCPコンソール上で新しいリビジョンの編集とデプロイをする

`hey-abe`はGCPのプロジェクト名

参考：[【GCP初心者向け】Cloud Runでサーバーレスな超簡易Web APIを無料で作る](https://qiita.com/dzbt_dzbt/items/dde54e3417ae5c17730b)

```
gcloud builds submit --tag gcr.io/hey-abe/hello-api --project hey-abe
```

### アップロードされるファイルの確認

```
gcloud meta list-files-for-upload
```