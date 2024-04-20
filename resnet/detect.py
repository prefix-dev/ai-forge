import sys
import os
import torch
from pathlib import Path
from PIL import Image
from torchvision.models.resnet import resnet18, ResNet18_Weights
from functools import partial

weights = ResNet18_Weights.DEFAULT
weights.value.url = (Path(os.environ["CONDA_PREFIX"]) / "share/models/resnet18-f37072fd.pth").as_uri()
model = resnet18(weights=weights)

# set to eval mode
model.eval()

if len(sys.argv) < 2:
    print("Missing image argument")
    sys.exit(1)

file = sys.argv[1]

filename = Path(file)

preprocess = weights.transforms()

input_image = Image.open(filename)
input_batch = preprocess(input_image).unsqueeze(0)

# The output has unnormalized scores. To get probabilities, you can run a softmax on it.
probabilities = model(input_batch).squeeze(0).softmax(0)

categories = weights.meta["categories"]

# Show top categories per image
top5_prob, top5_catid = torch.topk(probabilities, 5)
for i in range(top5_prob.size(0)):
    print(categories[top5_catid[i]], top5_prob[i].item())