from mozaik.experiments.optogenetic import SingleOptogeneticArrayStimulus
from mozaik.tools.distribution_parametrization import MozaikExtendedParameterSet
from parameters import ParameterSet

def create_experiments(model):
    experiments = []
    experiments.append(
        SingleOptogeneticArrayStimulus(
            model,
            MozaikExtendedParameterSet(
                    {
                        "stimulator_array_list": [
                            {
                                "sheet": "V1_Exc_L2/3",
                                "name": "stimulator_array",
                                "intensity_scaler": 1.0,
                            }
                        ],
                        "num_trials": 1,
                        "stimulating_signal_function": "mozaik.sheets.direct_stimulator.stimulating_pattern_flash",
                        "stimulating_signal_function_parameters": ParameterSet(
                            {
                                "shape": "video",
                                "video_path": "/home/Lea/Skola/bakalarka/mozaik-packages/mozaik/tests/full_model/models/LSV1M_tiny_opto/random_video/random_opto_video_1s.npy",
                                "intensity": 10,
                                "duration": 1000,
                                "onset_time": 0,
                                "offset_time": 1000,
                            }
                        )
                    }
            )
        )
    )
    return experiments