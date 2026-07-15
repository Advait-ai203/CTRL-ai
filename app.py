# app.py
import streamlit as st
import time

# Import your existing matrix tools
from tools.startup_founder_dept.investor_pitch_compiler import compile_pitch_narrative
from tools.marketing_agents.ad_copy_gen import generate_ad_copy
from tools.advanced_hardware_dept.power_draw_estimator import estimate_battery_life
from tools.team_agents.task_delegator import assign_task

# 1. Configure the Web Page
st.set_page_config(page_title="CTRL-ai Matrix", page_icon="⚡", layout="wide")

# 2. Build the UI Header
st.title("⚡ CTRL-ai Master Matrix")
st.markdown("Welcome to the autonomous intelligence framework for **ctrl** and **allmate**.")
st.divider()

# 3. Create a Sidebar Menu
st.sidebar.header("Command Modules")
module = st.sidebar.radio(
    "Select Department:",
    ("Startup Founder", "Marketing", "Hardware Engineering", "Team Operations")
)

# 4. Route to the correct tool based on user selection
if module == "Startup Founder":
    st.subheader("Investor Pitch Compiler")
    brand = st.selectbox("Select Brand Focus:", ["ctrl", "allmate"])
    if st.button("Generate Pitch"):
        with st.spinner("Compiling narrative..."):
            time.sleep(1) # Simulate matrix processing
            result = compile_pitch_narrative(brand_focus=brand)
            st.success("Pitch Ready.")
            st.markdown(result)

elif module == "Marketing":
    st.subheader("Ad Copy Generator")
    prod_name = st.text_input("Product Name (e.g., Heavyweight Hoodie)")
    val_prop = st.text_input("Core Value Proposition")
    if st.button("Generate Copy") and prod_name and val_prop:
        result = generate_ad_copy(product_name=prod_name, value_prop=val_prop)
        st.info(result)

elif module == "Hardware Engineering":
    st.subheader("Battery Life Estimator")
    mah = st.number_input("Battery Capacity (mAh)", min_value=100.0, value=3000.0)
    draw = st.number_input("System Draw (mA)", min_value=1.0, value=150.0)
    if st.button("Calculate Runtime"):
        result = estimate_battery_life(battery_capacity_mah=mah, total_current_draw_ma=draw)
        st.success(result)

elif module == "Team Operations":
    st.subheader("Task Delegator")
    task = st.text_input("Task Description")
    # Using your official roster
    assignee = st.selectbox("Assign To:", ["Advait", "Tarun", "Nicky", "Shubhansh"]) 
    if st.button("Delegate Task") and task:
        result = assign_task(task_name=task, assignee=assignee)
        st.success(result)
