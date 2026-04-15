# ============================================
# Day 3 - Drowsy Driver Detector
# Face Detection using dlib
# ============================================

import cv2
import dlib
import time

# ── Constants ────────────────────────────────
WINDOW_NAME  = "Drowsy Driver Detector - Day 3"
FRAME_WIDTH  = 640
FRAME_HEIGHT = 480
FPS_FONT     = cv2.FONT_HERSHEY_SIMPLEX

# Colors (BGR format)
GREEN  = (0,   255, 0)
RED    = (0,   0,   255)
YELLOW = (0,   255, 255)
WHITE  = (255, 255, 255)
BLACK  = (0,   0,   0)


# ── Load Face Detector ───────────────────────
def load_detector():
    """Load dlib's face detector."""
    print(" Loading dlib face detector...")
    detector = dlib.get_frontal_face_detector()
    print(" Face detector loaded!")
    return detector


# ── Open Webcam ──────────────────────────────
def open_webcam():
    """Open webcam and return capture object."""
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print(" ERROR: Could not open webcam!")
        return None

    cap.set(cv2.CAP_PROP_FRAME_WIDTH,  FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
    print(" Webcam opened successfully!")
    return cap


# ── Convert to Grayscale ─────────────────────
def to_gray(frame):
    """Convert frame to grayscale for dlib detection."""
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


# ── Detect Faces ─────────────────────────────
def detect_faces(detector, gray_frame):
    """
    Detect faces in grayscale frame.
    Returns list of face rectangles.
    """
    faces = detector(gray_frame, 0)
    return faces


# ── Draw Face Box ────────────────────────────
def draw_face_box(frame, face, face_num):
    """
    Draw a green rectangle around detected face.
    Also shows face coordinates.
    """
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()

    # Draw green rectangle around face
    cv2.rectangle(frame, (x1, y1), (x2, y2), GREEN, 2)

    # Draw face label above rectangle
    label = f"Face {face_num}"
    cv2.putText(frame, label,
                (x1, y1 - 10),
                FPS_FONT, 0.6,
                GREEN, 2)

    # Draw corner dots for style
    dot_size = 6
    cv2.circle(frame, (x1, y1), dot_size, GREEN, -1)
    cv2.circle(frame, (x2, y1), dot_size, GREEN, -1)
    cv2.circle(frame, (x1, y2), dot_size, GREEN, -1)
    cv2.circle(frame, (x2, y2), dot_size, GREEN, -1)

    return frame, (x1, y1, x2, y2)


# ── Draw Info Bar ────────────────────────────
def draw_info(frame, fps, face_count, frame_count):
    """Draw info bar at top and bottom of frame."""

    # Top black bar
    cv2.rectangle(frame, (0, 0),
                  (FRAME_WIDTH, 55), BLACK, -1)

    # Title
    cv2.putText(frame,
                "Drowsy Driver Detector",
                (10, 20),
                FPS_FONT, 0.6, GREEN, 2)

    # FPS
    cv2.putText(frame,
                f"FPS: {fps:.1f}",
                (10, 45),
                FPS_FONT, 0.5, YELLOW, 1)

    # Frame count
    cv2.putText(frame,
                f"Frame: {frame_count}",
                (120, 45),
                FPS_FONT, 0.5, YELLOW, 1)

    # Face count
    face_color = GREEN if face_count > 0 else RED
    face_text  = f"Faces: {face_count}"
    cv2.putText(frame,
                face_text,
                (270, 45),
                FPS_FONT, 0.5, face_color, 1)

    # Status
    if face_count > 0:
        status_text  = "FACE DETECTED"
        status_color = GREEN
    else:
        status_text  = "NO FACE"
        status_color = RED

    cv2.putText(frame,
                status_text,
                (380, 45),
                FPS_FONT, 0.5,
                status_color, 1)

    # Bottom bar
    cv2.rectangle(frame,
                  (0, FRAME_HEIGHT - 30),
                  (FRAME_WIDTH, FRAME_HEIGHT),
                  BLACK, -1)

    cv2.putText(frame,
                "Press Q to quit | Day 3/20",
                (10, FRAME_HEIGHT - 10),
                FPS_FONT, 0.45,
                WHITE, 1)

    return frame


# ── Draw No Face Warning ─────────────────────
def draw_no_face_warning(frame):
    """Show warning when no face is detected."""
    cv2.putText(frame,
                "No face detected!",
                (int(FRAME_WIDTH / 2) - 120,
                 int(FRAME_HEIGHT / 2)),
                FPS_FONT, 0.8,
                RED, 2)
    return frame


# ── Calculate FPS ────────────────────────────
def calculate_fps(prev_time):
    """Calculate current FPS."""
    curr_time = time.time()
    fps       = 1 / (curr_time - prev_time + 0.001)
    return fps, curr_time


# ── Main Function ────────────────────────────
def run_face_detector():
    """Main loop for face detection."""

    print("=" * 50)
    print("  Drowsy Driver Detector")
    print("  Day 3 - Face Detection")
    print("=" * 50)

    # Load detector and webcam
    detector = load_detector()
    cap      = open_webcam()

    if cap is None:
        return

    print("\n Instructions:")
    print("  - Look at camera to detect your face")
    print("  - Move around to test detection")
    print("  - Press Q to quit\n")

    frame_count      = 0
    total_detections = 0
    prev_time        = time.time()
    start_time       = time.time()

    # ── Main Loop ───────────────────────────
    while True:

        ret, frame = cap.read()
        if not ret:
            print(" ERROR: Could not read frame!")
            break

        frame_count += 1

        # Flip frame (mirror)
        frame = cv2.flip(frame, 1)

        # Calculate FPS
        fps, prev_time = calculate_fps(prev_time)

        # Convert to grayscale for detection
        gray = to_gray(frame)

        # Detect faces
        faces      = detect_faces(detector, gray)
        face_count = len(faces)

        if face_count > 0:
            total_detections += 1

        # Draw box around each face
        for i, face in enumerate(faces):
            frame, coords = draw_face_box(frame, face, i + 1)

        # Show warning if no face
        if face_count == 0:
            frame = draw_no_face_warning(frame)

        # Draw info bars
        frame = draw_info(frame, fps, face_count, frame_count)

        # Show frame
        cv2.imshow(WINDOW_NAME, frame)

        # Press Q to quit
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("\n Q pressed - closing...")
            break

    # ── Session Summary ──────────────────────
    session_time = time.time() - start_time

    cap.release()
    cv2.destroyAllWindows()

    print("\n" + "=" * 50)
    print(" Session Summary")
    print("=" * 50)
    print(f"  Total frames    : {frame_count}")
    print(f"  Face detected   : {total_detections} frames")
    print(f"  Session time    : {session_time:.1f} seconds")
    detection_rate = (total_detections / max(frame_count, 1)) * 100
    print(f"  Detection rate  : {detection_rate:.1f}%")
    print("\n Day 3 Complete!")


# ── Entry Point ──────────────────────────────
if __name__ == "__main__":
    run_face_detector()
