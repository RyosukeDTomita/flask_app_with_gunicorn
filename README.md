# flask app with gunicorn

![un license](https://img.shields.io/github/license/RyosukeDTomita/flask_app_with_gunicorn)

## INDEX

- [ABOUT](#about)
- [LICENSE](#license)
- [ENVIRONMENT](#environment)
- [PREPARING](#preparing)
- [HOW TO USE](#how-to-use)
- [ABOUT](#about)
- [REFERENCE](#reference)

---

## ABOUT

- Flask application を gunicorn と併用するテスト
- templates/にはapp.pyで使用するhtmlテンプレートを格納している。

---

## LICENSE

---

[NO LICENSE](./LICENSE)

---

## ENVIRONMENT

- python3.10
  - see [requiremets.txt](./requirements.txt)

---

## PREPARING

```shell
docker compose up
```

---

## HOW TO USE
### with gunicorn

1. [PREPARING](#preparing)
2. open browser and go to [localhost](http://localhost)

### just use python

1. [PREPARING](#preparing)
2. log in to the docker container.
3. run app.py with `python3` command.

```shell
docker compose exec -it app "/bin/bash"

cd /usr/local/app
python3 app.py
```


---


## REFERENCE
- [公式ドキュメント](https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/index.html)
- [jinja](https://jinja.palletsprojects.com/en/latest/): flask側で受け取った変数をtemplates/に渡す。
