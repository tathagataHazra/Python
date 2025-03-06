import cv2
import os

def capture_frames(video_path, output_folder, frames_per_second=1):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return
    
    # Get the frames per second (fps) of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Calculate the interval to capture frames
    frame_interval = int(fps / frames_per_second)
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    frame_count = 0
    saved_frame_count = 0
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Capture a frame at the specified interval
        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_frame_count += 1
        
        frame_count += 1
    
    # Release the video capture object
    cap.release()
    print(f"Finished capturing {saved_frame_count} frames.")

# Example usage
video_path = "input_video.mp4"  # Replace with your video file path
output_folder = "captured_frames"  # Replace with your desired output folder

capture_frames(video_path, output_folder, frames_per_second=2)


def main():
    pass

main()