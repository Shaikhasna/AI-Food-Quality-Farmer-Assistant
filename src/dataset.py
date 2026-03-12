import tensorflow as tf
from config import IMG_SIZE, BATCH_SIZE, TRAIN_DIR, VAL_DIR


def load_datasets():

    train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
        TRAIN_DIR,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        label_mode="categorical"
    )

    val_dataset = tf.keras.preprocessing.image_dataset_from_directory(
        VAL_DIR,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        label_mode="categorical"
    )

    class_names = train_dataset.class_names

    train_dataset = train_dataset.prefetch(buffer_size=tf.data.AUTOTUNE)
    val_dataset = val_dataset.prefetch(buffer_size=tf.data.AUTOTUNE)

    return train_dataset, val_dataset, class_names