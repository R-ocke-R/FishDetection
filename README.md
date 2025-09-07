# FishDetection

FishDetection is a deep learning project for detecting and identifying fish species from images and videos. This project was initially created for the Smart India Hackathon in 2022 and is now being revisited to improve its functionality and integrate a state-of-the-art YOLOv8 model.

## Story 

This project was born out of my very first hackathon during my undergraduate days in 2022—the Smart India Hackathon. I worked with a team of enthusiastic computer science undergrads, and we set out to create a tool for the Ministry of Fisheries of India. The idea was to develop an application that would help fishermen identify unfamiliar fish species easily. We envisioned a mobile-friendly interface so that anyone, even a child, could upload a picture of a fish and learn about it instantly.

Despite the excitement and the long nights, we faced some (a lot of) technical hurdles and couldn’t connect the backend to the frontend in time, so our project didn't move to the next round. But this project holds a very special place in my heart—not because of the result, but because of what it set in motion. It was the starting point that led me to my very first research assistantship, which later culminated in a published research paper. Along the way, I also met the professor who eventually became my research advisor. Looking back, I realize that so many pivotal events in my academic journey stemmed from this one project.

But this project will always held a special place in my heart. So now, I'm revisiting it with fresh perspective and determination—because it’s not just a hackathon idea, but a project that carved out the paths I'd take.


## Features

* **Deep Learning-Based Fish Detection:** Utilizes a YOLOv8 model for accurate fish detection.
* **Image and Video Processing:** The underlying model can process both static images and video streams.
* **Jupyter Notebooks for Development:** Includes notebooks for model training, fine-tuning, and demonstration.
* **Pre-trained Model:** A pre-trained model is available for immediate use.



## Project Structure
```
FishDetection/
├── configs/
│   └── config.json              # Configuration file for upload location
├── notebooks/
│   ├── Yolo_Finetuning.ipynb    # Notebook for fine-tuning the YOLOv8 model
│   ├── yolo_demo.ipynb          # Notebook for a real-time YOLOv8 demo
│   └── yolo_on_trained_weights.ipynb # Notebook for running inference with trained weights
├── src/
│   ├── app.py                   # Main Flask app for image upload and display
│   ├── app1.py                  # Deep learning model code (to be integrated)
│   └── data_mapping.py          # Script for preparing the dataset
├── static/
│   ├── Results/                 # Example detection results
│   └── Testing Images/          # Example images for testing
├── templates/
│   ├── index.html               # Main page template
│   └── results.html             # Results page template
├── .gitignore
├── LICENSE
└── README.md
```



## Current Usage 🚀

At the moment, there is no graphical user interface (GUI) for this application. To use the fish detection model, you can run the `notebooks/yolo_on_trained_weights.ipynb` Jupyter Notebook on your local system. This notebook will allow you to load the pre-trained model and perform inference on your own images and videos.

## Installation

**Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/FishDetection.git
    cd FishDetection
    ```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

## Here are some examples of the model's output:


<img src="static/Results/Screenshot%202025-09-07%20at%203.37.58%E2%80%AFPM.png" alt="Image from Yolo PreTrained Model" width="600"/>
<img src="static/Results/Screenshot%202025-09-07%20at%203.41.50%E2%80%AFPM.png" alt="Image from Yolo PreTrained Model" width="400"/>


## License
This project is licensed under the MIT License.


## Process 👨‍💻

1.  **State-of-the-Art Research:** I started by researching the best state-of-the-art (SOTA) models for species and image detection. Initially, I was fine-tuning a `yolov8m.pt` model on my dataset.

##### Link to the Dataset I used - https://www.kaggle.com/datasets/sripaadsrinivasan/fish-species-image-data

2.  **Data Mapping:** I created the object dimension map for the fish detection images. For now, I've selected the cropped folder of the dataset and set the entire width and height as the dimensions using the script in `data_mapping.py`.
3.  **Local Fine-Tuning:** I tried fine-tuning on my Mac M4, but only ran one epoch to test the setup without overloading the machine.
4.  **Cloud Training:** I then moved the training to Google Colab to fine-tune the parameters and build the overall system.
    * **Update:** I created and ran the `Yolo_FineTuning.ipynb` file and ran 100 epochs to get the validation loss under 2.5, but I was disconnected from Colab's runtime without saving the model.
5.  **Using a Pre-trained Model:** I am now using a pre-trained model from [YOLO-Fish](https://github.com/tamim662/YOLO-Fish?tab=readme-ov-file), which was trained on the DeepFish and OzFish datasets. The model weights can be found on the GitHub link.
6.  **Inference:** The `yolo_on_trained_weights.ipynb` notebook works like a charm for both image and video detection.
7.  **Further Resources:** For those interested in this problem, here are some excellent resources:
    * **Computer Vision:** [Roboflow](https://roboflow.com/)
    * **Fish Identification API:** [Fishial.ai](https://www.fishial.ai/) offers Fish identification AI models & a Developers REST API.
    * **Fish Recognition Tool:** [Fishial Recognition](https://portal.fishial.ai/search/by-fishial-recognition) is a great tool to detect fish species.

<img src="static/Results/Fishial/Screenshot%202025-09-07%20at%204.34.29%E2%80%AFPM.png" alt="Image from Fishial's portal" width="600"/>


## Future Scope 🚀

The vision for this project is to build a fully functional web application and mobile app. Here is a breakdown of the features that can be planned, inspired from  fishial.ai and the initial problem statement that we had. 

### Flask Application Developemnt

* **Flask Web Application:** Develop a fully functional Flask-powered web application to allow users to upload images and view detection results in their browser.
* **Model Integration:** Integrate the YOLOv8 model with the Flask backend to create a seamless user experience.
* **Deployment:** Deploy the web application to a cloud platform like Heroku or AWS to make it publicly accessible.

### Mid-Term Goals

* **Real-Time Webcam Detection:** Integrate the real-time webcam detection functionality from the basic `yolo_demo.ipynb` notebook into the web application.
* **User Accounts:** Allow users to create accounts to save their detection history and contribute to the dataset.
* **Fish Species Information:** Integrate with an external API (like Fishial.ai) to provide detailed information about the detected fish species.

### Long-Term Goals

* **Mobile Application:** Develop a mobile app for both iOS and Android to make the tool accessible to fishermen in the field.
* **Advanced Features:**
    * **Fish Measurement:** Add a feature to estimate the size and weight of the detected fish.
    * **Disease Detection:** Train the model to identify common diseases in fish.
* **Community Platform:** Create a platform for users to share their fish detections and contribute to the dataset.

## License 📄

This project is licensed under the MIT License.






