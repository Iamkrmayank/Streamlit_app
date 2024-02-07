import streamlit as st

# Dictionary mapping algorithm names to image URLs
algorithm_images = {
    'Decision Tree': '/Users/kumarmayank/Desktop/SL/DT.png',
    'Random Forest': '/Users/kumarmayank/Desktop/SL/RF.png',
    'Linear Regression': '/Users/kumarmayank/Desktop/SL/LR.png',
    'Extra Trees':'/Users/kumarmayank/Desktop/SL/ET.png',
    'Gradient Boosting':'/Users/kumarmayank/Desktop/SL/GB.png',
    'K Nearest Neigbour':'/Users/kumarmayank/Desktop/SL/Knn.png',
    'Simple Mean Model':'/Users/kumarmayank/Desktop/SL/Mean.png',
    'Simple Median Model':'/Users/kumarmayank/Desktop/SL/Median.png',
    'XgBoost':'/Users/kumarmayank/Desktop/SL/Xgboost.png',
    'HistGBM':'/Users/kumarmayank/Desktop/SL/HistGBM.png',
    'LightGBM':'/Users/kumarmayank/Desktop/SL/LightBGM.png',
    'ARIMA Time Series':'/Users/kumarmayank/Desktop/SL/ARIMA.png'
    # Add more algorithms as needed
}

# Streamlit app
st.title('Algorithm Visualization with Streamlit')

# Dropdown for selecting the algorithm
selected_algorithm = st.selectbox('Select Algorithm:', list(algorithm_images.keys()))

# Display the selected algorithm's image
if selected_algorithm in algorithm_images:
    st.image(algorithm_images[selected_algorithm], caption=f'{selected_algorithm} Visualization', use_column_width=True)

