# 🪄 Harry Potter's Invisible Cloak using OpenCV  

This project recreates the **Harry Potter Invisible Cloak** effect using **OpenCV** in Python. By detecting a specific color (black in this case), the program replaces it with a pre-captured background, making the person appear "invisible."  

## 🎥 Demo  
*(Add a GIF or screenshot of the effect in action)*  

## 📌 Features  
✅ Detects **black color** and makes it invisible.  
✅ Uses **background subtraction** to replace black-colored areas with a captured background.  
✅ **Real-time processing** using OpenCV.  
✅ Works with any **webcam**.  

## ⚙️ Installation  
## 1️⃣ Clone the Repository  

`git clone https://github.com/letsconfuse/cloak.git`

`cd invisible-cloak`

## 2️⃣ Install Dependencies

Ensure you have Python installed, then install OpenCV and NumPy:

`pip install opencv-python numpy`

## 3️⃣ Run the Script

`python main.py`

# 🛠 How It Works

The program captures 30 frames of the background at the start.
It detects black-colored objects in the frame.
The detected black areas are replaced with the pre-captured background.
The rest of the scene remains unchanged, creating the invisibility effect.

#🎭 How to Use

Wear black clothes or cover yourself with a black cloth.
Ensure the background is not black (otherwise, it will also disappear).
Run the program and enjoy the magic!
Press "Q" to exit.

#📌 Possible Improvements

Add support for custom colors (instead of only black).
Improve edge detection to reduce noise.
Enhance performance using multi-threading.

##👨‍💻 Contributing

Want to improve this project? Contributions are welcome! Feel free to open issues or submit pull requests.
