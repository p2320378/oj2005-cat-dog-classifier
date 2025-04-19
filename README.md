

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
- Pet-related mobile applications
- Veterinary clinics for patient categorization
- Animal shelter management systems
- Educational tools for machine learning

## Software Development Plan

### Development Process
1. **Requirements Gathering** (1 day)
2. **Model Development** (2 day)
3. **Web Interface Implementation** (1 day)
4. **Testing & Validation** (1 day)
5. **Deployment** (3 day)

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
<img width="827" alt="4280fda1e8688a8e1116a7ffb0947b2" src="https://github.com/user-attachments/assets/43547769-53a8-4867-b34d-3c1768b206a2" />


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
1. **Graphical Abstract** placeholder (replace with actual diagram)
2. Clear development methodology explanation
3. Detailed project timeline and team structure
4. Algorithm documentation with code highlighting
5. Current/Future status sections with checkboxes
6. Quick start guide for new users
7. Complete API documentation
8. License information


