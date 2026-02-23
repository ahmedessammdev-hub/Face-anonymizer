import cv2
import numpy as np

def get_bbox_pixels(bbox, frame_shape):
    h, w = frame_shape[:2]

    xmin = int(bbox.xmin * w)
    ymin = int(bbox.ymin * h)
    box_width = int(bbox.width * w)
    box_height = int(bbox.height * h)

    xmax = xmin + box_width
    ymax = ymin + box_height

    # Clamp
    xmin = max(0, xmin)
    ymin = max(0, ymin)
    xmax = min(w, xmax)
    ymax = min(h, ymax)

    return xmin, ymin, xmax, ymax


def anonymize_face(frame, xmin, ymin, xmax, ymax, method="black"):
    face = frame[ymin:ymax, xmin:xmax]

    if face.size == 0:
        return frame

    if method == "black":
        frame[ymin:ymax, xmin:xmax] = 0

    elif method == "blur":
        blurred = cv2.GaussianBlur(face, (51, 51), 0)
        frame[ymin:ymax, xmin:xmax] = blurred

    elif method == "pixelate":
        small = cv2.resize(face, (16, 16), interpolation=cv2.INTER_LINEAR)
        pixelated = cv2.resize(small, (xmax - xmin, ymax - ymin), interpolation=cv2.INTER_NEAREST)
        frame[ymin:ymax, xmin:xmax] = pixelated

    return frame


def draw_bounding_box(frame, xmin, ymin, xmax, ymax, confidence):
    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0,255,0), 2)
    cv2.putText(frame, f"{confidence:.2f}",
                (xmin, ymin-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0,255,0),
                2)
    return frame