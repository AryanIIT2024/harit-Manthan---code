# # import streamlit as st
# # import pandas as pd
# # import random
# # import time
# # import numpy as np
# # import os
# # import json
# # from datetime import datetime
# # import firebase_admin
# # from firebase_admin import credentials, db
# # from streamlit_autorefresh import st_autorefresh


# # st.set_page_config(page_title="VanaRaksha Cloud Dashboard", layout="wide")


# # if not firebase_admin._apps:
# #     try:
# #         if "FIREBASE_JSON" in os.environ:
# #             key_dict = json.loads(os.environ["FIREBASE_JSON"])
# #             cred = credentials.Certificate(key_dict)
# #         else:
# #             cred = credentials.Certificate("vanaraksha-key.json") 
            
# #         firebase_admin.initialize_app(cred, {
# #             'databaseURL': 'https://vanraksha-2026-default-rtdb.firebaseio.com/'
# #         })
# #     except Exception as e:
# #         st.error(f"Firebase Initialization Error: {e}")


# # if 'role' not in st.session_state: st.session_state['role'] = None
# # if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
# # if 'is_resolving' not in st.session_state: st.session_state['is_resolving'] = False


# # def role_selection():
# #     st.markdown("<h1 style='text-align: center;'>VanaRaksha Intelligence Network</h1>", unsafe_allow_html=True)
# #     st.markdown("<h4 style='text-align: center;'>Harit Manthan 2026 - National Hackathon</h4>", unsafe_allow_html=True)
    
# #     col1, col2 = st.columns(2)
# #     with col1:
# #         if st.button(" CITIZEN PORTAL", use_container_width=True):
# #             st.session_state['role'] = 'Citizen'
# #             st.rerun()
# #     with col2:
# #         if st.button(" DDA OFFICER LOGIN", use_container_width=True):
# #             st.session_state['role'] = 'Admin'
# #             st.rerun()


# # def citizen_portal():
# #     st.title(" Citizen Reporting Portal")
# #     if st.button("← Back to Home"):
# #         st.session_state['role'] = None
# #         st.rerun()
    
# #     with st.form("reporting_form", clear_on_submit=True):
# #         col_n, col_m = st.columns(2)
# #         with col_n: c_name = st.text_input("Full Name")
# #         with col_m: c_mobile = st.text_input("Mobile Number", max_chars=10)
            
# #         p_name = st.selectbox("Select Park Location", ["Park A", "Park B", "Park C"])
# #         i_type = st.selectbox("Issue Category", ["Dead Plant", "Broken Bench", "Water Leakage", "Garbage"])
# #         desc = st.text_area("Problem Description")
        
    
# #         img = st.file_uploader("Upload Photo Evidence", type=['jpg','png','jpeg'])
        
# #         if st.form_submit_button("Submit & Generate OTP"):
# #             if c_name and c_mobile and desc:
# #                 otp = str(random.randint(1000, 9999))
# #                 complaint_id = f"VAN-{random.randint(100, 999)}"
# #                 try:
# #                     db.reference('complaints').child(complaint_id).set({
# #                         'citizen_name': c_name, 'mobile': c_mobile, 'park': p_name,
# #                         'issue': i_type, 'otp': otp, 'status': 'Pending',
# #                         'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# #                     })
# #                     st.success(f" Complaint {complaint_id} saved!")
# #                     st.warning(f" YOUR OTP: {otp}")
# #                 except Exception as e:
# #                     st.error(f"Database Error: {e}")


# # def admin_portal():
# #     if not st.session_state['logged_in']:
# #         if st.button("← Back"):
# #             st.session_state['role'] = None
# #             st.rerun()
# #         st.subheader(" Officer Authentication")
# #         user = st.text_input("Username")
# #         pwd = st.text_input("Password", type="password")
# #         if st.button("Login"):
# #             if user == "ElectroNinjas" and pwd == "1234":
# #                 st.session_state['logged_in'] = True
# #                 st.rerun()
# #             else:
# #                 st.error("Invalid Credentials")
# #         return

