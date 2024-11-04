import csv
import os

class FrequencyListProcessor:
    def __init__(self, input_file, output_file,word_frequency):
        self.input_file = input_file
        self.output_file = output_file
        self.frequency = word_frequency
        self.extracted_words = []

    def load_frequency_list(self):
        """Loads frequency data from the text file and extracts the words."""
        try:
            with open(self.input_file, mode="r") as frequency_list:
                for line in frequency_list:
                    parts = line.split()
                    if len(parts) == 2:  # Ensure the line has exactly two parts
                        word, frequency = parts[0], parts[1]
                        if frequency.isdigit() and int(frequency) > self.frequency:
                            self.extracted_words.append(word)
        except FileNotFoundError:
            print(f"Error: The file {self.input_file} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_to_csv(self):
        """Writes the extracted words to a CSV file, avoiding appending if file already exists."""
        if os.path.exists(self.output_file):
            print(f"{self.output_file} already exists. Please delete it or rename it to avoid appending.")
            return  # Exit the method without writing to the file

        with open(self.output_file, mode="w", newline='') as extracted_csv:
            writer = csv.writer(extracted_csv)
            for word in self.extracted_words:
                writer.writerow([word])

        print(f"Data successfully written to {self.output_file}.")
        print(f"Total words extracted: {len(self.extracted_words)}")

    def process(self):
        """Runs the full process of loading and saving to CSV."""
        self.load_frequency_list()
        self.save_to_csv()


# Usage:
processor = FrequencyListProcessor("Data/fr_to_en_data/fr_50k.txt", "Data/fr_to_en_data/extracted_fr_words.csv", 100000)
processor.process()

#source of frequency lists : https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists
#GitHub link : https://github.com/hermitdave/FrequencyWords/