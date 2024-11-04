from .Dummy import v1_dummy_control, v2_dummy_control
from .Sample import add_new_sample_control_action_v1

control_action_options = {
    "DUMMY Length-1 DEF Equal Weight Option": v1_dummy_control,
    "DUMMY Length-1 DEF D Probability Option": v2_dummy_control,
    "Add New Sample Control Action V1": add_new_sample_control_action_v1,
}
