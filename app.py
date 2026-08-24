import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Page config - Set layout to "wide"
st.set_page_config(page_title="Vector Addition Visualizer", page_icon="📐", layout="wide")

# Title ne columns ni upar rakhiye jethi top thi alignment perfect aave
st.title("📐 Vector Addition Visualizer")
st.caption("Day 1 of 30: Physics Simulators Challenge")
st.markdown("---")

# 2. FIXED: Create EQUAL columns (50% - 50%) with a gap for better recording
col_input, col_graph = st.columns(2, gap="large")

with col_input:
    st.markdown("#### Adjust the X and Y components:")
    
    st.subheader("Vector A (Blue)")
    ax_val = st.slider("A_x component", -10.0, 10.0, 4.0, step=1.0)
    ay_val = st.slider("A_y component", -10.0, 10.0, 6.0, step=1.0)

    st.markdown("<br>", unsafe_allow_html=True) # Adds a little vertical breathing space

    st.subheader("Vector B (Red)")
    bx_val = st.slider("B_x component", -10.0, 10.0, 5.0, step=1.0)
    by_val = st.slider("B_y component", -10.0, 10.0, -3.0, step=1.0)

# Physics / Math Calculations
rx_val = ax_val + bx_val
ry_val = ay_val + by_val
magnitude = np.sqrt(rx_val**2 + ry_val**2)
angle = np.degrees(np.arctan2(ry_val, rx_val))

with col_graph:
    # Display Result text exactly above the graph
    st.success(f"**Resultant Vector R** = {rx_val} î + {ry_val} ĵ  |  **Magnitude**: {magnitude:.2f}  |  **Angle**: {angle:.2f}°")
    
    # Plotting - Reduced figsize slightly so it doesn't take too much vertical height
    fig, ax = plt.subplots(figsize=(6, 6))

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

    # Render the graph and force it to fit perfectly within its half of the screen
    st.pyplot(fig, use_container_width=True)
