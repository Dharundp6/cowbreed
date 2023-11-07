import streamlit as st
import cv2
import tempfile
from ultralytics import YOLO
from PIL import Image

def sort_array_func(val):
    return val[3]

st.set_page_config(page_title="")

hide_st_style = """
            <style>
            # MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            # header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("")

choice = st.selectbox("select",["Upload image","Real Time"])
conf = st.number_input("conf",0.2)

if choice == "Upload image":
    
    image_data = st.file_uploader("Upload the Image")
    img_summit_button = st.button("Predict")
    
    if img_summit_button:
        
        model = YOLO('/home/sudharsan/Documents/Projects/Tomato_disease_detector_project/best27.pt')   
    
        image = Image.open(image_data)
        image.save("input_data_image.png")
        frame = cv2.imread("input_data_image.png")
        frame_without_condition = frame
                
        results = model.predict(source=frame,iou=0.7,conf= conf)
        plot_show =  results[0].plot()
        get_array = results[0].boxes.numpy().boxes.tolist()

        # function to sort array 
        get_array.sort(key=sort_array_func)

        cv2.putText(plot_show,"" + str(len(get_array)),(50,50),cv2.COLOR_BGR2GRAY,2,(255,0,0),2) 
        st.image(plot_show)
        #------------------------------------------ model predicted result all boxes ------------------------------------------#
        for ind,i in enumerate(get_array):
            cv2.rectangle(frame_without_condition,(int(i[0]),int(i[1])), (int(i[2]), int(i[3])),(255,0,0),2)
            cv2.putText(frame_without_condition,str(ind+1),(int(i[0])-70,int(i[1])+10),cv2.COLOR_BGR2GRAY,1.5,(255,0,0),2,cv2.LINE_AA) 
            cv2.line(frame_without_condition,pt1=(int(i[0]),int(i[1])+10),pt2=(int(i[0])-40,int(i[1])+5),color=(0,0,255),thickness=2)                
                    
        count = str(len(get_array))
        frame_without_condition = cv2.resize(frame_without_condition,(200,750))
        cv2.putText(frame_without_condition,""+ str(len(get_array)),(1,680),cv2.COLOR_BGR2GRAY,1,(255,0,0),2) 

        
        classes_model = model.names 
          
        detected_list = [ classes_model[i] for  i in results[0].boxes.cls.tolist()]