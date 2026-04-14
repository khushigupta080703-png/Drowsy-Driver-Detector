# ============================================
# Day 2 - Drowsy Driver Detector
# Webcam Feed using OpenCV
# ============================================

import cv2
import time

# ── Constants ────────────────────────────────
WINDOW_NAME = "Drowsy Driver Detector - Day 2"
FRAME_WIDTH  = 640
FRAME_HEIGHT = 480
FPS_FONT     = cv2.FONT_HERSHEY_SIMPLEX

def open_webcam():
    """Open the webcam and return the capture object."""
    cap = cv2.VideoCapture(0)  # 0 = default webcam

    if not cap.isOpened():
        print(" ERROR: Could not open webcam!")
        print(" Make sure your webcam is connected.")
        return None

    # Set resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,  FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    print(" Webcam opened successfully!")
    print(f" Resolution: {FRAME_WIDTH}x{FRAME_HEIGHT}")
    print(" Press Q to quit")
    return cap


def calculate_fps(prev_time):
    """Calculate frames per second."""
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time + 0.001)
    return fps, curr_time


def draw_info(frame, fps, frame_count):
    """Draw FPS and frame info on the video frame."""

    # Background bar at top
    cv2.rectangle(frame, (0, 0), (FRAME_WIDTH, 50),
                  (0, 0, 0), -1)

    # Title text
    cv2.putText(frame,
                "Drowsy Driver Detector",
                (10, 20),
                FPS_FONT, 0.6,
                (0, 255, 0), 2)

    # FPS counter
    cv2.putText(frame,
                f"FPS: {fps:.1f}",
                (10, 42),
                FPS_FONT, 0.5,
                (255, 255, 0), 1)

    # Frame counter
    cv2.putText(frame,
                f"Frame: {frame_count}",
                (200, 42),
                FPS_FONT, 0.5,
                (255, 255, 0), 1)

    # Status: AWAKE (will change in Day 6)
    cv2.putText(frame,
                "STATUS: AWAKE",
                (380, 42),
                FPS_FONT, 0.5,
                (0, 255, 0), 1)

    # Instructions at bottom
    cv2.rectangle(frame,
                  (0, FRAME_HEIGHT - 30),
                  (FRAME_WIDTH, FRAME_HEIGHT),
                  (0, 0, 0), -1)

    cv2.putText(frame,
                "Press Q to quit | Day 2/20",
                (10, FRAME_HEIGHT - 10),
                FPS_FONT, 0.45,
                (200, 200, 200), 1)

    return frame


def run_webcam():
    """Main function to run the webcam feed."""

    print("=" * 50)
    print(" Drowsy Driver Detector")
    print(" Day 2 - Webcam Feed")
    print("=" * 50)

    # Open webcam
    cap = open_webcam()
    if cap is None:
        return

    frame_count = 0
    prev_time   = time.time()

    # ── Main Loop ───────────────────────────
    while True:
        # Read frame from webcam
        ret, frame = cap.read()

        # If frame not read correctly
        if not ret:
            print(" ERROR: Could not read frame!")
            break

        frame_count += 1

        # Calculate FPS
        fps, prev_time = calculate_fps(prev_time)

        # Flip frame horizontally (mirror effect)
        frame = cv2.flip(frame, 1)

        # Draw info on frame
        frame = draw_info(frame, fps, frame_count)

        # Show the frame in a window
        cv2.imshow(WINDOW_NAME, frame)

        # Press Q to quit
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("\n Q pressed - closing webcam...")
            break

    # ── Cleanup ─────────────────────────────
    cap.release()
    cv2.destroyAllWindows()

    print(f"\n Session Summary:")
    print(f"   Total frames captured: {frame_count}")
    print(f"   Average FPS: {frame_count / max(time.time() - prev_time, 1):.1f}")
    print(" Day 2 Complete!")


# ── Entry Point ──────────────────────────────
if __name__ == "__main__":
    run_webcam()
