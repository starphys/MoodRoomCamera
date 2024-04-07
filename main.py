import boto3
import cv2
from datetime import datetime
from picamera2 import Picamera2
import time

IMG_PATH = './image.png'

class FaceDetector:
    def __init__(self):
        self.classifier = cv2.CascadeClassifier('./cascade.xml')
    
    def detect(self, image):
        pixels = cv2.imread(image)
        faces = self.classifier.detectMultiScale(pixels)
        print(f'Found {len(faces)} faces')
        return len(faces) > 0

class ImageProvider():
    def __init__(self):
        self.camera = Picamera2()
        config = self.camera.create_still_configuration(main={"size": (1920, 1080)})
        self.camera.configure(config)

    def get_image(self):
        self.camera.start()
        time.sleep(2)
        self.camera.capture_file(IMG_PATH)
        self.camera.stop()
        return IMG_PATH

class AWSRekognitionWrapper:
    def __init__(self):
        self.client = boto3.client('rekognition')
    
    def analyze_mood(self, image):
        with open(image, 'rb') as image_file:
            image_data = image_file.read()

        try:
            faces = self.client.detect_faces(Image={'Bytes':image_data}, Attributes=['EMOTIONS'])
            return faces['FaceDetails'][0]['Emotions']
        except:
            return [{'Type': 'FAILED', 'Confidence': 1}]

def main():
    detector = FaceDetector()
    camera = ImageProvider()
    rekognition = AWSRekognitionWrapper()

    while True:
        image_path = camera.get_image()
        if detector.detect(image_path):
            print(rekognition.analyze_mood(image_path)[0]["Type"])
            # Wait a few minutes if mood successfully set
            time.sleep(120)
        time.sleep(5)

main()