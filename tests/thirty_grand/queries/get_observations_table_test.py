import unittest
from prettytable import PrettyTable
from unittest.mock import Mock

from src.thirty_grand import observation
from src.thirty_grand.utilities import get_observations_table_str


class TestGetObservationsTableStr(unittest.TestCase):
    def setUp(self):
        # Create mock Observation objects
        self.observation1 = Mock(spec=observation.Observation)
        self.observation1.obs_id = 1
        self.observation1.observed_on_string = "2023-05-25"
        self.observation1.observed_on = "2023-05-25"
        self.observation1.time_observed_at = "10:00"
        self.observation1.scientific_name = "Panthera leo"
        self.observation1.common_name = "Lion"
        self.observation1.iconic_taxon_name = "Mammalia"
        self.observation1.taxon_id = 1234

        self.observation2 = Mock(spec=observation.Observation)
        self.observation2.obs_id = 2
        self.observation2.observed_on_string = "2023-05-26"
        self.observation2.observed_on = "2023-05-26"
        self.observation2.time_observed_at = "12:00"
        self.observation2.scientific_name = "Elephas maximus"
        self.observation2.common_name = "Elephant"
        self.observation2.iconic_taxon_name = "Mammalia"
        self.observation2.taxon_id = 5678

        self.observations = [self.observation1, self.observation2]

    def test_get_observations_table_str(self):
        expected_table = PrettyTable()
        expected_table.field_names = [
            "Observation ID",
            "Observed On String",
            "Observed On",
            "Time Observed At",
            "Scientific Name",
            "Common Name",
            "Iconic Taxon Name",
            "Taxon ID"
        ]
        expected_table.add_row([
            1, "2023-05-25", "2023-05-25", "10:00", "Panthera leo", "Lion", "Mammalia", 1234
        ])
        expected_table.add_row([
            2, "2023-05-26", "2023-05-26", "12:00", "Elephas maximus", "Elephant", "Mammalia", 5678
        ])
        expected_output = expected_table.get_string()

        result = get_observations_table_str(self.observations)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
