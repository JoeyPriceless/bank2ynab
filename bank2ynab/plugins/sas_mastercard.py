from bank_process import B2YBank
import pandas as pd


class SAS_Mastercard(B2YBank):
    def __init__(self, config_object):
        """
        :param config_object: a dictionary of conf parameters
        """
        super(SAS_Mastercard, self).__init__(config_object)
        self.name = "SAS EuroBonus World Mastercard"

    def _preprocess_file(self, file_path):
        df = pd.read_excel(file_path, engine="xlrd")
        # Remove all rows before the row where the first column contains "Köp/uttag"
        index = df.index[df.iloc[:, 0] == "Köp/uttag"].tolist()[0]
        df = df[index+1:]
        df.to_csv(file_path, sep=";", index=False)


def build_bank(config):
    """This factory function is called from the main program,
    and expected to return a B2YBank subclass.
    Without this, the module will fail to load properly.

    :param config: dict containing all available configuration parameters
    :return: a B2YBank subclass instance
    """
    return SAS_Mastercard(config)
