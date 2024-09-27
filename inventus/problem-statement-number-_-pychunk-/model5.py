import cv2  # pip install opencv-python
from deepface import DeepFace  # pip install deepface

model = input("please enter your name ")


# Load the pre-trained face detection model
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture from the webcam
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

first_emotion_printed = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Analyze the frame for emotions with enforce_detection set to False
    results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangles around detected faces and display emotions
    for (x, y, w, h), result in zip(faces, results):
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        emotion = result['dominant_emotion']
        cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
        
        # Print the first recognized emotion and break the loop
        if not first_emotion_printed:
            print("hey",model,"you have a really beautiful face ")
            print(f"it seems like you are in a  {emotion} state")
            if emotion == 'happy':
                print('''here is happy and chill song playlist
                    https://www.bing.com/search?showselans=1&IG=5B9B0A52ADD34A5BA420DD9EF3F9A377&IID=SERP.9999&cw=1266&ch=631&dissrchswrite=1&lightschemeovr=1&kseed=10000&SFX=7&partnerId=bingchat&tone=Balanced&q=youtube+playlist+for+happy+music&iframeid=628cd332-1bbe-44a7-b92c-e614cda38c60#''')
            elif emotion == 'sad':
                print(''''here is sad song playlist that will cheer you 
                     https://www.bing.com/search?showselans=1&IG=5B9B0A52ADD34A5BA420DD9EF3F9A377&IID=SERP.9999&cw=1266&ch=631&dissrchswrite=1&lightschemeovr=1&kseed=12500&SFX=12&partnerId=bingchat&tone=Balanced&q=playlist+to+lift+you+up&iframeid=a1cd1686-849e-44e1-b4dd-f68f95a932bc#''')
            elif emotion == 'neutral':
                print(''' here is your playlist that will make u super happy
                    https://www.bing.com/search?showselans=1&IG=5B9B0A52ADD34A5BA420DD9EF3F9A377&IID=SERP.9999&cw=1266&ch=631&dissrchswrite=1&lightschemeovr=1&kseed=12500&SFX=12&partnerId=bingchat&tone=Balanced&q=playlist+to+lift+you+up&iframeid=a1cd1686-849e-44e1-b4dd-f68f95a932bc#''')
            elif emotion == 'angry':
                print('''here is your playlist 
                      https://www.bing.com/search?showselans=1&IG=5B9B0A52ADD34A5BA420DD9EF3F9A377&IID=SERP.9999&cw=1266&ch=631&dissrchswrite=1&lightschemeovr=1&kseed=15000&SFX=17&partnerId=bingchat&tone=Balanced&q=heavy+metal+playlist&iframeid=ff733d2e-2b16-456f-89ad-d39ee61df8c6#''')
            elif emotion == 'fear':
                print('''here is your playlist 
                      https://www.bing.com/search?showselans=1&IG=5B9B0A52ADD34A5BA420DD9EF3F9A377&IID=SERP.9999&cw=1266&ch=631&dissrchswrite=1&lightschemeovr=1&kseed=15000&SFX=17&partnerId=bingchat&tone=Balanced&q=heavy+metal+playlist&iframeid=ff733d2e-2b16-456f-89ad-d39ee61df8c6#''')
            first_emotion_printed = True
            break
            first_emotion_printed = True
            break

    # Display the frame with detected faces and emotions
    cv2.imshow('Face Emotion Recognition', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
