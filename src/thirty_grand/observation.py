class Observation:
    def __init__(self, obs_id, observed_on_string, observed_on, time_observed_at, scientific_name, common_name, iconic_taxon_name, taxon_id):
        self.obs_id = obs_id
        self.observed_on_string = observed_on_string
        self.observed_on = observed_on
        self.time_observed_at = time_observed_at
        self.scientific_name = scientific_name
        self.common_name = common_name
        self.iconic_taxon_name = iconic_taxon_name
        self.taxon_id = taxon_id
        
    def __repr__(self):
        return f"Observation(obs_id={self.obs_id}, observed_on_string='{self.observed_on_string}', observed_on='{self.observed_on}', time_observed_at='{self.time_observed_at}', scientific_name='{self.scientific_name}', common_name='{self.common_name}', iconic_taxon_name='{self.iconic_taxon_name}', taxon_id={self.taxon_id})"

