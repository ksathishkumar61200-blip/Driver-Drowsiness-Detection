from scipy.spatial import distance
from imutils import face_utils
from pygame import mixer
import imutils
import dlib
import cv2
import time

# ------------------ Initialize mixer ------------------ #
mixer.init()
mixer.music.load("music.wav")  # Make sure this file exists

# ------------------ Eye Aspect Ratio ------------------ #
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

# ------------------ Thresholds ------------------ #
EAR_THRESHOLD = 0.25
CONSEC_FRAMES = 20

# ------------------ Load dlib models ------------------ #
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")

# Landmark ranges
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]

# ------------------ Start Webcam ------------------ #
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ ERROR: Could not open webcam")
    exit()

flag = 0
alert_playing = False


# ======================================================
#                 MAIN LOOP
# ======================================================
while True:

    ret, frame = cap.read()

    # -------- FIX: Prevent invalid frame error -------- #
    if not ret or frame is None:
        print("⚠ Frame not captured... retrying")
        time.sleep(0.1)
        continue

    # FIX datatype
    if frame.dtype != 'uint8':
        frame = frame.astype('uint8')

    # Resize + convert
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray, 0)

    for face in faces:
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0

        # Draw eyes
        cv2.drawContours(frame, [cv2.convexHull(leftEye)], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [cv2.convexHull(rightEye)], -1, (0, 255, 0), 1)

        # Drowsiness detection
        if ear < EAR_THRESHOLD:
            flag += 1
            if flag >= CONSEC_FRAMES:
                cv2.putText(frame, "********** ALERT **********",
                            (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, (0, 0, 255), 2)
                if not alert_playing:
                    mixer.music.play(-1)
                    alert_playing = True
        else:
            flag = 0
            if alert_playing:
                mixer.music.stop()
                alert_playing = False

    cv2.imshow("Driver Drowsiness Detection", frame)

    # Quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
mixer.quit()
