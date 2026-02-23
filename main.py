import cv2
import mediapipe as mp
import numpy as np
from utils import get_bbox_pixels, anonymize_face, draw_bounding_box
# Load video
video_path='./Test Data/test video.mp4'
cap = cv2.VideoCapture(video_path)
fps=cap.get(cv2.CAP_PROP_FPS)

# Initialize face detection
mp_face_detection = mp.solutions.face_detection
with mp_face_detection.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.6
) as face_detection:

    while True:
        # Read frame
        ret, frame = cap.read()
        if not ret:
            break
        # Resize frame
        frame=cv2.resize(frame,(640,480))
       
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(rgb)
        # Process frame
        if results.detections :   
            for detection in results.detections:
                bbox=detection.location_data.relative_bounding_box
                # Get face pixels
                xmin, ymin, xmax, ymax = get_bbox_pixels(bbox, frame.shape)
                # Anonymize face 
                frame = anonymize_face(frame, xmin, ymin, xmax, ymax, method="blur")    
                frame = draw_bounding_box(frame, xmin, ymin, xmax, ymax, detection.score[0])
        cv2.imshow("Face Detection", frame)

        if cv2.waitKey(int(1000/fps)) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()