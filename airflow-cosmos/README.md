![Cosmos Logo](https://raw.githubusercontent.com/astronomer/astronomer-cosmos/main/docs/_static/cosmos-logo.svg)

-------------------

以下の手順に従って、AirflowとDBTを含む環境をセットアップできる:

1. リポジトリのルートディレクトリに移動

```bash
cd airflow-cosmos
```

2. 環境変数を含む`.env`ファイルを作成

```bash
echo DB_USER=%JQU1%>docker/.env
echo DB_PASS=%JQP%>>docker/.env
echo DB_NAME=%JQD%>>docker/.env
```

3. Dockerイメージをビルド

```bash
docker build -f ./docker/Dockerfile -t airflow-dbt .
```

4. Dockerコンテナを実行。以下のコマンドはWindowsの場合の例です。LinuxやmacOSでは`\`を`^`に置き換える

```bash
docker run -it --rm ^
    --name airflow-dbt ^
    --user airflow ^
    --env-file docker/.env -p 8080:8080 ^
    -v %cd%/airflow/dags:/usr/local/airflow/dags ^
    -v %cd%/airflow/logs:/usr/local/airflow/logs ^
    -v %cd%/docker:/usr/local/docker ^
    airflow-dbt
```

## コンテナ作成時の初期設定

コンテナ作成時、初回のみ以下のコマンドを実行し、Airflowを初期化

```bash
source airflow/dbt_venv/bin/activate && source ./docker/init.sh
```

## 手動設定

コンテナ作成後、以下の手動設定が必要

1. ブラウザで `http://127.0.0.1:8000` にアクセスし、Airflow UIを開く。

2. Airflow UIの「Admin」メニューから「Connections」を選択

3. 「Create」ボタンをクリックし、新しいコネクションを作成

4. 以下の項目を設定します：
   - `Conn Id`: `airflow_db`
   - `Conn Type`: `Postgres`
   - `Host`: データベースのホスト名(ex. host.docker.internal)
   - `Port`: データベースのポート番号
   - `Password`: データベースのパスワード
   - `Database`: データベース名
   - `Login`: データベースのユーザー名

以下のコマンドを実行することで、Airflow WebserverとSchedulerを実行

```bash
source airflow/dbt_venv/bin/activate && airflow webserver --port 8080 & airflow scheduler
```
