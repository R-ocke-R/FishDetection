import os
import random
import shutil

# ---------- CONFIG ----------
CROPPED_FOLDER = "/Users/manu/Master/FishDetection/Data/cropped"       # folder with cropped images
DATASET_FOLDER = "/Users/manu/Master/FishDetection/Data/fish_dataset"  # folder to create YOLO structure
INDEX_FILE = "/Users/manu/Master/FishDetection/Data/index.txt"         # your txt index file
TRAIN_SPLIT = 0.8

# ---------- STEP 1: Read index file ----------
class_map = {}  # species_name -> class_id
image_class_map = {}  # image_name -> class_id

with open(INDEX_FILE, "r") as f:
    for line in f:
        parts = line.strip().split("=")
        if len(parts) < 5:
            continue
        class_id, species_name, capture_type, image_name, idx = parts
        class_id = int(class_id) - 1  # zero-based for YOLO
        # map species to class id
        if species_name not in class_map:
            class_map[species_name] = class_id
        image_class_map[image_name] = class_id

# ---------- STEP 2: Create YOLO folder structure ----------
for folder in ["images/train", "images/val", "labels/train", "labels/val"]:
    os.makedirs(os.path.join(DATASET_FOLDER, folder), exist_ok=True)

# ---------- STEP 3: Split images ----------
all_images = [f for f in os.listdir(CROPPED_FOLDER) if f.endswith((".png", ".jpg", ".jpeg"))]
random.shuffle(all_images)
split_idx = int(len(all_images) * TRAIN_SPLIT)
train_images = all_images[:split_idx]
val_images = all_images[split_idx:]

# ---------- STEP 4: Copy images and create labels ----------
def process_images(image_list, split_type):
    for img_file in image_list:
        # Determine class_id from image name
        base_name = os.path.splitext(img_file)[0]
        class_id = image_class_map.get(base_name, None)
        if class_id is None:
            continue  # skip images not in index

        # Copy image
        src_path = os.path.join(CROPPED_FOLDER, img_file)
        dst_path = os.path.join(DATASET_FOLDER, f"images/{split_type}", img_file)
        shutil.copy2(src_path, dst_path)

        # Create YOLO label file (full image bounding box)
        label_path = os.path.join(DATASET_FOLDER, f"labels/{split_type}", f"{base_name}.txt")
        with open(label_path, "w") as f:
            f.write(f"{class_id} 0.5 0.5 1 1\n")

process_images(train_images, "train")
process_images(val_images, "val")

# ---------- STEP 5: Create data.yaml ----------
yaml_path = os.path.join(DATASET_FOLDER, "data.yaml")
with open(yaml_path, "w") as f:
    f.write(f"path: {DATASET_FOLDER}\n")
    f.write("train: images/train\n")
    f.write("val: images/val\n\n")
    f.write(f"nc: {len(class_map)}\n")
    # Ensure species are ordered by class_id
    names_list = [None] * len(class_map)
    for species, cid in class_map.items():
        names_list[cid] = species
    f.write(f"names: {names_list}\n")

print("✅ Dataset prepared for YOLO!")
