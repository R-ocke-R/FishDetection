# FishDetection

FishDetection is a web application for detecting fish species from a user uploaded image using deep learning models built with TensorFlow and Keras. The app provides a simple web interface for uploading fish images and viewing detection results.


## Features

- Deep learning-based fish detection and classification
- Flask-powered web front-end for image upload and results display
- Easy configuration via `config.json`
- Ready-to-use HTML templates for upload and results

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/FishDetection.git
    cd FishDetection
    ```

2. **Install dependencies:**
    ```bash
    pip install flask tensorflow
    ```

3. **Set up the upload folder:**
    - Make sure the folder specified in `config.json` (default: `/Users/manu/Master/FishDetection/static`) exists.
    - If needed, update the path in `config.json` to match your system.

## Usage

1. **Start the Flask app:**
    ```bash
    python app.py
    ```
2. **Open your browser and go to** `http://localhost:5000` **to use the app.**
    - Upload a fish image.
    - View the uploaded image and detection result.

## Project Structure

```
FishDetection/
├── app.py               # Main Flask app for image upload and display
├── app1.py              # Deep learning model code (to be merged with app.py for full functionality)
├── config.json          # Configuration file for upload location
├── __init__.py          # Package marker (empty)
├── templates/
│   ├── index1.html      # Upload page template
│   └── index2.html      # Results page template
```


## Known Issues

- The deep learning model is not currently integrated with the main Flask app.
- The upload path in `config.json` may need to be changed for your operating system.
- Only one image (`123.jpg`) is handled at a time; uploading a new image will overwrite the previous one.

## License

MIT

## Story 

This project was born out of my very first hackathon during my undergraduate days in 2022—the Smart India Hackathon. I led a team of enthusiastic computer science undergrads, and we set out to create a tool for the Ministry of Fisheries of India. The idea was to develop an application that would help fishermen identify unfamiliar fish species easily. We envisioned a mobile-friendly interface so that anyone, even a child, could upload a picture of a fish and learn about it instantly.

Despite the excitement and the long nights, we faced some technical hurdles and couldn’t connect the backend to the frontend in time, so we didn’t win the hackathon. But this project holds a very special place in my heart—not because of the result, but because of what it set in motion. It was the starting point that led me to my very first research assistantship, which later culminated in a published research paper. Along the way, I also met the professor who eventually became my research advisor. Looking back, I realize that so many pivotal events in my academic journey stemmed from this one project.

But this project will always held a special place in my heart. So now, I'm revisiting it with fresh perspective and determination—because it’s not just a hackathon idea, but a project that shaped who I became as a researcher.