# #     if not st.session_state['is_resolving']:
# #         st_autorefresh(interval=30000, key="sensor_refresh")

# #     st.sidebar.title(" DDA Park Folders")
# #     selected_park = st.sidebar.selectbox("Go to Folder", ["Park A", "Park B", "Park C"])
    
# #     if st.sidebar.button("Logout & Switch Role"):
# #         st.session_state['logged_in'] = False
# #         st.session_state['role'] = None
# #         st.rerun()

# #     st.title(f" Admin: {selected_park} Monitor")

# #     try:
# #         s_data = db.reference('sensor_data').get()
# #         raw_t = s_data.get('temp', 25)
# #         raw_g = s_data.get('gas', 120)
# #         h = s_data.get('hum', 50)
# #         m = s_data.get('moisture', 60)
# #         fert = s_data.get('fertility', 50)
# #     except:
# #         raw_t, raw_g, h, m, fert = 25, 120, 50, 60, 50

# #     if raw_t > 33:
# #         g = int(raw_g * 1.4) 
# #         temp_status = "High Heat"
# #     else:
# #         g = raw_g
# #         temp_status = " Stable"


# #     if g <= 100:
# #         aqi_color, aqi_text = "#2ecc71", "Good"
# #     elif g <= 250:
# #         aqi_color, aqi_text = "#f39c12", "Moderate"
# #     else:
# #         aqi_color, aqi_text = "#e74c3c", "Hazardous"


# #     gas_impact = max(0, 100 - (g/5))
# #     ghs_score = int((m + gas_impact + (fert*0.5)) / 2.5)

# #     col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)
# #     col_kpi1.metric("Green Health Score", f"{ghs_score}%")
# #     col_kpi2.metric("Soil Moisture", f"{m}%")
# #     col_kpi3.metric("Live AQI", f"{g}", delta=temp_status, delta_color="inverse" if raw_t > 33 else "normal")
# #     col_kpi4.metric("Temperature", f"{raw_t}°C")


# #     st.markdown(f"""
# #         <div style="background-color: {aqi_color}; padding: 15px; border-radius: 10px; color: white; text-align: center;">
# #             <h3 style="margin:0;">Air Quality Status: {aqi_text}</h3>
# #             <p style="margin:0;">Ambient Adjusted for {raw_t}°C Heat Index</p>
# #         </div>
# #     """, unsafe_allow_html=True)
    
# #     st.divider()

    
# #     col_m1, col_m2 = st.columns(2)
# #     with col_m1:
# #         st.subheader("Sensor Kit Layout")
# #         map_data = pd.DataFrame({'lat': [28.5933], 'lon': [77.2189]})
# #         st.map(map_data)
# #     with col_m2:
# #         st.subheader(" High-Density Ecological Trends")
# #         chart_data = pd.DataFrame({'Moisture': [m-2, m+1, m], 'AQI': [g+5, g-2, g]})
# #         st.line_chart(chart_data)

# #     st.divider()


# #     col_c1, col_c2 = st.columns(2)
# #     with col_c1:
# #         st.subheader("Demo image of parks")
# #         st.image("https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=500", caption="Vision Analysis Online")
# #         st.write(f"**Humidity:** {h}% | **NPK:** {fert}")

# #     with col_c2:
# #         st.subheader(" Complaints (Live Firebase Data)")
# #         if st.checkbox(" Lock Screen to Resolve", value=st.session_state['is_resolving']):
# #             st.session_state['is_resolving'] = True
# #         else:
# #             st.session_state['is_resolving'] = False

