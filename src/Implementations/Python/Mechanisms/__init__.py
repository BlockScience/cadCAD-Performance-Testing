from .Dummy import (
    dummy_update_dummy_entity_mechanism,
    dummy_increment_time_mechanism,
    dummy_log_simulation_data_mechanism,
)
from .Sample import (
    update_mean_mechanism,
    update_queue_mechanism,
    log_simulation_data_mechanism,
)

mechanisms = {
    "DUMMY Update Dummy Entity Mechanism": dummy_update_dummy_entity_mechanism,
    "DUMMY Increment Time Mechanism": dummy_increment_time_mechanism,
    "DUMMY Log Simulation Data Mechanism": dummy_log_simulation_data_mechanism,
    "Update Mean Mechanism": update_mean_mechanism,
    "Update Queue Mechanism": update_queue_mechanism,
    "Log Simulation Data Mechanism": log_simulation_data_mechanism,
}
