import pandas as pd
import tensorflow as tf
import os

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path # Path to the file to be processed
        self.data = None # This will hold the loaded data


    def load_data(self):
         # Check the file extension and load the data accordingly

            # Load CSV file
        if self.file_path.endswith('.csv'):
            self.data = pd.read_csv(self.file_path)
            print(f"CSV loaded: {self.file_path}")

            # Load Parquet file
        elif self.file_path.endswith('.parquet'):
            self.data = pd.read_parquet(self.file_path)
            print(f"Parquet loaded: {self.file_path}")

            # Load text file
        elif self.file_path.endswith('.txt'):
            with open(self.file_path, 'r') as f:
                self.data = f.read()
            print(f"Text file loaded: {self.file_path}")

            # Load image folder (uses TensorFlow to load images)
        elif os.path.isdir(self.file_path):  # Assuming image folder
            self.data = tf.keras.utils.image_dataset_from_directory(
                self.file_path,
                image_size=(64, 64),
                batch_size=1
            )
            print(f"Image dataset loaded from folder: {self.file_path}")

        else:
            raise ValueError("Unsupported file format or path.")

    def initial_processing(self):
        if self.data is None:
            raise ValueError("No data loaded.")

        if isinstance(self.data, pd.DataFrame):
            print("Initial Data Summary:")
            print(self.data.info())
            print("\nMissing Values:")
            print(self.data.isnull().sum())
            print("\nDescriptive Statistics:")
            print(self.data.describe())

        elif isinstance(self.data, str):  # text file
            print("Text file contents:")
            print(self.data[:500])  # print first 500 chars

        else:  # TensorFlow image dataset
            print("Image dataset loaded. Previewing one batch:")
            for images, labels in self.data.take(1):
                print("Images shape:", images.shape)
                print("Labels shape:", labels.shape)