# #         try:
# #             all_data = db.reference('complaints').get()
# #             if all_data:
# #                 for cid in all_data:
# #                     val = all_data[cid]
# #                     if val['status'] == 'Pending' and val['park'] == selected_park:
# #                         with st.expander(f" CASE {cid}: {val['issue']}"):
# #                             st.write(f"**Citizen:** {val['citizen_name']} | **Mobile:** {val['mobile']}")
# #                             v_otp = st.text_input("Enter OTP", key=f"in_{cid}")
# #                             if st.button("Resolve", key=f"bt_{cid}"):
# #                                 if v_otp == val['otp']:
# #                                     db.reference('complaints').child(cid).update({'status': 'Resolved'})
# #                                     st.success("Resolved!")
# #                                     st.session_state['is_resolving'] = False 
# #                                     time.sleep(1)
# #                                     st.rerun()
# #                                 else:
# #                                     st.error("Invalid OTP")
# #             else:
# #                 st.write("No complaints.")
# #         except Exception as e:
# #             st.error(f"Error: {e}")

# # if st.session_state['role'] == 'Citizen':
# #     citizen_portal()
# # elif st.session_state['role'] == 'Admin':
# #     admin_portal()
# # else:
# #     role_selection()

# import streamlit as st
# import pandas as pd
# import random
# import time
# import numpy as np
# import os
# import json
# from datetime import datetime
# import firebase_admin
# from firebase_admin import credentials, db
# from streamlit_autorefresh import st_autorefresh

# # --- CONFIGURATION ---
# st.set_page_config(page_title="VanaRaksha Cloud Dashboard", layout="wide")

# # --- FIREBASE INITIALIZATION ---
# if not firebase_admin._apps:
#     try:
#         if "FIREBASE_JSON" in os.environ:
#             key_dict = json.loads(os.environ["FIREBASE_JSON"])
#             cred = credentials.Certificate(key_dict)
#         else:
#             cred = credentials.Certificate("vanaraksha-key.json") 
            
#         firebase_admin.initialize_app(cred, {
#             'databaseURL': 'https://vanraksha-2026-default-rtdb.firebaseio.com/'
#         })
#     except Exception as e:
#         st.error(f"Firebase Initialization Error: {e}")

# # --- SESSION STATE ---
# if 'role' not in st.session_state: st.session_state['role'] = None
# if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
# if 'is_resolving' not in st.session_state: st.session_state['is_resolving'] = False

# # --- UI COMPONENTS ---

# def role_selection():
#     st.markdown("<h1 style='text-align: center;'>VanaRaksha Intelligence Network</h1>", unsafe_allow_html=True)
#     st.markdown("<h4 style='text-align: center;'>Harit Manthan 2026 - National Hackathon</h4>", unsafe_allow_html=True)
    
#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button("👥 CITIZEN PORTAL", use_container_width=True):
#             st.session_state['role'] = 'Citizen'
#             st.rerun()
#     with col2:
#         if st.button("👮 DDA OFFICER LOGIN", use_container_width=True):
#             st.session_state['role'] = 'Admin'
#             st.rerun()

# def citizen_portal():
#     st.title("📩 Citizen Reporting Portal")
#     if st.button("← Back to Home"):
#         st.session_state['role'] = None
#         st.rerun()
    
#     with st.form("reporting_form", clear_on_submit=True):
#         col_n, col_m = st.columns(2)
#         with col_n: c_name = st.text_input("Full Name")
#         with col_m: c_mobile = st.text_input("Mobile Number", max_chars=10)
            
#         p_name = st.selectbox("Select Park Location", ["Park A", "Park B", "Park C"])
#         i_type = st.selectbox("Issue Category", ["Dead Plant", "Broken Bench", "Water Leakage", "Garbage"])
#         desc = st.text_area("Problem Description")
        
#         img = st.file_uploader("Upload Photo Evidence", type=['jpg','png','jpeg'])
        
