import cv2
import os

def capture_images(output_folder, num_images):
    # Open the default camera 
    camera = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not camera.isOpened():
        print("Unable to access camera")
        return

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop to capture images
    for i in range(num_images):
        ret, frame = camera.read()
        if not ret:
            print("Failed to capture image")
            break

        # Save the image
        image_name = f"image_{i + 1}.jpg"
        image_path = os.path.join(output_folder, image_name)
        cv2.imwrite(image_path, frame)

        print(f"Image {i + 1} captured")

    # Release the camera
    camera.release()
    cv2.destroyAllWindows()

# Specify the output folder and number of images to capture
output_folder = "Music\Thesis_paper\autoimagecal"
num_images = 20

# Call the function to capture images
capture_images(output_folder, num_images)
