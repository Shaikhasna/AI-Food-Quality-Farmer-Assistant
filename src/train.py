from dataset import load_datasets
from model import build_model
from config import EPOCHS, MODEL_PATH


def train():

    train_ds, val_ds, class_names = load_datasets()

    num_classes = len(class_names)

    model = build_model(num_classes)

    model.summary()

    model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=EPOCHS
    )

    model.save(MODEL_PATH)

    print("Model saved to", MODEL_PATH)


if __name__ == "__main__":
    train()