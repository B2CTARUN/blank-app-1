import cv2
import numpy as np
import streamlit as st
from pyzbar.pyzbar import decode

def scan_qr_code():
    # Create a video capture object
    cap = cv2.VideoCapture(0)

    # Placeholder for image display
    stframe = st.empty()

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to grab frame")
            break

        # Decode QR codes in the frame
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            qr_data = obj.data.decode('utf-8')
            st.success(f'Scanned QR Code Data: {qr_data}')
            break  # Stop after the first QR code is found

        # Convert the frame to RGB format for Streamlit
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame_rgb, channels="RGB", use_column_width=True)

        # Break the loop if 'q' is pressed (not directly possible in Streamlit)
        if st.button('Stop Scanning'):
            break

    cap.release()

if __name__ == '__main__':
    st.title("QR Code Scanner")
    st.write("Press the button below to start scanning.")
    if st.button("Start Scanning"):
        scan_qr_code()
