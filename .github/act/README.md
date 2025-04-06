# .github/act

ローカル環境で GitHub Actions のワークフローを実行するためのツール `act` の関連ファイルを保存しています

## 実行環境のインストール

ローカル環境にインストールする場合、複数の方法が用意されています。  
手軽な方法としては、リポジトリの README に記載の通り、インストール用スクリプトを実行する方法があります。

```bash
curl -s https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
```

ダウンロードされたファイルをパスの通ったディレクトリに移動してください。

## ワークフローの実行

`act` コマンド単体で実行すると、`push` イベントが発生したものとして GitHub Actions のワークフローが実行されます。  
`act` コマンドにオプションを付与することで、ワークフローの実行イベントを指定することができます。  
`act` コマンドのオプションについては、[Example Commands](https://github.com/nektos/act#example-commands) を参照してください。

## 環境変数ファイル

`.env` に、act 実行時の環境変数を保持させます。
GitHub リポジトリ上の Variables に対応します。
`act` 実行時に、`--env-file ./.github/act/.env` オプションでファイルを読み込みます。
秘匿情報を含む場合があるので、`.gitignore` に追加しています。
.env.example を参考に、設定を行ってください。

## 秘匿情報ファイル

`.secrets` に、act 実行時の秘匿情報を保持させます。
GitHub リポジトリ上の Secrets に対応します。
`act` 実行時に、`--secret-file ./.github/act/.secrets` オプションでファイルを読み込みます。
秘匿情報を含むため、`.gitignore` に追加しています。
.secrets.example を参考に、設定を行ってください。

## イベントプロパティの追加

あらかじめ作成した json ファイルを通じて、act 実行時のペイロード情報を追加することができます。  
act 実行時に、`-e ./.github/act/event.json` オプションでファイルを読み込みます。  
例えば、以下のコマンドを実行すると、`push-to-develop.json` が読み込まれ、  
リモートリポジトリで develop ブランチに対して push を行った時の動作をシミュレートできます。

```bash
act push -e ./.github/act/push-to-develop.json
```

`push-to-develop.json` は以下のように記述します。

```json
{
    "ref": "refs/heads/develop",
    "ref_name": "develop",
    "base_ref": "refs/heads/develop",
    "push": {
        "base_ref ": "refs/heads/develop"
    }
}
```

なお、`push-to-develop.json` はあくまでローカル環境における動作の確認のために用いるものです。  
GitHub のホスティング環境には影響を与えません。
