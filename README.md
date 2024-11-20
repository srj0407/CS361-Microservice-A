# CS361-Microservice-A

# Image Microservice

## Description
This microservice provides endpoints for uploading images with metadata and retrieving them based on tags. The tags need to be fed into the microservice themselves. They will not be grabbed by the microservice. This uplaods images encoded in Base64 format along with metadata such as uploader name, date, and the aformentioned tags. This microservice will also retrieve images based on associated tags. This software uses *Flask* for all backend functionality and stores the image metadata in memory. This microservices is only suitable for small scale applications.

## Set-Up Instructions
1. **Make sure you are running Python 3.6 or later**
     -You can check what version of Python you are running by typing 
       ```python
         python --version
       ```
      into the console.
2. **Install all Dependancies**
      ```python
      pip intall flask requests pillow
      ```
3. **clone the repository or download the code files**
      ```bash
      git clone <repository-url>
      cd <repository-folder>
      ```
4. **Run the Microservice**
   ```python
   python image_microservice.py
```
   Flask will start a dev server at http://127.0.0.1:5000, this can be changed to any other server you need.
   The Microservice is now ready to use.

## **How to Use**

### **Endpoints**
1. **Upload an Image**:
   - **URL**: `POST /uploadImage`
   - **Request Body** (JSON):
     ```json
     {
       "uploader_name": "John Doe",
       "image": "<base64_encoded_image>",
       "tags": ["tag1", "tag2"]
     }
     ```
   - **Response** (Success):
     ```json
     {
       "message": "Image uploaded successfully!"
     }
     ```
   - **Example**:
     ```python
     import requests
     import base64

     with open("test_image.jpg", "rb") as img_file:
         encoded_image = base64.b64encode(img_file.read()).decode('utf-8')

     response = requests.post(
         "http://127.0.0.1:5000/uploadImage",
         json={
             "uploader_name": "John Doe",
             "image": encoded_image,
             "tags": ["nature", "sunset"]
         }
     )
     print(response.json())
     ```

2. **Retrieve Images by Tags**:
   - **URL**: `GET /returnImage`
   - **Request Body** (JSON):
     ```json
     {
       "taglist": ["tag1", "tag2"]
     }
     ```
   - **Response** (Success):
     ```json
     [
       {
         "uploader_name": "John Doe",
         "upload_date": "2024-11-19 15:32:10",
         "tags": ["tag1", "tag2"],
         "image": "<base64_encoded_image>"
       }
     ]
     ```
   - **Example**:
     ```python
     import requests

     response = requests.get(
         "http://127.0.0.1:5000/returnImage",
         json={"taglist": ["nature"]}
     )
     print(response.json())
     ```

## **Sample Workflow**

1. Start the microservice by running:
   ```bash
   python image_microservice.py
   ```

2. Use the test program `test_microservice.py` to:
   - Upload a test image.
   - Retrieve images using tags.

   Example:
   ```bash
   python test_microservice.py
   ```

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
