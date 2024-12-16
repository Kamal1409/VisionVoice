# VisionVoice - Object Recognition to Speech  

**VisionVoice** is an innovative application that leverages **YOLO (You Only Look Once)** object detection to recognize objects in real time and convert their names into speech output. This project is designed to assist visually impaired individuals by providing auditory information about their surroundings.

---

## Features  

- **Real-Time Object Detection**: Uses the YOLO model to identify objects in the camera feed.  
- **Text-to-Speech Conversion**: Converts detected object names into spoken words.  
- **User-Friendly Interface**: Simple and easy to use, aimed at improving accessibility for visually impaired users.  
- **Customizable**: Easily extendable to include more objects or additional features.  

---

## How It Works  

1. **Object Detection**:  
   - The application uses a pre-trained YOLO model to detect objects in real time from the camera feed.  
   - The YOLO model processes frames and identifies objects with high accuracy and speed.  

2. **Text-to-Speech Conversion**:  
   - Once objects are recognized, their names are passed to a text-to-speech engine.  
   - The TTS engine converts text into audio, which is played through the device's speakers.  

3. **Auditory Feedback**:  
   - The device provides immediate voice output to inform the user about detected objects.  

---

## Installation  

### Prerequisites  

- Python 3.7 or higher  
- A compatible GPU (optional but recommended for real-time performance)  
- Required libraries (detailed below)  

### Steps  

1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/VisionVoice.git
   cd VisionVoice
