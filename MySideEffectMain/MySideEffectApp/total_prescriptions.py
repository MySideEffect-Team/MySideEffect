import csv


class prescription_data:
    """

    Builds a class that allows querying to retrieve the number of people in a specific chosen subgroup that receive a specific medicine.

    """
    # Provide the file paths of the csv files containing prescriptions split by population characteristics and prescriptions by medicine
    def __init__(self, population_filepath, medicine_filepath):
        self.pop_prescriptions = prescription_data.load_data(population_filepath)
        self.drug_prescriptions = prescription_data.load_data(medicine_filepath)

# Load the data from the total medicines prescribed and the total population that is getting a prescription
    @staticmethod
    def load_data(filename):
        with open(filename) as csvfile:
            filedict = {}
            reader = csv.reader(csvfile)
            for row in reader:
                filedict[row[0].lower()] = row[1]
            return filedict

    def compute_data(self, characteristic, medicine):
        """
        Return the number of people with the chosen characteristics (age, gender, race) that are being prescribed the chosen medicine.

        Args:
            cha (str): both, male, female, white, white_male, white_female, black, black_male, black_female, asian, asian_male,
                       asian_female, hispanic, hispanic_male, hispanic_female, mexican, mexican_male, mexican_female, both_under18,
                       both_18-44, both_45-64, both_over65, male_under18, male_18-44, male_45-64, male_over65, female_under18,
                       female_18-44, female_45-64, female_over65
            med (str): generic drug names

        Returns:
           (float) total number of people with chosen characteristic taking this drug.

        """

        # calculate the percentage of people with the chosen characterstics that are being prescribed a drug out of all drug prescriptions
        percentage_out_total = int(self.pop_prescriptions.get(characteristic.lower(), None)) / int(self.pop_prescriptions.get('both', None))

        # Calculate and return by multiplying the percentage out of total with the total number of prescriptions for that specific medicine
        return int(self.drug_prescriptions.get(medicine.lower(), None)) * percentage_out_total
