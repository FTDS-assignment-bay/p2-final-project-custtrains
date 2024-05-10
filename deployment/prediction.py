import pandas as pd
import streamlit as st
import pickle as pkl
import json as js

def app():
    with open('list_kolom_numerik.txt', 'r') as num:
        numeric = js.load(num)
    with open('list_kolom_kategorik.txt', 'r') as cat:
        categoric = js.load(cat)
    with open('modelBest.pkl', 'rb') as file:
        model = pkl.load(file)

    items = {
        'Clothing': ['Blouse', 'Sweater', 'Jeans', 'Shirt', 'Shorts', 'Dress', 'Skirt', 'Pants', 'Hoodie', 'T-shirt', 'Socks'],
        'Footwear': ['Sandals', 'Sneakers', 'Shoes', 'Boots'],
        'Accessories': ['Handbag', 'Sunglasses', 'Jewelry', 'Scarf', 'Hat', 'Backpack', 'Belt', 'Gloves'],
        'Outerwear': ['Coat', 'Jacket']
    }
    
    st.title('Silahkan Periksa Kategori Anda!')
    # Menampilkan gambar
    st.image('image2.jpg', use_column_width=True)
    
    with st.form('Input Data Pelanggan'):
        age = st.number_input('Age', min_value=0, step=1)
        gender = st.selectbox('Gender', ['Male', 'Female'])
        item_purchased = st.selectbox('Item Purchased', ['Blouse', 'Sweater', 'Jeans', 'Shirt', 'Shorts', 'Coat', 'Dress', 'Skirt', 'Pants', 'Jacket', 'Hoodie', 'T-shirt', 'Socks', 'Sandals', 'Sneakers', 'Shoes', 'Boots', 'Handbag', 'Sunglasses', 'Jewelry', 'Scarf', 'Hat', 'Backpack', 'Belt', 'Gloves' ])
        purchase_amount = st.number_input('Purchase Amount (USD)', min_value=0.0, step=0.01)
        location = st.selectbox('Location', ['Kentucky', 'Maine', 'Massachusetts', 'Rhode Island', 'Oregon','Wyoming', 'Montana', 'Louisiana', 'West Virginia', 'Missouri','Arkansas', 'Hawaii', 'Delaware', 'New Hampshire', 'New York','Alabama', 'Mississippi', 'North Carolina', 'California','Oklahoma', 'Florida', 'Texas', 'Nevada', 'Kansas', 'Colorado','North Dakota', 'Illinois', 'Indiana', 'Arizona', 'Alaska','Tennessee', 'Ohio', 'New Jersey', 'Maryland', 'Vermont','New Mexico', 'South Carolina', 'Idaho', 'Pennsylvania','Connecticut', 'Utah', 'Virginia', 'Georgia', 'Nebraska', 'Iowa','South Dakota', 'Minnesota', 'Washington', 'Wisconsin', 'Michigan'])
        size = st.selectbox('Size', ['L', 'S', 'M', 'XL'])
        color = st.selectbox('Color', ['Gray', 'Maroon', 'Turquoise', 'White', 'Charcoal', 'Silver','Pink', 'Purple', 'Olive', 'Gold', 'Violet', 'Teal', 'Lavender','Black', 'Green', 'Peach', 'Red', 'Cyan', 'Brown', 'Beige','Orange', 'Indigo', 'Yellow', 'Magenta', 'Blue'])
        season = st.selectbox('Season', ['Winter', 'Spring', 'Summer', 'Fall'])
        review_rating = st.number_input('Review Rating', min_value=0.0, max_value=5.0, step=0.1)
        subscription_status = st.selectbox('Subscription Status', ['Yes', 'No'])
        shipping_type = st.selectbox('Shipping Type', ['Express', 'Free Shipping', 'Next Day Air', '2-Day Shipping', 'Store Pickup', 'Standard'])
        discount_applied = st.selectbox('Discount Applied', ['Yes', 'No'])
        promo_code_used = st.selectbox('Promo Code Used', ['Yes', 'No'])
        previous_purchases = st.number_input('Previous Purchases', min_value=0, step=1)
        payment_method = st.selectbox('Payment Method', ['Venmo', 'Cash', 'Credit Card', 'PayPal', 'Bank Transfer'])
        frequency_of_purchases = st.selectbox('Frequency of Purchases', ['Fortnightly', 'Weekly', 'Bi-Weekly', 'Monthly'])
        
        submit_button = st.form_submit_button('Submit Data')

        if submit_button:
            category = None
            for key, values in items.items():
                if item_purchased in values:
                    category = key
                    break

            if category is None:
                st.error('Invalid item purchased selected. Please select a valid item.')
            else:
                data_inf = {
                    'Customer ID': [1],
                    'Age': [age],
                    'Gender': [gender],
                    'Item Purchased': [item_purchased],
                    'Category': [category],
                    'Purchase Amount (USD)': [purchase_amount],
                    'Location': [location],
                    'Size': [size],
                    'Color': [color],
                    'Season': [season],
                    'Review Rating': [review_rating],
                    'Subscription Status': [subscription_status],
                    'Shipping Type': [shipping_type],
                    'Discount Applied': [discount_applied],
                    'Promo Code Used': [promo_code_used],
                    'Previous Purchases': [previous_purchases],
                    'Payment Method': [payment_method],
                    'Frequency of Purchases': [frequency_of_purchases]
                }
                df = pd.DataFrame(data_inf)
                listColumn = numeric + categoric
                df = df[listColumn]
                prediksi = model.predict(df)
                if prediksi[0] == 0:
                    hasil = "Discount Hunter"
                elif prediksi[0] == 1:
                    hasil = "Impulsive Buyer"
                elif prediksi[0] == 2:
                    hasil = "Normal Customer"
                else:
                    hasil = "Royal Customer"
                st.write('Status Pelanggan Kamu Termasuk', hasil)

if __name__ == "__main__":
    app()
