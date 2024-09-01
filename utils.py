import requests

from config import APIConfig


async def video_url(url):
    url = f"https://Video-Downloader.proxy-production.allthingsdev.co/instagram/download?url={url}"

    headers = {
        'x-apihub-key': APIConfig.API_KEY,
        'x-apihub-host': APIConfig.API_HOST,
        'x-apihub-endpoint': APIConfig.API_ENDPOINT
    }

    response = requests.request("POST", url, headers=headers, data={})

    if response.status_code in (200, 201, 202):
        return response.json()
    else:
        raise Exception('Url is not working')