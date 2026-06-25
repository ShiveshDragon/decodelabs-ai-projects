from PIL import Image
import torch
from torchvision import models, transforms

# Load pretrained model
weights = models.ResNet18_Weights.DEFAULT
model = models.resnet18(weights=weights)
model.eval()

# Class labels
labels = weights.meta["categories"]

# Image preprocessing
preprocess = weights.transforms()

# Load image
img = Image.open("sample.jpg").convert("RGB")

# Prepare image
input_tensor = preprocess(img).unsqueeze(0)

# Prediction
with torch.no_grad():
    output = model(input_tensor)

predicted_class = output.argmax(1).item()

print("\n===== Image Recognition Result =====")
print("Predicted Object:", labels[predicted_class])