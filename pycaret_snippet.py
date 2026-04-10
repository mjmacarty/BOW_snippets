# PyCaret Example Code Snippet
# NOTE: this code should be copied into a Jupyter Notebook.

""" Meant to facilitate the entire machine learning workflow, 
from data preprocessing to model training, evaluation. PyCaret is a 
low-code machine learning library that automates many of the tedious 
tasks involved in building machine learning models, making it easier for 
users to quickly develop and deploy models with minimal coding. PyCaret is not 
meant for production code, but rather to quickly identify promising models 
and get a sense of the data. """

from pycaret.classification import *

# 1. Load sample data (or use your own DataFrame)
data = get_data('juice')

# 2. Initialize setup (automatically handles preprocessing)
s = setup(data, target = 'Purchase', session_id = 123)

# 3. Compare all models and pick the best one
best = compare_models()

# 4. Analyze the model with interactive plots
plot_model(best, plot = 'auc')
evaluate_model(best)

# 5. Make predictions on new data
predictions = predict_model(best, data = data.drop('Purchase', axis=1))

# 6. Save the entire pipeline
save_model(best, 'my_best_pipeline')
