import cv2

def main():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Let the user select the object to track
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        return

    bbox = cv2.selectROI("Select Object", frame, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow("Select Object")

    if bbox == (0, 0, 0, 0):  # If no object is selected
        print("Error: No object selected.")
        return

    # Initialize the CSRT tracker
    tracker = cv2.TrackerCSRT_create()
    tracker.init(frame, bbox)

    # Tracking parameters
    tracking_status = "Tracking..."
    lost_frames = 0
    last_valid_bbox = bbox  # Store the last valid bounding box

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Warning: Could not read frame. Retrying...")
            cap.release()
            cap = cv2.VideoCapture(0)  # Reinitialize the webcam
            cv2.waitKey(1000)  # Wait for 1 second before retrying
            continue

        # Update the tracker
        success, bbox = tracker.update(frame)

        if success:
            # Draw bounding box if tracking is successful
            x, y, w, h = [int(v) for v in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            tracking_status = "Tracking..."
            lost_frames = 0
            last_valid_bbox = bbox  # Update the last valid bounding box
        else:
            # Increment lost frames counter
            lost_frames += 1
            if lost_frames > 5:
                tracking_status = "Lost tracking!"
                # Reinitialize the tracker with the last valid bounding box
                tracker = cv2.TrackerCSRT_create()
                tracker.init(frame, last_valid_bbox)

        # Display status text
        cv2.putText(
            frame,
            tracking_status,
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255) if "Lost" in tracking_status else (0, 255, 0),
            2,
        )

        # Show the frame
        cv2.imshow("Live Object Tracking", frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()