import streamlit as st
import pandas as pd
import re

def process_text_file(uploaded_file):
    lines = uploaded_file.read().decode("utf-8").split("\n")
    data_list = []
    capture_data = False

    for line in lines:
        if "CONTAINER" in line and "ITEM" in line:
            capture_data = True
            continue
        
        if capture_data and re.match(r"^\d+", line.strip()):
            container_no = line[0:10].strip()
            item_no = line[11:20].strip()
            cut_width = line[21:26].strip()
            fabric_lot = line[27:32].strip()
            finish_color = line[33:38].strip()
            status = line[39:43].strip()
            mach_no = line[44:48].strip() or ""
            bin_row = line[49:57].strip()
            finish_date = line[58:68].strip()
            finish_lbs = line[69:76].strip()
            finish_yds = line[77:84].strip()
            dye_lot = line[85:93].strip()
            grd = line[94:96].strip()
            last_act_date = line[97:107].strip()
            wo_no = line[108:114].strip()
            print_code = line[115:122].strip()
            shipment = line[123:].strip()

            data_list.append([
                container_no, item_no, cut_width, fabric_lot, finish_color, status,
                mach_no, bin_row, finish_date, finish_lbs, finish_yds,
                dye_lot, grd, last_act_date, wo_no, print_code, shipment
            ])

    columns = [
        "CONTAINER NO.", "ITEM NO.", "CUT WIDTH", "FABRIC LOT", "FINISH COLOR",
        "STATUS", "MACH NO.", "BIN/ROW", "FINISH DATE", "FINISH LBS",
        "FINISH YDS", "DYE LOT", "GRD", "LAST ACT DATE", "WO #", "PRINT CODE", "SHIPMENT"
    ]

    df = pd.DataFrame(data_list, columns=columns)
    return df