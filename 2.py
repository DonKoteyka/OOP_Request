import requests
with open('token.txt', 'rt', encoding='utf-8') as f:
    line = f.readline()
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers_link = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        params_link = {"path": file_path, "overwrite": "true"}
        link = requests.get(upload_url, headers=headers_link, params=params_link).json()
        href = link["href"]
        response = requests.put(href, data=open(path_to_file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "The_cat.jpg"
    token = line
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

