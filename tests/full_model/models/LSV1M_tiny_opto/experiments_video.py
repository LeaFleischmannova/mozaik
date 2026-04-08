from mozaik.experiments.optogenetic import SingleOptogeneticArrayStimulus
from mozaik.tools.distribution_parametrization import MozaikExtendedParameterSet
from parameters import ParameterSet
import os

HERE = os.path.dirname(os.path.abspath(__file__))
VIDEO_PATH = os.path.join(HERE, "random_video", "random_opto_video_1s.npy")

def create_experiments(model):
    experiments = []
    experiments.append(
        NoStimulation(model, ParameterSet({"duration": 105})),
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
                                "video_path": VIDEO_PATH,
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