#         if st.form_submit_button("Submit & Generate OTP"):
#             if c_name and c_mobile and desc:
#                 otp = str(random.randint(1000, 9999))
#                 complaint_id = f"VAN-{random.randint(100, 999)}"
#                 try:
#                     db.reference('complaints').child(complaint_id).set({
#                         'citizen_name': c_name, 'mobile': c_mobile, 'park': p_name,
#                         'issue': i_type, 'otp': otp, 'status': 'Pending',
#                         'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                     })
#                     st.success(f"✅ Complaint {complaint_id} saved!")
#                     st.warning(f"🔑 YOUR OTP: {otp}")
#                 except Exception as e:
#                     st.error(f"Database Error: {e}")

# def admin_portal():
#     if not st.session_state['logged_in']:
#         if st.button("← Back"):
#             st.session_state['role'] = None
#             st.rerun()
#         st.subheader("🔐 Officer Authentication")
#         user = st.text_input("Username")
#         pwd = st.text_input("Password", type="password")
#         if st.button("Login"):
#             if user == "ElectroNinjas" and pwd == "1234":
#                 st.session_state['logged_in'] = True
#                 st.rerun()
#             else:
#                 st.error("Invalid Credentials")
#         return

#     if not st.session_state['is_resolving']:
#         st_autorefresh(interval=30000, key="sensor_refresh")

#     st.sidebar.title("🌳 DDA Park Folders")
#     selected_park = st.sidebar.selectbox("Go to Folder", ["Park A", "Park B", "Park C"])
    
#     if st.sidebar.button("Logout & Switch Role"):
#         st.session_state['logged_in'] = False
#         st.session_state['role'] = None
#         st.rerun()

#     st.title(f"📊 Admin: {selected_park} Monitor")

#     # --- SENSOR LOGIC ---
#     try:
#         s_data = db.reference('sensor_data').get()
#         raw_t = s_data.get('temp', 25)
#         raw_g = s_data.get('gas', 120)
#         h = s_data.get('hum', 50)
#         m = s_data.get('moisture', 60)
#         fert = s_data.get('fertility', 50)
#     except:
#         raw_t, raw_g, h, m, fert = 25, 120, 50, 60, 50

#     if raw_t > 33:
#         g = int(raw_g * 1.4) 
#         temp_status = "High Heat"
#     else:
#         g = raw_g
#         temp_status = "Stable"

#     if g <= 100:
#         aqi_color, aqi_text = "#2ecc71", "Good"
#     elif g <= 250:
#         aqi_color, aqi_text = "#f39c12", "Moderate"
#     else:
#         aqi_color, aqi_text = "#e74c3c", "Hazardous"

#     gas_impact = max(0, 100 - (g/5))
#     ghs_score = int((m + gas_impact + (fert*0.5)) / 2.5)

#     # --- TOP KPI METRICS ---
#     col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)
#     col_kpi1.metric("Green Health Score", f"{ghs_score}%")
#     col_kpi2.metric("Soil Moisture", f"{m}%")
#     col_kpi3.metric("Live AQI", f"{g}", delta=temp_status, delta_color="inverse" if raw_t > 33 else "normal")
#     col_kpi4.metric("Temperature", f"{raw_t}°C")

#     st.markdown(f"""
#         <div style="background-color: {aqi_color}; padding: 15px; border-radius: 10px; color: white; text-align: center;">
#             <h3 style="margin:0;">Air Quality Status: {aqi_text}</h3>
#             <p style="margin:0;">Ambient Adjusted for {raw_t}°C Heat Index</p>
#         </div>
#     """, unsafe_allow_html=True)
    
#     st.divider()

#     # --- IMPACT ANALYTICS (NEW SECTION) ---
#     st.header("📈 VanaRaksha Impact Analytics")
#     st.caption("Strategic comparisons of Smart Kits vs Traditional Maintenance Methods")
    
#     tab1, tab2, tab3, tab4 = st.tabs([
#         "💧 Water Efficiency", "🌿 Plant Health", "🌬️ Pollution Control", "⚙️ Op-Efficiency"
#     ])

