# src/data_processor.py

import os
import pandas as pd
import tensorflow as tf

class DataProcessor:
    def __init__(self, file_path, image_size=(64, 64), batch_size=1):
        self.file_path = file_path
        self.image_size = image_size
        self.batch_size = batch_size
        self.data = None

    def load_data(self):
        if self.file_path.endswith('.csv'):
            self.data = pd.read_csv(self.file_path)
            print(f"CSV loaded: {self.file_path}")
        elif self.file_path.endswith('.parquet'):
            self.data = pd.read_parquet(self.file_path)
            print(f"Parquet loaded: {self.file_path}")
        elif self.file_path.endswith('.txt'):
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.data = f.read()
            print(f"Text file loaded: {self.file_path}")
        elif os.path.isdir(self.file_path):
            self.data = tf.keras.utils.image_dataset_from_directory(
                self.file_path,
                image_size=self.image_size,
                batch_size=self.batch_size
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
        elif isinstance(self.data, str):
            print("Text file contents:")
            print(self.data[:500])  # Print first 500 characters
        else:
            print("Image dataset loaded. Previewing one batch:")
            for images, labels in self.data.take(1):
                print("Images shape:", images.shape)
                print("Labels shape:", labels.shape)
