from mozaik.experiments.optogenetic import SingleOptogeneticArrayStimulus
from mozaik.tools.distribution_parametrization import MozaikExtendedParameterSet
from mozaik.experiments import NoStimulation
from parameters import ParameterSet
import os


def create_experiments(model):
    video_path = os.environ.get("VIDEO_PATH")
    if video_path is None:
        raise ValueError("VIDEO_PATH is not set")

    experiments = []

    experiments.append(
        NoStimulation(model, ParameterSet({"duration": 140})))

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
                                "video_path": video_path,
                                "intensity": 10,
                                "duration": 2002,
                                "onset_time": 0,
                                "offset_time": 2002,
                            }
                        )
                    }
            )
        )
    )
    return experiments