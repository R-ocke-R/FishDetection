# FishDetection

FishDetection is a web application for detecting fish species using deep learning models built with TensorFlow and Keras.

## Features

- Deep learning-based fish detection and classification
- Flask-powered web front-end for image upload and results display
- RESTful API for backend communication
- Model training and inference scripts included

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/FishDetection.git
    cd FishDetection
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the backend server:
    ```bash
    python backend/app.py
    ```
2. Start the Flask front-end:
    ```bash
    python frontend/app.py
    ```
3. Open your browser and go to `http://localhost:5000` to use the app.

## Project Structure

```
FishDetection/
├── backend/
│   ├── app.py
│   ├── model/
│   └── utils.py
├── frontend/
│   ├── app.py
│   └── templates/
├── requirements.txt
└── README.md
```

## Known Issues

- Backend and frontend connection may require CORS configuration.
- Jupyter notebook for deep learning was removed due to compatibility issues.

## License

MIT License