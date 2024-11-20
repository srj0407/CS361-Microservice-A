# CS361-Microservice-A

# Image Microservice

## Description
This microservice provides endpoints for uploading images with metadata and retrieving them based on tags. The tags need to be fed into the microservice themselves. They will not be grabbed by the microservice.

## Communication Contract
1. **Request Data**: Use `POST /uploadImage` to upload an image with metadata.
   - Example:
     ```python
     import requests
     response = requests.post(
         "http://127.0.0.1:5000/uploadImage",
         json={
             "uploader_name": "John Doe",
             "image": "<base64-encoded-image>",
             "tags": ["nature", "sunset"]
         }
     )
     print(response.json())
     ```
2. **Receive Data**: Use `GET /returnImage` to retrieve images based on tags.
   - Example:
     ```python
     import requests
     response = requests.get(
         "http://127.0.0.1:5000/returnImage",
         json={"taglist": ["nature"]}
     )
     print(response.json())
     ```

## Sequence Diagram
```plaintext
Client -> Microservice: POST /uploadImage
Microservice -> Storage: Save ImageDetails.JSON
Client -> Microservice: GET /returnImage with {tags}
Microservice -> Client: Return images with matching tags
