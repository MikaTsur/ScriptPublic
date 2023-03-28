import os
from comet_ml import Experiment
import time


os.environ["COMET_URL_OVERRIDE"] = "https://staging.comet.ml/clientlib/"
os.environ["COMET_OPTIMIZER_URL"] = "https://staging.comet.com/optimizer/"
os.environ["COMET_OVERRIDE_FEATURE_SDK_USE_HTTP_MESSAGES"] = 'True'


experiment = Experiment(log_git_metadata=False, log_git_patch=False, api_key=os.environ.get("STG_KEY"), log_env_details=True,
                        log_env_gpu=True, log_env_cpu=True, log_env_host=True, project_name="HTML")


for i in range(1000):
  sampleHtml = "<p>" + str(i) + " love Comet </p>\n"
  time.sleep(0.3)
  experiment.log_html(sampleHtml, clear=False)

experiment.end()