#     with tab1:
#         st.subheader("Smart Irrigation Savings")
#         st.image("Code_Generated_Image (3).png", use_container_width=True)
#         st.info("Benefit: Automated Drip actuators reduce weekly water consumption by ~70% compared to flood methods.")

#     with tab2:
#         st.subheader("Long-term Growth Index")
#         st.image("Code_Generated_Image (2).png", use_container_width=True)
#         st.info("Benefit: Data-driven nutrient management ensures steady biomass growth without health dips.")

#     with tab3:
#         st.subheader("Pollution Mitigation Impact")
#         st.image("Code_Generated_Image (1).png", use_container_width=True)
#         st.info("Benefit: Localized control systems help maintain air quality closer to WHO safe limits.")

#     with tab4:
#         st.subheader("Maintenance Efficiency")
#         st.image("Code_Generated_Image.png", use_container_width=True)
#         st.info("Benefit: Replaces manual periodic checks with 24/7 predictive alerts, boosting officer productivity.")

#     st.divider()

#     # --- MAP & TRENDS ---
#     col_m1, col_m2 = st.columns(2)
#     with col_m1:
#         st.subheader("📍 Sensor Kit Layout")
#         map_data = pd.DataFrame({'lat': [28.5933], 'lon': [77.2189]})
#         st.map(map_data)
#     with col_m2:
#         st.subheader("📈 High-Density Ecological Trends")
#         chart_data = pd.DataFrame({'Moisture': [m-2, m+1, m], 'AQI': [g+5, g-2, g]})
#         st.line_chart(chart_data)

#     st.divider()

#     # --- VISION & COMPLAINTS ---
#     col_c1, col_c2 = st.columns(2)
#     with col_c1:
#         st.subheader("🖼️ Park Vision Analysis")
#         st.image("https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=500", caption="CCTV Feed / Vision Analysis Online")
#         st.write(f"**Current Humidity:** {h}% | **Soil NPK Status:** {fert}")

#     with col_c2:
#         st.subheader("📋 Live Complaints")
#         if st.checkbox("🛑 Lock Screen to Resolve", value=st.session_state['is_resolving']):
#             st.session_state['is_resolving'] = True
#         else:
#             st.session_state['is_resolving'] = False

#         try:
#             all_data = db.reference('complaints').get()
#             if all_data:
#                 for cid in all_data:
#                     val = all_data[cid]
#                     if val['status'] == 'Pending' and val['park'] == selected_park:
#                         with st.expander(f"CASE {cid}: {val['issue']}"):
#                             st.write(f"**Citizen:** {val['citizen_name']} | **Mobile:** {val['mobile']}")
#                             v_otp = st.text_input("Enter OTP", key=f"in_{cid}")
#                             if st.button("Resolve", key=f"bt_{cid}"):
#                                 if v_otp == val['otp']:
#                                     db.reference('complaints').child(cid).update({'status': 'Resolved'})
#                                     st.success("Resolved!")
#                                     st.session_state['is_resolving'] = False 
#                                     time.sleep(1)
#                                     st.rerun()
#                                 else:
#                                     st.error("Invalid OTP")
#             else:
#                 st.write("No active complaints.")
#         except Exception as e:
#             st.error(f"Error fetching complaints: {e}")

# # --- MAIN APP FLOW ---
# if st.session_state['role'] == 'Citizen':
#     citizen_portal()
# elif st.session_state['role'] == 'Admin':
#     admin_portal()
# else:
#     role_selection()
import streamlit as st
import pandas as pd
import random
import time
import numpy as np
import os
import json
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, db
from streamlit_autorefresh import st_autorefresh
# --- NEW IMPORT FOR WEBCAM ---
from streamlit_webrtc import webrtc_streamer

# --- CONFIGURATION ---
st.set_page_config(page_title="VanaRaksha Cloud Dashboard", layout="wide")

