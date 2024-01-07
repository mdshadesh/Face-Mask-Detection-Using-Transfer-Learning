# Face-Mask-Detection-Using-Transfer-Learning
Enhancing Public Health: a Better Approach for Face Mask Detection Using Transfer Learning to Prevent Airborne Disease


# Here's a step-by-step guide to running this code on any device:
First Run Traning Project on Code

# Step 1: Install Required Libraries
If you haven't installed the required libraries, open a terminal or command prompt and type:

pip install tensorflow scikit-learn matplotlib numpy opencv-python


# Step 2: Set Up Directory
Ensure you have a directory with images categorized into "with_mask" and "without_mask". Update the DIRECTORY variable in your code to point to this directory:

DIRECTORY = r"path_to_your_directory_containing_images"


# Step 3: Run the Code
Copy the entire code and paste it into a Python environment (like Jupyter Notebook or a Python script).

# Step 4: Execute the Code
Run the code cell by cell or all at once. This will:

### Steps for Face Mask Detection:

1. Load images from the specified directory.
2. Preprocess the images and perform label encoding.
3. Split the data into training and testing sets.
4. Set up data augmentation.
5. Build and compile the model.
6. Train the model.
7. Evaluate the model's performance.
8. Save the trained model and generate plots for training loss and accuracy.


# Step 5: Check Outputs
After running the code, check the following:

Model files saved in your working directory (e.g., "mask_detector.model").
Plots depicting training loss and accuracy ("plot.png").


# Run Main Face Mask Detection Video Code

# Step 1: Install Required Libraries: 
Ensure you have the necessary libraries installed. The code requires TensorFlow, NumPy, imutils, and OpenCV (cv2). You can install them via pip:

pip install tensorflow numpy imutils opencv-python

# Step 2: Download Model Files:

Download the face detector model files (deploy.prototxt and res10_300x300_ssd_iter_140000.caffemodel) from here.
Save the downloaded model files in a folder named face_detector.
# Step 3: Download Mask Detection Model:

Download the face mask detection model (mask_detector.model) or train your own. Ensure the path to this model is correctly specified in the code.

# Step 4: Run the Code:

1. Copy the provided code into a Python environment (e.g., a Python script or a Jupyter Notebook).
2. Update the paths to the face detector model (prototxtPath and weightsPath) and the face mask detection model (maskNet) in the code.
3. Save the changes and run the script.
4. A window should open displaying the webcam feed with predictions regarding whether a person is wearing a mask or not.
5. Press 'q' to exit the program and close the window.

# Step 5: Verify Output:

As the code runs, it will detect faces and predict whether they are wearing masks or not. The console will print whether a mask is detected or not.
