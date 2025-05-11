# Thirty Grand

A data analysis and visualization tool for my first 30,000 wildlife observations from iNaturalist. 

## 📝 License

This project is licensed under the LGPL License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

Mark Nenadov (2024/2025)

## 🔗 Links

- [iNaturalist Observations Report](https://docs.google.com/document/d/19-Nd1FMf-i1crleeBk0qfocPLEZFZPEB0-CNjl1a2Ac/edit?usp=sharing)

## 📋 Requirements

- Python 3.12+
- Poetry for dependency management

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/thirty-grand.git
cd thirty-grand

# Install dependencies using Poetry
poetry install
```

## 🏗️ Project Structure

```
thirty-grand/
├── src/
│   ├── thirty_grand/
│   │   ├── core/           # Core business logic
│   │   ├── data/          # Data models and processing
│   │   ├── visualization/ # Visualization components
│   │   └── cli/           # Command-line interface
│   └── tests/             # Test suite
├── data/                  # Data files
├── scripts/              # Utility scripts
└── docs/                 # Documentation
```

## Module Structure

### Queries
- query_all_observations (function)
- random_sample (function)

### Utilities

Charting
- display_yearly_observation_barchart (function using matplotlib)

Tables
- get_observations_table_str (function)
- print_observations_table (function)
- get_taxon_table_str (function)
- print_family_table (function)
- print_class_table (function)
- print_genera_table (function)
- print_order_table (function)
- print_distinct_species_in_taxon (function)

### Running Tests

```bash
poetry run pytest
```
