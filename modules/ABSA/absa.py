import pandas as pd
import warnings

from pyabsa import AspectTermExtraction as ATEPC
from pyabsa import DatasetItem
from pyabsa import ModelSaveOption, DeviceTypeOption

config = (ATEPC.ATEPCConfigManager.get_atepc_config_english())
config.model = ATEPC.ATEPCModelList.FAST_LCF_ATEPC
config.batch_size = 16
config.patience = 2
config.log_step = -1
config.seed = [1]
config.verbose = False  # If verbose == True, PyABSA will output the model strcture and seversal processed data examples
config.notice = ("This is an training example for aspect term extraction")
my_dataset = DatasetItem("100.CustomDataset", ["129.Kaggle", "113.laptop14"])

trainer = ATEPC.ATEPCTrainer(
    config=config,
    dataset=my_dataset,
    from_checkpoint="english",  # if you want to resume training from our pretrained checkpoints, you can pass the checkpoint name here
    auto_device=DeviceTypeOption.AUTO,  # use cuda if available
    checkpoint_save_mode=ModelSaveOption.SAVE_MODEL_STATE_DICT,  # save state dict only instead of the whole model
    load_aug=False,  # there are some augmentation dataset for integrated datasets, you use them by setting load_aug=True to improve performance
)

# Untuk test hasil prediksi
# aspect_extractor = trainer.load_trained_model()
# assert isinstance(aspect_extractor, ATEPC.AspectExtractor)
# atepc_examples = [
#     'The app has a fantastic design with vibrant colors that make the user experience wonderful. However, the load times can sometimes be quite slow, which can be annoying',
#     'I absolutely love the functionality of this app, it integrates well with my daily tasks, and no bugs at all!',
#     'The customer service was not helpful at all. I had an issue that needed resolving, and it took them over a week to respond, which was very frustrating ',
#     'This application is revolutionary in its approach to online learning. The content is well-organized and easy to follow, but the video playback could be improved as it buffers a lot',
#     'I found the app to be generally unstable after the last update; it crashes frequently. Customer support was responsive but could not solve the problem immediately'
# ]
# for ex in atepc_examples:
#     result = aspect_extractor.predict(
#         text=ex,
#         print_result=True,
#         ignore_error=True,  # ignore an invalid example, if it is False, invalid examples will raise Exceptions
#         eval_batch_size=32,
#     )