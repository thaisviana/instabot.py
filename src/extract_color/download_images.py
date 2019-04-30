
import requests

path = 'https://small-big-api.herokuapp.com/photo'
response = requests.get(path, stream=False)
result = response.json()
for small_big in result['result']:
    with open('imgs/'+small_big['shortcode'] + '.jpg', 'wb') as handle:
        print(small_big['shortcode'])
        response = requests.get(small_big['image_url'], stream=True)
        if not response.ok:
            print(response)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)