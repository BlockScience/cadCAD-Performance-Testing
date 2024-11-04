from .Dummy import dummy_letter_count_policy
from .Sample import update_rolling_mean_policy_v1

policies = {
    "DUMMY Letter Count Policy V1": dummy_letter_count_policy,
    "Update Rolling Mean Policy V1": update_rolling_mean_policy_v1,
}
