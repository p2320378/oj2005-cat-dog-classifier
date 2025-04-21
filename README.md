

# Cat-Dog Image Classifier 🐱 vs 🐶


<img width="518" alt="eb74ac3b3228dd65686b976d9e52e63" src="https://github.com/user-attachments/assets/942a87bf-fa72-43fa-964a-2ba3e532e058" />

https://github.com/user-attachments/assets/5da4bcc5-61b4-48f6-81f2-ef56c8539b88

## Project Structure
.
├── .gitignore
├── .vercelignore
├── app.py # Flask web application
├── model.py # PyTorch CNN model
├── requirements.txt # Python dependencies
└── vercel.json # Vercel deployment config


## Purpose of the Software

### Development Process
- Agile Methodology was chosen because:
  - Allows for iterative improvements to the model
  - Enables rapid response to user feedback
  - Better suited for machine learning projects requiring frequent testing

### Target Market
- Pet-related mobile applications: Enhance user experience by providing pet identification features.
- Veterinary clinics for patient categorization: Automate patient categorization for cats and dogs.
- Animal shelter management systems: Streamline animal intake processes.
- Educational tools for machine learning: Serve as a beginner-friendly project for ML studies.

## Software Development Plan

### Development Process

1.**Requirements Gathering** (Day 1)
Identify the scope of the classifier: binary classification (cat vs. dog).
Choose a lightweight yet accurate convolutional neural network (CNN) architecture for deployment.
Collect a labeled dataset of cat and dog images (e.g., Kaggle’s Dog vs. Cat dataset).
Perform data preprocessing:
Resize images to a consistent shape (e.g., 224x224 pixels).
Normalize pixel values and apply augmentations (flip, rotate, crop) to improve generalization.

2. **Model Development** (Days 2-3)
Build a CNN model using PyTorch:
Use convolutional layers for feature extraction.
Add dropout and batch normalization for regularization.
Design fully connected layers for classification.
Train the model on the prepared dataset and optimize using cross-entropy loss.
Evaluate the model’s accuracy on a validation dataset.

3. **Web Interface Implementation** (Day 4)
Develop a simple Flask web application:
Allow users to upload an image via a user-friendly interface.
Pass the image to the pre-trained CNN model for prediction.
Display the result (cat/dog) along with probabilities.

4. **Testing & Validation** (Day 5)
Conduct unit tests for each module (e.g., image preprocessing, model inference).
Perform end-to-end testing of the web application with various test images.
Validate model accuracy using additional test datasets.

5. **Deployment** (Days 6-8)
Containerize the application using Docker for consistent deployment.
Deploy the web app to Vercel for scalable hosting.
Ensure the app is mobile-friendly with responsive design.
6.**Post-deployment Monitoring**(Ongoing)
Gather user feedback and monitor server performance.
Optimize model performance based on real-world usage.
## Future Roadmap 🚀
### Short-term (Next 2 weeks)
 Expand to 10 common pet categories (birds, rabbits, etc.)
 Implement breed identification within species
 Add age estimation feature
 Mobile-friendly responsive design

### Long-term
 Wildlife recognition module
 Behavior analysis through video
 Integration with veterinary databases
 AR overlay for real-time identification

### Team Members
<img width="677" alt="ceabaa5e456563be08f141026e9bced" src="https://github.com/user-attachments/assets/c8751f98-bd23-4b9d-96a7-b9e6089fa699" />



### Schedule
<img width="1164" alt="2fe6365514a12455dd0f3510238440b" src="https://github.com/user-attachments/assets/6ebbe6d2-0daa-45b4-a89c-285518759915" />


## Technical Implementation

### Algorithm
```python
class CatDogNet(nn.Module):
    def __init__(self):
        super(CatDogNet, self).__init__()
        # 3 Convolutional Blocks with increasing channels (32→64→128)
        self.conv1 = nn.Sequential(...)
        self.conv2 = nn.Sequential(...)
        self.conv3 = nn.Sequential(...)
        
        # Fully Connected Layers
        self.fc = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128*28*28, 512),  # Feature transformation
            nn.ReLU(),
            nn.Dropout(0.5),  # Regularization
            nn.Linear(512, 2)  #



git clone https://github.com/oj2005/oj2005-cat-dog-classifier.git
pip install -r requirements.txt
python app.py

{
  "result": "cat|dog",
  "cat_probability": 0.85,
  "dog_probability": 0.15
}


Key features of this README:
1. **Graphical Abstract** 
2. Clear development methodology explanation
3. Detailed project timeline and team structure
4. Algorithm documentation with code highlighting
5. Current/Future status sections with checkboxes
6. Quick start guide for new users



