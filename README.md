# Generation-and-detection-of-face-morphing-attacks
Introduction
This project aims to develop a robust system for detecting face morphing attacks in facial recognition and authentication systems. Face morphing attacks involve combining images of multiple individuals to deceive recognition systems. This README provides an overview of the project, its objectives, features, installation instructions, and usage guidelines.
## Features
- Face morphing detection using:
  - Convolutional Neural Networks (CNNs)
  - Support Vector Machines (SVMs)
- Image preprocessing techniques for enhancing detection accuracy
- Integration with existing facial recognition systems
- User-friendly interface for uploading and analyzing images
- 
## Installation

1. Clone the repository: git clone https://github.com/yourusername/face-morphing-detection.git

2. Install dependencies:
   
pip install -r requirements.txt
pip install opencv-contrib-python
pip install mysqlclient
pip install PyWavelets
pip install scikit-iamge

3. Run the application:

python manage.py makemigrations
python mange.py migrate
python manage.py runserver


## Usage

1. Upload an image to the system.
2. The system will analyze the image and determine if it's a clean image or a morphed image.
3. View the analysis results and take appropriate action.

## Contributing

Contributions are welcome! If you have any ideas for improvements, bug fixes, or new features
