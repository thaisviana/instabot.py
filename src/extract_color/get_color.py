from PIL import Image
import os
# import requests
#
# path = 'https://small-big-api.herokuapp.com/photo'
# response = requests.get(path, stream=False)
# result = response.json()
# for small_big in result['result']:
#     with open('../../imgs/'+small_big['shortcode'] + '.jpg', 'wb') as handle:
#         print(small_big['shortcode'])
#         response = requests.get(small_big['image_url'], stream=True)
#         if not response.ok:
#             print(response)
#         for block in response.iter_content(1024):
#             if not block:
#                 break
#             handle.write(block)


for image in os.listdir('../../imgs'):
    HUE, R, G, B = [], [], [], []
    if image.endswith('.jpg'):
        img = Image.open(f'../../imgs/{image}').convert('RGB')
        width, height = img.size
        for y in range(0, height):
            for x in range(0, width):
                r, g, b = img.getpixel((x, y))
                brightness = sum([r, g, b]) / 3
                HUE.append([r, g, b])
                R.append(r)
                G.append(g)
                B.append(b)
        r_average = sum(R) / R.__len__()
        g_average = sum(G) / R.__len__()
        b_average = sum(B) / R.__len__()
        result = f'[ average: {int(r_average)}, {int(g_average)}, {int(b_average)} ]'
        print(result)







