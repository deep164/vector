import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Page config - Set layout to "wide"
st.set_page_config(page_title="Vector Addition Visualizer", page_icon="📐", layout="wide")

st.title("📐 Vector Addition Visualizer")
st.caption("Day 1 of 30: Physics Simulators Challenge")

# 2. Create main columns (Left for sliders, Right for graph)
# [1, 2] means the right column is twice as wide as the left one
col_input, col_graph = st.columns([1, 2])

with col_input:
    st.markdown("Adjust the X and Y components of Vectors **A** and **B**.")
    
    st.subheader("Vector A (Blue)")
    ax_val = st.slider("A_x component", -10.0, 10.0, 4.0, step=1.0)
    ay_val = st.slider("A_y component", -10.0, 10.0, 6.0, step=1.0)

    st.markdown("---") # Divider line

    st.subheader("Vector B (Red)")
    bx_val = st.slider("B_x component", -10.0, 10.0, 5.0, step=1.0)
    by_val = st.slider("B_y component", -10.0, 10.0, -3.0, step=1.0)

# Physics / Math Calculations
rx_val = ax_val + bx_val
ry_val = ay_val + by_val
magnitude = np.sqrt(rx_val**2 + ry_val**2)
angle = np.degrees(np.arctan2(ry_val, rx_val))

with col_graph:
    # Display Result text clearly above the graph
    st.success(f"**Resultant Vector R** = {rx_val} î + {ry_val} ĵ  |  **Magnitude**: {magnitude:.2f}  |  **Angle**: {angle:.2f}°")
    
    # Plotting
    fig, ax = plt.subplots(figsize=(7, 7))

    # Draw Vectors using quiver
    ax.quiver(0, 0, ax_val, ay_val, angles='xy', scale_units='xy', scale=1, color='blue', label='Vector A')
    ax.quiver(0, 0, bx_val, by_val, angles='xy', scale_units='xy', scale=1, color='red', label='Vector B')
    ax.quiver(0, 0, rx_val, ry_val, angles='xy', scale_units='xy', scale=1, color='green', width=0.008, label='Resultant R')

    # Draw Parallelogram dotted lines
    ax.plot([ax_val, rx_val], [ay_val, ry_val], 'b--') 
    ax.plot([bx_val, rx_val], [by_val, ry_val], 'r--') 

    # Grid and Formatting
    limit = max(10, abs(rx_val) + 2, abs(ry_val) + 2)
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    ax.set_aspect('equal')
    ax.legend()

    # Render the graph in the right column
    st.pyplot(fig)
