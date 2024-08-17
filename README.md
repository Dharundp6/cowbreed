# cowbreed
# Indian Bovine Breed Detectio

This project aims to detect and classify 32 different breeds of Indian bovines (cattle and buffalo) using the YOLOv8 object detection model. The model is trained on a dataset of bovine images and deployed using Gradio for easy interaction and testing.

## Dataset

The dataset used for training and validation consists of images of 32 Indian bovine breeds. The images were collected from various sources and manually annotated using smart polygons to accurately label the bovine regions in each image.

To enhance the dataset and improve the model's robustness, data augmentation techniques were applied. These techniques include:

- Rotation
- Flipping
- Scaling
- Brightness adjustment
- Contrast adjustment

The augmented dataset provides a more diverse set of images for training, helping the model generalize better to unseen data.

## Model Architecture

The breed detection model is based on the YOLOv8 architecture, which is a state-of-the-art object detection model known for its high accuracy and real-time performance. YOLOv8 is an improvement over its predecessors, offering better speed and accuracy trade-offs.

The YOLOv8 model was trained on the augmented dataset using the appropriate input size and anchor box configuration. The model learns to predict the bounding boxes and class probabilities for each breed in the input image.

## Training

The YOLOv8 model was trained using the annotated dataset, with the images and their corresponding bounding box annotations. The training process involved optimizing the model's parameters using a suitable loss function and optimizer.

The training hyperparameters, such as batch size, learning rate, and number of epochs, were carefully tuned to achieve the best performance on the validation set.

## Deployment

To make the trained YOLOv8 model accessible and easy to use, it has been deployed using Gradio. Gradio is a Python library that allows creating interactive web interfaces for machine learning models with just a few lines of code.

The Gradio interface provides a user-friendly way to upload an image of a bovine and get the predicted breed and bounding box coordinates as the output. The interface also displays the confidence score associated with each prediction.

## Usage

To use the deployed Indian Bovine Breed Detection model:

1. Install the required dependencies mentioned in the `requirements.txt` file.
2. Run the Gradio script using the command: `python app.py`.
3. Access the Gradio interface through the provided URL.
4. Upload an image of a bovine and click the "Predict" button.
5. The interface will display the predicted breed, bounding box coordinates, and confidence score.

## Future Improvements

Some potential improvements for this project include:

- Expanding the dataset with more diverse images of Indian bovine breeds.
- Fine-tuning the YOLOv8 model with additional data to improve its performance.
- Exploring other object detection architectures and comparing their performance with YOLOv8.
- Enhancing the Gradio interface with more features and visualizations.

Feel free to contribute to this project by submitting pull requests or opening issues on the GitHub repository.

