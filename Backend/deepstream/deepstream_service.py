import requests

DEEPSTREAM_VISUAL_SEARCH_URL = 'http://localhost:50052/visual-search'  # Update with actual DeepStream endpoint

def process_image(image):
    files = {'image': image.read()}
    response = requests.post(DEEPSTREAM_VISUAL_SEARCH_URL, files=files)
    return response.json()
