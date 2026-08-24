import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Vector Addition Visualizer", page_icon="📐", layout="centered")

st.title("📐 Vector Addition Visualizer")
st.caption("Day 1 of 30: Physics Simulators Challenge")

st.markdown("Adjust the X and Y components of Vectors **A** and **B** to see their Resultant **R**.")

# UI: Create two columns for neat sliders
col1, col2 = st.columns(2)

with col1:
    st.subheader("Vector A (Blue)")
    ax_val = st.slider("A_x component", -10.0, 10.0, 4.0, step=1.0)
    ay_val = st.slider("A_y component", -10.0, 10.0, 6.0, step=1.0)

with col2:
    st.subheader("Vector B (Red)")
    bx_val = st.slider("B_x component", -10.0, 10.0, 5.0, step=1.0)
    by_val = st.slider("B_y component", -10.0, 10.0, -3.0, step=1.0)

# Physics / Math Calculations
rx_val = ax_val + bx_val
ry_val = ay_val + by_val
magnitude = np.sqrt(rx_val**2 + ry_val**2)
angle = np.degrees(np.arctan2(ry_val, rx_val))

# Display Results
st.markdown("---")
st.success(f"**Resultant Vector R** = {rx_val} î + {ry_val} ĵ  |  **Magnitude**: {magnitude:.2f}  |  **Angle**: {angle:.2f}°")

# Plotting
fig, ax = plt.subplots(figsize=(7, 7))

# Draw Vectors using quiver
# origin X, origin Y, Vector X, Vector Y
ax.quiver(0, 0, ax_val, ay_val, angles='xy', scale_units='xy', scale=1, color='blue', label='Vector A')
ax.quiver(0, 0, bx_val, by_val, angles='xy', scale_units='xy', scale=1, color='red', label='Vector B')
ax.quiver(0, 0, rx_val, ry_val, angles='xy', scale_units='xy', scale=1, color='green', width=0.008, label='Resultant R')

# Draw Parallelogram dotted lines
ax.plot([ax_val, rx_val], [ay_val, ry_val], 'b--') # Line from tip of A to tip of R
ax.plot([bx_val, rx_val], [by_val, ry_val], 'r--') # Line from tip of B to tip of R

# Grid and Formatting
limit = max(10, abs(rx_val) + 2, abs(ry_val) + 2)
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.axhline(0, color='black',linewidth=1)
ax.axvline(0, color='black',linewidth=1)
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
ax.set_aspect('equal')
ax.legend()

st.pyplot(fig)
