import cv2

# Load pre-trained Haarcascades for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load pre-trained models for age and gender prediction
age_net = cv2.dnn.readNet("age_deploy.prototxt", "age_net.caffemodel")
gender_net = cv2.dnn.readNet("deploy_gender.prototxt", "gender_net.caffemodel")

# Function to get age and gender from face
def get_age_and_gender(face):
    blob = cv2.dnn.blobFromImage(face, scalefactor=1.0, size=(227, 227), mean=(78.4263377603, 87.7689143744, 114.895847746), swapRB=False)
    
    # Predict age
    age_net.setInput(blob)
    age_preds = age_net.forward()
    age = int(age_preds[0].argmax())

    # Predict gender
    gender_net.setInput(blob)
    gender_preds = gender_net.forward()

    # Check if gender_preds has more than one element along axis 0
    if gender_preds.shape[0] > 1:
        gender = "Male" if gender_preds[0][0] > gender_preds[1][0] else "Female"
    else:
        gender = "Male" if gender_preds[0][0] > 0.5 else "Female"

    return age, gender

# Open the webcam
video_capture = cv2.VideoCapture(1)

while True:
    # Capture each frame from the webcam
    ret, frame = video_capture.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extract the face from the frame
        face = frame[y:y+h, x:x+w]

        # Get age and gender
        age, gender = get_age_and_gender(face)

        # Draw rectangle and display age and gender
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        label = f"Age: {age}, Gender: {gender}"
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
video_capture.release()
cv2.destroyAllWindows()
