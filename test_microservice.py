import requests
import base64

def test_microservice():
    # URL of the microservice
    base_url = "http://127.0.0.1:5000"

    # Upload an image
    image_path = "dog.png"
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode('utf-8')

    upload_payload = {
        "uploader_name": "John Doe",
        "image": encoded_image,
        "tags": ["nature", "sunset", "landscape"]
    }

    upload_response = requests.post(f"{base_url}/uploadImage", json=upload_payload)
    print("Upload Response:", upload_response.json())

    # Retrieve image by tags
    retrieve_payload = {"taglist": ["nature"]}
    retrieve_response = requests.get(f"{base_url}/returnImage", json=retrieve_payload)
    print("Retrieve Response:", retrieve_response.json())

if __name__ == '__main__':
    test_microservice()
