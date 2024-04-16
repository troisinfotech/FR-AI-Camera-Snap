from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import cv2
import base64
import requests
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import cv2
import base64
import requests
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

class CameraLink(BaseModel):
    link: str

@app.post("/process_camera_link")
async def process_camera_link(camera_link: CameraLink):
    rtsp_link = camera_link.link
    cap = cv2.VideoCapture(rtsp_link)
    if not cap.isOpened():
        raise HTTPException(status_code=500, detail="Error opening camera stream")
    ret, frame = cap.read()
    if not ret:
        raise HTTPException(status_code=500, detail="Error reading frame from camera stream")
    
    # Resize the frame to 720p
    frame = cv2.resize(frame, (1280, 720))  # Assuming 1280x720 is 720p
    
    cv2.imwrite("captured_image.jpg", frame)
    cap.release()
    with open("captured_image.jpg", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_image

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
    allow_methods=["POST"],
    allow_headers=["*"],
)

class CameraLink(BaseModel):
    link: str

@app.post("/process_camera_link")
async def process_camera_link(camera_link: CameraLink):
    rtsp_link = camera_link.link
    cap = cv2.VideoCapture(rtsp_link)
    if not cap.isOpened():
        raise HTTPException(status_code=500, detail="Error opening camera stream")
    ret, frame = cap.read()
    if not ret:
        raise HTTPException(status_code=500, detail="Error reading frame from camera stream")
    
    # Resize the frame to 720p
    frame = cv2.resize(frame, (1280, 720))  # Assuming 1280x720 is 720p
    
    cv2.imwrite("captured_image.jpg", frame)
    cap.release()
    with open("captured_image.jpg", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_image

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
