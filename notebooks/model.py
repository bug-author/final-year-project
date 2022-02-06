import keras
from keras import layers

# preprocessed data
input_speeds = keras.Input(shape=(1200, 17), name="input_speeds")
input_positions = keras.Input(shape=(1200, 17), name="input_positions")

features = layers.Concatenate()([input_speeds, input_positions])
LSTM_50 = layers.LSTM(50, name="features_1", return_sequences=True)(features)
LSTM_5 = layers.LSTM(5, name="features_2")(LSTM_50)

forecasted_speeds = layers.Dense(17, name="forecasted_speeds")(features)
forecasted_positions = layers.Dense(17, name="forecasted_positions")(features)

model = keras.Model(
    inputs = [input_speeds, input_positions],
    outputs = [forecasted_speeds, forecasted_positions]
)

# visualize the model
import tensorflow
tensorflow.keras.utils.plot_model(model, 'functional_api_regressor.png', show_shapes=True)
"""
# guess these are the arrays from creation function
# input data
input_speeds_data = ...
input_positions_data = ...

# target data
forecasted_speeds_data = ...
forecasted_positons_data = ...

# compilation
model.compile(
    optimizer='adam',
    loss=['mean_squared_error'],
    metrics=['mean_absolute_error']
)

# fitting
model.fit(
    [input_speeds_data, input_positions_data],
    [forecasted_speeds_data, forecasted_positons_data],
    epochs=100,
    shuffle=False
    validation_split=0.15
)

# predictions
forecasted_speeds_preds, forecasted_positons_preds = model.predict(
    [...]
)
"""