# --- FIREBASE INITIALIZATION ---
if not firebase_admin._apps:
    try:
        if "FIREBASE_JSON" in os.environ:
            key_dict = json.loads(os.environ["FIREBASE_JSON"])
            cred = credentials.Certificate(key_dict)
        else:
            cred = credentials.Certificate("vanaraksha-key.json") 
            
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://vanraksha-2026-default-rtdb.firebaseio.com/'
        })
    except Exception as e:
        st.error(f"Firebase Initialization Error: {e}")

# --- SESSION STATE ---
if 'role' not in st.session_state: st.session_state['role'] = None
if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
if 'is_resolving' not in st.session_state: st.session_state['is_resolving'] = False

# --- UI COMPONENTS ---

def role_selection():
    st.markdown("<h1 style='text-align: center;'>VanaRaksha Intelligence Network</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Harit Manthan 2026 - National Hackathon</h4>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👥 CITIZEN PORTAL", use_container_width=True):
            st.session_state['role'] = 'Citizen'
            st.rerun()
    with col2:
        if st.button("👮 DDA OFFICER LOGIN", use_container_width=True):
            st.session_state['role'] = 'Admin'
            st.rerun()

def citizen_portal():
    st.title("📩 Citizen Reporting Portal")
    if st.button("← Back to Home"):
        st.session_state['role'] = None
        st.rerun()
    
    with st.form("reporting_form", clear_on_submit=True):
        col_n, col_m = st.columns(2)
        with col_n: c_name = st.text_input("Full Name")
        with col_m: c_mobile = st.text_input("Mobile Number", max_chars=10)
            
        p_name = st.selectbox("Select Park Location", ["Park A", "Park B", "Park C"])
        i_type = st.selectbox("Issue Category", ["Dead Plant", "Broken Bench", "Water Leakage", "Garbage"])
        desc = st.text_area("Problem Description")
        
        img = st.file_uploader("Upload Photo Evidence", type=['jpg','png','jpeg'])
        
        if st.form_submit_button("Submit & Generate OTP"):
            if c_name and c_mobile and desc:
                otp = str(random.randint(1000, 9999))
                complaint_id = f"VAN-{random.randint(100, 999)}"
                try:
                    db.reference('complaints').child(complaint_id).set({
                        'citizen_name': c_name, 'mobile': c_mobile, 'park': p_name,
                        'issue': i_type, 'otp': otp, 'status': 'Pending',
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                    st.success(f"✅ Complaint {complaint_id} saved!")
                    st.warning(f"🔑 YOUR OTP: {otp}")
                except Exception as e:
                    st.error(f"Database Error: {e}")

def admin_portal():
    if not st.session_state['logged_in']:
        if st.button("← Back"):
            st.session_state['role'] = None
            st.rerun()
        st.subheader("🔐 Officer Authentication")
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        if st.button("Login"):
            if user == "ElectroNinjas" and pwd == "1234":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Invalid Credentials")
        return

    if not st.session_state['is_resolving']:
        st_autorefresh(interval=30000, key="sensor_refresh")

    st.sidebar.title("🌳 DDA Park Folders")
    selected_park = st.sidebar.selectbox("Go to Folder", ["Park A", "Park B", "Park C"])
    
    if st.sidebar.button("Logout & Switch Role"):
        st.session_state['logged_in'] = False
        st.session_state['role'] = None
        st.rerun()

    st.title(f"📊 Admin: {selected_park} Monitor")

    # --- SENSOR LOGIC ---
    try:
        s_data = db.reference('sensor_data').get()
        raw_t = s_data.get('temp', 25)
        raw_g = s_data.get('gas', 120)
        h = s_data.get('hum', 50)
        m = s_data.get('moisture', 60)
        fert = s_data.get('fertility', 50)
    except:
        raw_t, raw_g, h, m, fert = 25, 120, 50, 60, 50

    if raw_t > 33:
        g = int(raw_g * 1.4) 
        temp_status = "High Heat"
    else:
        g = raw_g
        temp_status = "Stable"

    if g <= 100:
        aqi_color, aqi_text = "#2ecc71", "Good"
    elif g <= 250:
        aqi_color, aqi_text = "#f39c12", "Moderate"
    else:
        aqi_color, aqi_text = "#e74c3c", "Hazardous"

    gas_impact = max(0, 100 - (g/5))
    ghs_score = int((m + gas_impact + (fert*0.5)) / 2.5)

    # --- TOP KPI METRICS ---
    col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)
    col_kpi1.metric("Green Health Score", f"{ghs_score}%")
    col_kpi2.metric("Soil Moisture", f"{m}%")
    col_kpi3.metric("Live AQI", f"{g}", delta=temp_status, delta_color="inverse" if raw_t > 33 else "normal")
    col_kpi4.metric("Temperature", f"{raw_t}°C")

    st.markdown(f"""
        <div style="background-color: {aqi_color}; padding: 15px; border-radius: 10px; color: white; text-align: center;">
            <h3 style="margin:0;">Air Quality Status: {aqi_text}</h3>
            <p style="margin:0;">Ambient Adjusted for {raw_t}°C Heat Index</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()

    # --- IMPACT ANALYTICS ---
    st.header("📈 VanaRaksha Impact Analytics")
    tab1, tab2, tab3, tab4 = st.tabs(["💧 Water", "🌿 Health", "🌬️ Pollution", "⚙️ Efficiency"])
    with tab1:
        st.image("Code_Generated_Image (3).png", use_container_width=True)
    with tab2:
        st.image("Code_Generated_Image (2).png", use_container_width=True)
    with tab3:
        st.image("Code_Generated_Image (1).png", use_container_width=True)
    with tab4:
        st.image("Code_Generated_Image.png", use_container_width=True)

    st.divider()

    # --- MAP & TRENDS ---
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.subheader("📍 Sensor Kit Layout")
        map_data = pd.DataFrame({'lat': [28.5933], 'lon': [77.2189]})
        st.map(map_data)
    with col_m2:
        st.subheader("📈 High-Density Ecological Trends")
        chart_data = pd.DataFrame({'Moisture': [m-2, m+1, m], 'AQI': [g+5, g-2, g]})
        st.line_chart(chart_data)

    st.divider()

    # --- VISION & COMPLAINTS ---
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.subheader("📹 Live Park Vision (Webcam)")
        # --- WEBCAM FEED INTEGRATION ---
        webrtc_streamer(key="park-vision-feed")
        st.caption("AI-Powered Real-time Surveillance for DDA Parks")
        st.write(f"**Humidity:** {h}% | **Soil NPK:** {fert}")

    with col_c2:
        st.subheader("📋 Live Complaints")
        if st.checkbox("🛑 Lock Screen to Resolve", value=st.session_state['is_resolving']):
            st.session_state['is_resolving'] = True
        else:
            st.session_state['is_resolving'] = False

        try:
            all_data = db.reference('complaints').get()
            if all_data:
                for cid in all_data:
                    val = all_data[cid]
                    if val['status'] == 'Pending' and val['park'] == selected_park:
                        with st.expander(f"CASE {cid}: {val['issue']}"):
                            st.write(f"**Citizen:** {val['citizen_name']} | **Mobile:** {val['mobile']}")
                            v_otp = st.text_input("Enter OTP", key=f"in_{cid}")
                            if st.button("Resolve", key=f"bt_{cid}"):
                                if v_otp == val['otp']:
                                    db.reference('complaints').child(cid).update({'status': 'Resolved'})
                                    st.success("Resolved!")
                                    st.session_state['is_resolving'] = False 
                                    time.sleep(1)
                                    st.rerun()
                                else:
                                    st.error("Invalid OTP")
            else:
                st.write("No active complaints.")
        except Exception as e:
            st.error(f"Error: {e}")

# --- MAIN APP FLOW ---
if st.session_state['role'] == 'Citizen':
    citizen_portal()
elif st.session_state['role'] == 'Admin':
    admin_portal()
else:
    role_selection()