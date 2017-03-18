import os
import shutil
import pandas as pd

# specify path to original images directory
path_of_original_folder = '../images/train'
# specify path to new images directory
path_of_organised_folder = '../new_images/'
# specify path to train csv directory
path_of_train_folder = '../data/train.csv'

if not os.path.exists(path_of_organised_folder): ## remove dir if exists
    os.makedirs(path_of_organised_folder)

# create a directory for each combination of training and validation set with labels
for dataset_folder in ['train', 'val']:
    for label_folder in ['label1', 'label2', 'label3', 'label4']:
        if not os.path.exists(os.path.join(path_of_organised_folder, dataset_folder, label_folder)):
            os.makedirs(os.path.join(path_of_organised_folder, dataset_folder, label_folder))
        

train = pd.read_csv(path_of_train_folder)
train['Id'] = train.Id.astype('str') + '.jpg'
allImages = [f for f in os.listdir(path_of_original_folder)]

# stratified sampling of 30% validation
val_images = set(train.ix[train.label == 1, 'Id'].sample(frac=0.3, random_state=0)).union(set(train.ix[train.label == 2, 'Id'].sample(frac=0.3, random_state=0))).union(set(train.ix[train.label == 3, 'Id'].sample(frac=0.3, random_state=0))).union(set(train.ix[train.label == 4, 'Id'].sample(frac=0.3, random_state=0)))

for image in allImages:
    label = train.ix[train['Id'] == image, 'label'].values[0]
    if image in val_images:
        shutil.copy(os.path.join(path_of_original_folder, image), os.path.join(path_of_organised_folder, 'val/label{}/'.format(label)))
    else:
        shutil.copy(os.path.join(path_of_original_folder, image), os.path.join(path_of_organised_folder, 'train/label{}/'.format(label)))
