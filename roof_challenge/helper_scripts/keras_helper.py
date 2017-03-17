import pandas as pd


def classify_images(test_dir, model):
    """Score model on test images
    Args:
        test_dir(string): the path to test images directory
        model: keras model

    Returns:
        a pandas data frame with image id and predicted class (label)
    """
    test_datagen = ImageDataGenerator(rescale=1./255)

    test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(150, 150),
        batch_size=1,
        class_mode=None,
        shuffle=False)
    preds = model.predict_generator(test_generator, 1600)
    submission = pd.DataFrame({'Id': test_generator.filenames})
    submission['label'] = pd.DataFrame(preds).apply(lambda x: x.idxmax(), axis=1)
    submission['Id'] = submission.Id.str.extract('(\-*[0-9]+)')
    submission['label'] = submission.label + 1
    return submission