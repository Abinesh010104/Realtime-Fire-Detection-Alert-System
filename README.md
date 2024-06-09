# Real-Time Fire Detection Alert System

This project implements a real-time fire detection alert system that sends notifications via Gmail. The system uses the YOLOv8 model for fire detection, and the model was trained on a custom dataset available on Roboflow.

## Features

- Real-time fire detection
- Email alerts through Gmail
- Trained using YOLOv8

## Dataset

The dataset used for training the fire detection model is available on Roboflow:
[Fire Detection Dataset](https://universe.roboflow.com/rehman-2vlay/fire-detection-vdtmc)

## Model Training

The model was trained using Google Colab. You can find the Colab notebook for training the model here:
[Colab Link for Model Training](https://colab.research.google.com/drive/1HsN9hWnCCvWN5OvMSNLjcFR2wRtuiVit?usp=sharing)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/fire-detection-alert-system.git
    cd fire-detection-alert-system
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Model Inference**:

    - Ensure you have the trained YOLOv8 model weights saved in the project directory.
    - Update the `model_path` variable in the `Main.py` script to point to your model weights.

2. **Email Configuration**:

    - Update the email configuration section in the `Main.py` script with your Gmail credentials and recipient details.

3. **Run the Script**:

    ```bash
    python Main.py
    ```

    The script will start the fire detection process and send an alert email if fire is detected.

## File Descriptions

- `Main.py`: The main script to run the fire detection and email alert system.
- `requirements.txt`: Contains the list of dependencies required to run the project.

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- [Roboflow](https://roboflow.com) for providing the dataset.
- [Ultralytics](https://ultralytics.com) for the YOLOv8 model.

