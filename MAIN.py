import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
import subprocess
import sys
import math
import datetime
from datetime import date, timedelta
import time 
import gc
import calendar
import os
import matplotlib
matplotlib.use("Agg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import threading

app = tk.Tk()
app.geometry("1280x1024")
app.attributes('-fullscreen', True)
app.configure(bg="#030068")
app.resizable(True, True)


def quit_fullscreen(event):
    app.attributes('-fullscreen', False)
app.bind('<Escape>', quit_fullscreen)

baseframe = tk.Frame(app, bg="#030068")
baseframe.pack(fill=tk.BOTH, expand=True)

def text(frame,txt,fs,x,y,anchor,background):
    text=ctk.CTkLabel(frame,text=txt,text_color="#ffffff",font=("Sofia Pro Regular",fs),fg_color="transparent",image=background)
    text.place(relx=x,rely=y,anchor=anchor)


def welcomepage():
    frame = tk.Frame(app, bg="#030068")
    frame.pack(fill=tk.BOTH, expand=True)
    #directory = os.getcwd()
    #print(directory)
    image_path = ".\\A3\\image_1.png" 
    background = ImageTk.PhotoImage(Image.open(image_path))
    label = tk.Label(frame, image=background)
    label.pack()
    
    text(frame,"Welcome!",150,0.5,0.45,"center",background)
    configure_button=ctk.CTkButton(frame, text="Configure", height=90, width=135, corner_radius=97.5, fg_color="#0e9cec", hover_color="#0b7dbd",bg_color="#020069",font=("Sofia Pro Regular",54),text_color="white",command=lambda:room_setup_page(frame))
    configure_button.place(relx=0.5,rely=0.8,anchor="center")
    
def room_setup_page(frame):
    frame.destroy()
    
    frame = tk.Frame(app, bg="#030068")
    frame.pack(fill=tk.BOTH, expand=True)
    
    image_path = ".\\A3\\image_1.png" 
    background = ImageTk.PhotoImage(Image.open(image_path))
    label = tk.Label(frame, image=background)
    label.pack()
    
    text(frame,"Kindly type your room name",70,0.5,0.1,"center",background)
    room_name_entry=ctk.CTkEntry(frame,width=750, height=120,text_color="#ffffff",font=("Sofia Pro Regular",70),
                                 fg_color="#2039a1",placeholder_text="Room name",placeholder_text_color="#6374bd",
                                 border_color="white",corner_radius=24,bg_color="#02026a",border_width=4,justify=tk.CENTER)
    room_name_entry.place(relx=0.5,rely=0.3,anchor="center")
    proceed_button=ctk.CTkButton(frame, text="Proceed", height=90, width=135, corner_radius=105, fg_color="#0e9cec", hover_color="#0b7dbd",bg_color="#020069",font=("Sofia Pro Regular",54),text_color="white",command=lambda:wifi_page(frame,room_name_entry))
    proceed_button.place(relx=0.5,rely=0.5,anchor="center")
    
def wifi_page(frame,room_name_entry):
    global room_name
    room_name=room_name_entry.get()
    frame.destroy()

    frame = tk.Frame(app, bg="#030068")
    frame.pack(fill=tk.BOTH, expand=True)

    image_path = ".\\A3\\image_1.png" 
    background = ImageTk.PhotoImage(Image.open(image_path))
    label = tk.Label(frame, image=background)
    label.pack()
    
    text(frame,"Kindly fill in your WiFi information",70,0.5,0.1,"center",background)
    
    ssid_entry=ctk.CTkEntry(frame,width=500, height=80,text_color="#ffffff",font=("Sofia Pro Regular",45),
                                 fg_color="#2039a1",placeholder_text="SSID",placeholder_text_color="#6374bd",
                                 border_color="white",corner_radius=24,bg_color="#02026a",border_width=4,justify=tk.CENTER)
    ssid_entry.place(relx=0.5,rely=0.2,anchor="center")
    
    password_entry=ctk.CTkEntry(frame,width=500, height=80,text_color="#ffffff",font=("Sofia Pro Regular",45),
                                 fg_color="#2039a1",placeholder_text="Password",placeholder_text_color="#6374bd",
                                 border_color="white",corner_radius=24,bg_color="#02026a",border_width=4,justify=tk.CENTER)
    password_entry.place(relx=0.5,rely=0.3,anchor="center")
    
    proceed_button=ctk.CTkButton(frame, text="Proceed", height=60, width=90, corner_radius=65, fg_color="#0e9cec", hover_color="#0b7dbd",
                                 bg_color="#020069",font=("Sofia Pro Regular",36),text_color="white",command=lambda:wifi_setup(frame,ssid_entry,password_entry,background))
    proceed_button.place(relx=0.5,rely=0.4,anchor="center")
    
   
    
def wifi_setup(frame,ssid_entry,password_entry,background):
    global ssid
    global password
    ssid=ssid_entry.get()
    password=password_entry.get()
    
    #Write the code for connecting wifi here using the ssid and password.
    
    if False: #Replace the false statement with the condition for a unsuccesful connection
        text(frame,"Authentication failed. Check your credentials",45,0.5,0.85,"center",background)
    
    else:
        frame.destroy()
        city_setup_page()   

def city_setup_page():    
    frame = tk.Frame(app, bg="#030068")
    frame.pack(fill=tk.BOTH, expand=True)

    image_path = ".\\A3\\image_1.png" 
    background = ImageTk.PhotoImage(Image.open(image_path))
    label = tk.Label(frame, image=background)
    label.pack()
    
    text(frame,"Kindly type your city",70,0.5,0.1,"center",background)
    
    city_name_entry=ctk.CTkEntry(frame,width=500, height=80,text_color="#ffffff",font=("Sofia Pro Regular",45),
                                 fg_color="#2039a1",placeholder_text="City name",placeholder_text_color="#6374bd",
                                 border_color="white",corner_radius=24,bg_color="#02026a",border_width=4,justify=tk.CENTER)
    city_name_entry.place(relx=0.5,rely=0.3,anchor="center")

    proceed_button=ctk.CTkButton(frame, text="Proceed", height=60, width=90, corner_radius=65, fg_color="#0e9cec", hover_color="#0b7dbd",bg_color="#020069",font=("Sofia Pro Regular",36),text_color="white",command=lambda:details_saver(frame,city_name_entry))
    proceed_button.place(relx=0.5,rely=0.5,anchor="center")
     
def details_saver(frame,city_name_entry):
    city_name=city_name_entry.get()
    frame.destroy()  
    f=open("Validator.txt","w")
    global details
    details=[room_name,ssid,password,city_name]
    for i in details:
        f.write(i+ '\n')
    f.close() 
    
    off_dashboard()
     
def off_dashboard():
    f=open("Validator.txt","r")
    global details
    details=[]
    
    for line in f.readlines():
        details.append(line.strip())
    global city_name
    city_name=details[3]
    
    global off_dashboard_field_area
    def off_dashboard_field_area():
        frame = tk.Frame(app, bg="#030068")
        frame.pack(fill=tk.BOTH, expand=True)
        my_image = ctk.CTkImage(light_image=Image.open(".\\A3\\image_2.png"),size=(1280,1024))
        image_label = ctk.CTkLabel(frame, image=my_image, text="")  
        image_label.pack(fill=tk.BOTH, expand=True)
            
        def update_time():
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            time_label.configure(text=current_time)
            frame.after(1000, update_time)
        time_label=ctk.CTkLabel(frame,text="",text_color="#10a9ff",font=("Sofia Pro SemiBold",105/1.22),fg_color="#022e81",justify="left")
        time_label.place(relx=0.380,rely=0.225,anchor="w")
        update_time()
        
        def update_time_date():
            current_time_date = datetime.datetime.now().strftime("%b %d, %Y | %I:%M %p")  # Format time as "MMM DD, YYYY - HH:MM pm"
            date_time.configure(text=current_time_date)
            frame.after(1000, update_time_date)
        date_time = ctk.CTkLabel(frame, text="", text_color="#ffffff", font=("Sofia Pro Regular", 26/1.22), fg_color="#022372")
        date_time.place(relx=0.675, rely=0.032)
        update_time_date()

        def update_date():
            current_date = datetime.datetime.now().strftime("%A, %B %d %Y")
            date.configure(text=current_date)
            frame.after(1000, update_date)
        date = ctk.CTkLabel(frame, text="", text_color="#ffffff", font=("Sofia Pro Regular", 28/1.22), fg_color="#022e81",justify="left")
        date.place(relx=0.385, rely=0.32, anchor="w")
        update_date()
        current_time = datetime.datetime.now().time()
        print("Current time:", current_time)
        weather_query(city_name)

        def weather_display(): 
            ctc = ctk.CTkLabel(frame, text=weather["current_temperature_celsius"], font=("Sofia Pro Semibold", 190/1.22), text_color="#ffffff",fg_color="#134bb7")
            ctc.place(relx=0.095, rely=0.23, anchor="center")
            
            ctc1 = ctk.CTkLabel(frame, text="Current weather", font=("Sofia Pro Regular", 25/1.22), text_color="#ffffff",fg_color="#134bb7")
            ctc1.place(relx=0.088, rely=0.13, anchor="center") 
            
            weathericon=ctk.CTkImage(light_image=Image.open(".\\A3\\" + weather["status"]+".png"),
                                        size=(200/1.22,200/1.22))
            weather_icon = ctk.CTkLabel(frame, image=weathericon, text="",bg_color="#134bb7",corner_radius=35)  
            weather_icon.place(relx=0.28, rely=0.25, anchor="center")
            
            feels_like_label=ctk.CTkLabel(frame, text=weather["status_label"]+". Feels like "+weather["feels_like"]+"°C", font=("Sofia Pro Regular", 26/1.22), text_color="#ffffff",fg_color="#134bb7")
            feels_like_label.place(relx=0.11, rely=0.35, anchor="center") 
            
            precipitation_label=ctk.CTkLabel(frame,text=weather["precipitation"],text_color="#d2def4",font=("Sofia Pro Regular",21/1.22),justify="left",bg_color="#134bb7")
            precipitation_label.place(relx=0.119,rely=0.398,anchor="w")
            
            humidity_label=ctk.CTkLabel(frame,text=weather["humidity"],text_color="#d2def4",font=("Sofia Pro Regular",21/1.22),justify="left",bg_color="#134bb7")
            humidity_label.place(relx=0.095,rely=0.4375,anchor="w")
            
            wind_label=ctk.CTkLabel(frame,text=weather["wind"],text_color="#d2def4",font=("Sofia Pro Regular",21/1.22),justify="left",bg_color="#134bb7")
            wind_label.place(relx=0.072,rely=0.478,anchor="w")
            
            hpa_label=ctk.CTkLabel(frame,text=weather["hpa"],text_color="#d2def4",font=("Sofia Pro Regular",21/1.22),justify="left",bg_color="#134bb7")
            hpa_label.place(relx=0.225,rely=0.398,anchor="w")
            
            uv_label=ctk.CTkLabel(frame,text=weather["uv"],text_color="#d2def4",font=("Sofia Pro Regular",21/1.22),justify="left",bg_color="#134bb7")
            uv_label.place(relx=0.228,rely=0.4375,anchor="w")
            
            visibility_label=ctk.CTkLabel(frame,text=weather["visibility"],text_color="#d2def4",font=("Sofia Pro Regular",21/1.22),justify="left",bg_color="#134bb7")
            visibility_label.place(relx=0.26,rely=0.478,anchor="w")

            city_airqualitylabel=ctk.CTkLabel(frame, text=city_name+" Air Quality", text_color="#ffffff", font=("Sofia Pro Regular", 30/1.22), fg_color="#022e81",justify="left")
            city_airqualitylabel.place(relx=0.728, rely=0.136,anchor="w")
            
            city_name_label=ctk.CTkLabel(frame, text=city_name, text_color="#ffffff", font=("Sofia Pro Regular", 30/1.22), fg_color="#022e81",justify="left")
            city_name_label.place(relx=0.424, rely=0.134,anchor="w")
            
            aqilabel=ctk.CTkLabel(frame, text=air_quality["aqi"], text_color="#ffffff", font=("Sofia Pro Regular", 45/1.22), fg_color="#022e81")
            aqilabel.place(relx=0.7935, rely=0.26,anchor="ne")
            
            primary_pollutant=ctk.CTkLabel(frame, text=air_quality["pm10"], text_color="#ffffff", font=("Sofia Pro Regular", 35/1.22), fg_color="#022e81")
            primary_pollutant.place(relx=0.9, rely=0.4,anchor="ne")
            
            p25label=ctk.CTkLabel(frame, text=air_quality["pm25"]+" (PM 2.5)", text_color="#56c0ed", font=("Sofia Pro Regular",18/1.22), fg_color="#022e81")
            p25label.place(relx=0.758, rely=0.545,anchor="ne")
            
            pm10label=ctk.CTkLabel(frame, text=air_quality["pm10"]+" (PM 10)", text_color="#56c0ed", font=("Sofia Pro Regular",18/1.22), fg_color="#022e81")
            pm10label.place(relx=0.86, rely=0.545,anchor="ne")
            
            so2label=ctk.CTkLabel(frame, text=air_quality["so2"]+" (SO2)", text_color="#56c0ed", font=("Sofia Pro Regular",18/1.22), fg_color="#022e81")
            so2label.place(relx=0.954, rely=0.545,anchor="ne")
            
            colabel=ctk.CTkLabel(frame, text=air_quality["co"]+" (CO)", text_color="#56c0ed", font=("Sofia Pro Regular",18/1.22), fg_color="#022e81")
            colabel.place(relx=0.745, rely=0.67,anchor="ne")
            
            ozonelabel=ctk.CTkLabel(frame, text=air_quality["ozone"]+" (Ozone)", text_color="#56c0ed", font=("Sofia Pro Regular",18/1.22), fg_color="#022e81")
            ozonelabel.place(relx=0.86, rely=0.67,anchor="ne")
            
            no2label=ctk.CTkLabel(frame, text=air_quality["no2"]+" (SO2)", text_color="#56c0ed", font=("Sofia Pro Regular",18/1.22), fg_color="#022e81")
            no2label.place(relx=0.954, rely=0.67,anchor="ne")
            
            if  int(air_quality["aqi"]) >=0 and int(air_quality["aqi"])<50:
                face=".\\A3\\50face.png"
                
            elif int(air_quality["aqi"]) >=50 and int(air_quality["aqi"])<100:
                face=".\\A3\\100face.png"
                
            elif int(air_quality["aqi"]) >=100 and int(air_quality["aqi"])<200:
                face=".\\A3\\200face.png"
                
            elif int(air_quality["aqi"]) >=200 and int(air_quality["aqi"])<300:
                face=".\\A3\\300face.png"
                
            elif int(air_quality["aqi"]) >=300 and int(air_quality["aqi"])<400:
                face=".\\A3\\400face.png"
                
            elif  int(air_quality["aqi"]) >=400:
                face=".\\A3\\500face.png"
            
            face_icon=ctk.CTkImage(light_image=Image.open(face),
                                        size=(100/1.22,200/1.22))
            face_place = ctk.CTkLabel(frame, image=face_icon, text="",bg_color="#022e81",corner_radius=35)  
            face_place.place(relx=0.91, rely=0.29, anchor="center")
            major_pollutants_label=ctk.CTkLabel(frame, text="Major Pollutants in "+city_name, font=("Sofia Pro Regular", 26/1.22), bg_color="#022e81", corner_radius=35,justify="left")
            major_pollutants_label.place(relx=0.82, rely=0.47, anchor="center")
            last_update_label=ctk.CTkLabel(frame, text="Last Update: "+last_update , font=("Sofia Pro Regular", 22/1.22), bg_color="#022e81", corner_radius=35,justify="left")
            last_update_label.place(relx=0.83, rely=0.75, anchor="center")
            positions = [0.052, 0.118, 0.183, 0.249, 0.314]  # X positions for the labels

            for i, (day, data) in enumerate(forecast.items()):
                forecast_icon = ctk.CTkImage(light_image=Image.open(".\\A3\\"+ data["status"] + ".png"), size=(60/1.22, 60/1.22))
                label = ctk.CTkLabel(frame, image=forecast_icon, text="", bg_color="#4e78c9", corner_radius=35)
                label.place(relx=positions[i], rely=0.612, anchor="center")

                day_label = ctk.CTkLabel(frame, text=data["day"], font=("Sofia Pro Regular", 20/1.22), bg_color="#4e78c9", corner_radius=35)
                day_label.place(relx=positions[i], rely=0.57, anchor="center")

                min_max_label = ctk.CTkLabel(frame, text=data["max"] + "    " + data["min"], font=("Sofia Pro Regular", 18.5/1.22), bg_color="#4e78c9", corner_radius=35)
                min_max_label.place(relx=positions[i], rely=0.655, anchor="center")

        weather_display()     
        current_time = datetime.datetime.now().time()
        print("Current time:", current_time)
        sun_position_figure(frame,"6:31am","6:41pm")
        
        electricity_info()
        
        voltage_label=ctk.CTkLabel(frame, text=voltage+"V", font=("Sofia Pro Regular", 21/1.22), bg_color="#022372", corner_radius=35,justify="center")
        voltage_label.place(relx=0.395, rely=0.0375, anchor="center")
        
        current_label=ctk.CTkLabel(frame, text=current+"A", font=("Sofia Pro Regular", 21/1.22), bg_color="#022372", corner_radius=35,justify="center")
        current_label.place(relx=0.467, rely=0.0375, anchor="center")
        
        pwr_consump_text=ctk.CTkLabel(frame, text=power_consumption_monthly[calendar.month_name[datetime.datetime.now().month]], font=("Sofia Pro Regular", 42/1.22), bg_color="#2355b4", corner_radius=35)
        pwr_consump_text.place(relx=0.512, rely=0.515, anchor="center")
        
        pwr_consump_sav_text=ctk.CTkLabel(frame, text="Savings "+power_consumption_savings_monthly[calendar.month_name[datetime.datetime.now().month]]+" units", font=("Sofia Pro Regular", 24/1.22), bg_color="#022e81", corner_radius=35,justify="center")
        pwr_consump_sav_text.place(relx=0.508, rely=0.65, anchor="center")
        
        def combobox_callback(choice):
            pwr_consump_text.configure(text=power_consumption_monthly[choice])
            pwr_consump_sav_text.configure(text="Savings "+power_consumption_savings_monthly[choice]+" units")
        pwr_consump_dropdown = ctk.CTkComboBox(frame,font=("Sofia Pro Regular", 18/1.22),dropdown_fg_color="#010061",dropdown_font=("Sofia Pro Regular", 25/1.22),width=115
                                            ,fg_color="#010061",button_color="#010061",border_color="#010061",bg_color="#022e81",corner_radius=8,
                                            values=["January","February","March","April","May","June","July","August","September","October","November","December"],
                                            command=combobox_callback)
        pwr_consump_dropdown.place(relx=0.557,rely=0.388)
        pwr_consump_dropdown.set(calendar.month_name[datetime.datetime.now().month]) 
        
        labels = ["5", "10", "15", "20", "25", "30"]
        values = power_charge_monthly_breakdown[calendar.month_name[datetime.datetime.now().month]]
        sub_values=power_unit_monthly_breakdown[calendar.month_name[datetime.datetime.now().month]]
        global fig1    
        fig1 = plt.figure(figsize=(3.79999,2.1))
        fig1.patch.set_visible(False)

        # Create a subplot in the figure
        ax1 = fig1.add_subplot(111)
        # Plot the bar chart with specified color
        ax1.bar(labels, values, color='#10a9ff',width=0.4)

        # Remove the box around the subplot
        ax1.spines['top'].set_visible(False)
        ax1.spines['right'].set_visible(False)
        ax1.spines['bottom'].set_visible(True)
        ax1.spines['left'].set_visible(True)


        # Set the background color of the subplot
        ax1.set_facecolor('#022e81')
        
        for label, value, sub_value in zip(labels, values, sub_values):
            ax1.text(label, value, str(sub_value)+"kWh", ha='center', va='bottom', color='#9aabcd')

        ax1.set_xticklabels(labels, color='white')
        yticks=[]
        for i in ax1.get_yticks():
            yticks.append(int(i))
        ax1.set_yticklabels(yticks, color='white')
        global basecanvas
        basecanvas = tk.Canvas(frame, width=360, height=220, bg="#022e81",borderwidth=1, highlightthickness=0)
        basecanvas.place(relx=0.371,rely=0.753)
        # Create a Tkinter canvas that can display the bar chart
        global canvas
        canvas = FigureCanvasTkAgg(fig1, master=basecanvas)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.53,rely=0.5,anchor="center")
        canvas.get_tk_widget().config(bg="#022e81")
        def combobox_callback2(choice):
            global values, sub_values
            values = power_charge_monthly_breakdown[choice]
            sub_values=power_unit_monthly_breakdown[choice]
            global fig
            fig = plt.figure(figsize=(3.79999,2.1))
            fig.patch.set_visible(False)

            # Create a subplot in the figure
            ax = fig.add_subplot(111)

            # Plot the bar chart with specified color
            ax.bar(labels, values, color='#10a9ff',width=0.4)

            # Remove the box around the subplot
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['bottom'].set_visible(True)
            ax.spines['left'].set_visible(True)

        
            # Set the background color of the subplot
            ax.set_facecolor('#022e81')
            
            for label, value, sub_value in zip(labels, values, sub_values):
                ax.text(label, value, str(sub_value)+"kWh", ha='center', va='bottom', color='#9aabcd')

            ax.set_xticklabels(labels, color='white')
            yticks=[]
            for i in ax.get_yticks():
                yticks.append(int(i))
            ax.set_yticklabels(yticks, color='white')
            basecanvas = tk.Canvas(frame, width=360, height=220, bg="#022e81",borderwidth=0, highlightthickness=0)
            basecanvas.place(relx=0.371,rely=0.753)
            # Create a Tkinter canvas that can display the bar chart
            canvas = FigureCanvasTkAgg(fig, master=basecanvas)
            canvas.draw()
            canvas.get_tk_widget().place(relx=0.53,rely=0.5,anchor="center")
            canvas.get_tk_widget().config(bg="#022e81")
            
            
        pwr_breakup_dropdown = ctk.CTkComboBox(frame,font=("Sofia Pro Regular", 18/1.22),dropdown_fg_color="#010061",dropdown_font=("Sofia Pro Regular", 25/1.22),width=115
                                            ,fg_color="#010061",button_color="#010061",border_color="#010061",bg_color="#022e81",corner_radius=8,
                                            values=["January","February","March","April","May","June","July","August","September","October","November","December"],
                                            command=combobox_callback2)
        pwr_breakup_dropdown.place(relx=0.557,rely=0.72)
        pwr_breakup_dropdown.set(calendar.month_name[datetime.datetime.now().month]) 
        
        labels1 = ["5", "10", "15", "20", "25", "30"]
        values1 = power_charge_monthly_breakdown[calendar.month_name[datetime.datetime.now().month]]
        sub_values1=power_unit_monthly_breakdown[calendar.month_name[datetime.datetime.now().month]]
        
        global fig3    
        fig3 = plt.figure(figsize=(5/1.22,2.5/1.22))
        fig3.patch.set_visible(False)

        # Create a subplot in the figure
        ax = fig3.add_subplot(111)

        # Plot the bar chart with specified color
        ax.bar(labels1, values1, color='#10a9ff',width=0.4)

        # Remove the box around the subplot
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(True)
        ax.spines['left'].set_visible(True)

        # Set the background color of the subplot
        ax.set_facecolor('#022e81')
        
        for label, value, sub_value in zip(labels1, values1, sub_values1):
             ax.text(label, value, str(sub_value)+"kWh", ha='center', va='bottom', color='#9aabcd')

        ax.set_xticklabels(labels1, color='white')
        yticks=[]
        for i in ax.get_yticks():
            yticks.append(int(i))
        ax.set_yticklabels(yticks, color='white')
        basecanvas2 = tk.Canvas(frame, width=475/1.22, height=260/1.22, bg="#022e81",borderwidth=0, highlightthickness=0)
        basecanvas2.place(relx=0.68,rely=0.76)
        # Create a Tkinter canvas that can display the bar chart
        global canvas1
        canvas1 = FigureCanvasTkAgg(fig3, master=basecanvas2)
        canvas1.draw()
        canvas1.get_tk_widget().place(relx=0.54,rely=0.5,anchor="center")
        canvas1.get_tk_widget().config(bg="#022e81") 
        plt.close("all")
        gc.collect()
        def double_click_to_on(event):
            frame.destroy()
            app.unbind('<Double-Button-1>')
            on_dashboard()
        frame.after(60000,off_dashboard_field_area)
        app.bind('<Double-Button-1>', double_click_to_on)   
        
    off_dashboard_field_area()  
    
def on_dashboard():
    frame = tk.Frame(app, bg="#030068")
    frame.pack(fill=tk.BOTH, expand=True)
    
    my_image = ctk.CTkImage(light_image=Image.open(".\\A3\\image_3.png"),size=(1280,1024))
    image_label = ctk.CTkLabel(frame, image=my_image, text="")  
    image_label.pack(fill=tk.BOTH, expand=True)
    
    def double_click_to_off(event):
        frame.destroy()
        app.unbind('<Double-Button-1>')
        off_dashboard_field_area()  
    app.bind('<Double-Button-1>', double_click_to_off)
    
    icon_position={0:[0.082,0.1982],1:[0.228,0.1982],2:[0.374,0.1982],3:[0.082,0.416],4:[0.228,0.416],5:[0.374,0.416],6:[0.082,0.633],7:[0.228,0.633],8:[0.374,0.633],9:[0.082,1.046]}
    text_position = {0: [0.082, 0.255], 1: [0.228, 0.255], 2: [0.374, 0.255], 3: [0.082, 0.4738], 4: [0.228, 0.4738], 5: [0.374, 0.4738], 6: [0.082, 0.6916], 7: [0.228, 0.6916], 8: [0.374, 0.6916], 9: [0.082, 1.1044]}
    
    def device_management():
        global device_display
        def device_display():
            f=open("Device List.txt","r+")
            global devices
            devices=[]
            
            read=f.readlines()
            for i in read: 
                j=i.split("4$4")
                devices.append(j)
            for m in devices:
                if m[0]=="\n":
                    devices.remove(m)
            global r
            if len(devices)!=0:
                for r in range(len(devices)):    
                    if devices[r][1]=="Lightbulb" and devices[r][2]=="Non-smart device\n":
                        bulb(frame,icon_position[int(r)],text_position[int(r)],devices[r][0])
            f.close()
        
        device_display()

        def add_device_function(): 
            global tempframe
            tempframe= tk.Frame(app, bg="#030068")
            tempframe.place(relx=0,rely=0)
            
            my_image1 = ctk.CTkImage(light_image=Image.open(".\\A3\\image_4.png"),size=(1280,1024))
            image_label1 = ctk.CTkLabel(tempframe, image=my_image1, text="")  
            image_label1.pack(fill=tk.BOTH, expand=True)
            global device_name_entry
            device_name_entry=ctk.CTkEntry(tempframe,width=460, height=50,text_color="#ffffff",font=("Sofia Pro Regular",21),
                                    fg_color="#2b2990",placeholder_text="Device name",placeholder_text_color="#9f9fd1",
                                    border_color="#2b2990",corner_radius=10,bg_color="#1b1976")
            device_name_entry.place(relx=0.507,rely=0.35,anchor="center")
            global device_dropdown
            device_dropdown = ctk.CTkComboBox(tempframe,font=("Sofia Pro Regular", 21),width=460,height=50,dropdown_fg_color="#1b1a5d",dropdown_font=("Sofia Pro Regular", 21)
                                                ,fg_color="#2b2990",button_color="#2b2990",border_color="#2b2990",bg_color="#022e81",corner_radius=10,dropdown_text_color="#ffffff",
                                                values=["Lightbulb","Fan","Geyser","Water Pump","Dishwasher","Refrigerator","Iron","Water Filter","Chimney","Induction Stove"])
            device_dropdown.place(relx=0.3265,rely=0.425)
            device_dropdown.set("Device")
            global device_type  
            device_type = ctk.CTkComboBox(tempframe,font=("Sofia Pro Regular", 21),width=460,height=50,dropdown_fg_color="#1b1a5d",dropdown_font=("Sofia Pro Regular", 21)
                                                ,fg_color="#2b2990",dropdown_text_color="#ffffff",button_color="#2b2990",border_color="#2b2990",bg_color="#022e81",corner_radius=10,
                                                values=["Smart Device","Non-smart device"])
            device_type.place(relx=0.3265,rely=0.525)
            device_type.set("Type of device")
            
            add_device_button=ctk.CTkButton(tempframe, text="Add Device Now", height=50, width=460, corner_radius=10, fg_color="#0fa5f9",bg_color="#01005f",font=("Sofia Pro Regular",22),text_color="white",command=device_saver)
            add_device_button.place(relx=0.507,rely=0.66,anchor="center")
            
            close_button=ctk.CTkButton(tempframe, text="X",width=25, corner_radius=5, fg_color="#1b1976",bg_color="#1b1976",font=("Arial",32),text_color="#ffe036",compound="top",command=lambda:tempframe.destroy())
            close_button.place(relx=0.675,rely=0.24,anchor="center")
            
        add_device_button=ctk.CTkButton(frame, text="+", height=33, width=35, corner_radius=5, fg_color="#0e9cec",hover_color="#0b7dbd",bg_color="#01005f",font=("Arial",26),text_color="white",compound="top",command=add_device_function)
        add_device_button.place(relx=0.2,rely=0.049,anchor="center")
        
        def device_saver():
            f=open("Device List.txt","a+")
            add=device_name_entry.get()+"4$4"+device_dropdown.get()+"4$4"+device_type.get()+"\n"
            f.write(add)
            f.close()
            device_display()
            tempframe.destroy()
    device_management()
    weather_query(city_name)
    def weather_display2():
        aqilabel=ctk.CTkLabel(frame, text=air_quality["aqi"], text_color="#ffffff", font=("Sofia Pro Regular", 40/1.22), fg_color="#022e81")
        aqilabel.place(relx=0.88, rely=0.21,anchor="ne")
        
        primary_pollutant=ctk.CTkLabel(frame, text=air_quality["pm10"], text_color="#ffffff", font=("Sofia Pro Regular", 35/1.22), fg_color="#022e81")
        primary_pollutant.place(relx=0.85, rely=0.355,anchor="ne")
        
        aqi_ranges = {(0, 50): ".\\A3\\50face.png",(50, 100): ".\\A3\\100face.png",(100, 200): ".\\A3\\200face.png",(200, 300): ".\\A3\\300face.png",(300, 400): ".\\A3\\400face.png",(400, float('inf')): ".\\A3\\500face.png"}
        aqi = int(air_quality["aqi"])
        face = None
        for range_, filename in aqi_ranges.items():
            if range_[0] <= aqi < range_[1]:
                face = filename
                break
        if face is not None:
            face_icon = ctk.CTkImage(light_image=Image.open(face), size=(80/1.22, 160/1.22))
            face_place = ctk.CTkLabel(frame, image=face_icon, text="", bg_color="#022e81", corner_radius=35)  
            face_place.place(relx=0.95, rely=0.25, anchor="center")
            
        ctc = ctk.CTkLabel(frame, text=weather["current_temperature_celsius"]+"°C", font=("Sofia Pro Regular",50/1.22), text_color="#ffffff",fg_color="#022e81")
        ctc.place(relx=0.735, rely=0.17, anchor="center")
        
        humidity_label=ctk.CTkLabel(frame,text=weather["humidity"],text_color="#ffffff",font=("Sofia Pro Regular",50/1.22),bg_color="#022e81")
        humidity_label.place(relx=0.735,rely=0.336,anchor="center")
        weathericon=ctk.CTkImage(light_image=Image.open(".\\A3\\" + weather["status"]+".png"),
                                        size=(85/1.22,85/1.22))
        weather_icon = ctk.CTkLabel(frame, image=weathericon, text="",bg_color="#022e81",corner_radius=35)  
        weather_icon.place(relx=0.735, rely=0.253, anchor="center")
            
        room_name1= ctk.CTkLabel(frame, text=details[0],bg_color="#020268",text_color="#ffffff",font=("Sofia Pro Regular",30/1.22),corner_radius=35,justify="left")  
        room_name1.place(relx=0.065, rely=0.045, anchor="w" )
    weather_display2()
    electricity_info()

    voltage_label=ctk.CTkLabel(frame, text=voltage+"V", font=("Sofia Pro Regular", 21/1.22),text_color="#ffffff", bg_color="#022372", corner_radius=35,justify="center")
    voltage_label.place(relx=0.395, rely=0.0375, anchor="center")
    
    current_label=ctk.CTkLabel(frame, text=current+"A", font=("Sofia Pro Regular", 21/1.22),text_color="#ffffff", bg_color="#022372", corner_radius=35,justify="center")
    current_label.place(relx=0.467, rely=0.0375, anchor="center")

    labels = ["5", "10", "15", "20", "25", "30"]
    values = power_charge_monthly_breakdown[calendar.month_name[datetime.datetime.now().month]]
    sub_values=power_unit_monthly_breakdown[calendar.month_name[datetime.datetime.now().month]]
    global fig1    
    fig1 = plt.figure(figsize=(3.79999,2.1))
    fig1.patch.set_visible(False)

    # Create a subplot in the figure
    ax1 = fig1.add_subplot(111)
    # Plot the bar chart with specified color
    ax1.bar(labels, values, color='#10a9ff',width=0.4)

    # Remove the box around the subplot
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_visible(True)
    ax1.spines['left'].set_visible(True)


    # Set the background color of the subplot
    ax1.set_facecolor('#022e81')
    
    for label, value, sub_value in zip(labels, values, sub_values):
        ax1.text(label, value, str(sub_value)+"kWh", ha='center', va='bottom', color='#9aabcd')

    ax1.set_xticklabels(labels, color='white')
    yticks=[]
    for i in ax1.get_yticks():
        yticks.append(int(i))
    ax1.set_yticklabels(yticks, color='white')
    global basecanvas
    basecanvas = tk.Canvas(frame, width=360, height=220, bg="#022e81",borderwidth=1, highlightthickness=0)
    basecanvas.place(relx=0.7,rely=0.76)

    global canvas
    canvas = FigureCanvasTkAgg(fig1, master=basecanvas)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.53,rely=0.5,anchor="center")
    canvas.get_tk_widget().config(bg="#022e81") 
    
    def combobox_callback2(choice):
        global values, sub_values
        values = power_charge_monthly_breakdown[choice]
        sub_values=power_unit_monthly_breakdown[choice]
        global fig
        fig = plt.figure(figsize=(3.79999,2.1))
        fig.patch.set_visible(False)

        ax = fig.add_subplot(111)
        ax.bar(labels, values, color='#10a9ff',width=0.4)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(True)
        ax.spines['left'].set_visible(True)
        ax.set_facecolor('#022e81')
        
        for label, value, sub_value in zip(labels, values, sub_values):
            ax.text(label, value, str(sub_value)+"kWh", ha='center', va='bottom', color='#9aabcd')

        ax.set_xticklabels(labels, color='white')
        yticks=[]
        for i in ax.get_yticks():
            yticks.append(int(i))
        ax.set_yticklabels(yticks, color='white')
        basecanvas = tk.Canvas(frame, width=360, height=220, bg="#022e81",borderwidth=0, highlightthickness=0)
        basecanvas.place(relx=0.7,rely=0.76)
        # Create a Tkinter canvas that can display the bar chart
        canvas = FigureCanvasTkAgg(fig, master=basecanvas)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.53,rely=0.5,anchor="center")
        canvas.get_tk_widget().config(bg="#022e81")
        
        
    pwr_breakup_dropdown = ctk.CTkComboBox(frame,font=("Sofia Pro Regular", 18/1.22),text_color="#ffffff",dropdown_text_color="#ffffff", dropdown_fg_color="#010061",dropdown_font=("Sofia Pro Regular", 25/1.22),width=115
                                        ,fg_color="#010061",button_color="#010061",border_color="#010061",bg_color="#022e81",corner_radius=8,
                                        values=["January","February","March","April","May","June","July","August","September","October","November","December"],
                                        command=combobox_callback2)
    pwr_breakup_dropdown.place(relx=0.895,rely=0.72)
    pwr_breakup_dropdown.set(calendar.month_name[datetime.datetime.now().month]) 

    pwr_consump_text=ctk.CTkLabel(frame, text=power_consumption_monthly[calendar.month_name[datetime.datetime.now().month]],text_color="#ffffff", font=("Sofia Pro Regular", 38/1.22), bg_color="#2355b4", corner_radius=35)
    pwr_consump_text.place(relx=0.788, rely=0.56, anchor="center")
        
    pwr_consump_sav_text1=ctk.CTkLabel(frame, text="Savings\n"+power_consumption_savings_monthly[calendar.month_name[datetime.datetime.now().month]]+" units",text_color="#ffffff", font=("Sofia Pro Regular", 35/1.22), bg_color="#022e81", corner_radius=35)
    pwr_consump_sav_text1.place(relx=0.92, rely=0.56, anchor="center")
    
    def combobox_callback(choice):
        pwr_consump_text.configure(text=power_consumption_monthly[choice])
        pwr_consump_sav_text1.configure(text="Savings\n"+power_consumption_savings_monthly[choice]+" units")
    pwr_consump_dropdown = ctk.CTkComboBox(frame,font=("Sofia Pro Regular", 18/1.22),dropdown_fg_color="#010061",dropdown_font=("Sofia Pro Regular", 25/1.22),width=115
                                        ,fg_color="#010061",button_color="#010061",border_color="#010061",bg_color="#022e81",corner_radius=8,
                                        values=["January","February","March","April","May","June","July","August","September","October","November","December"],
                                        command=combobox_callback)
    pwr_consump_dropdown.place(relx=0.891,rely=0.435)
    pwr_consump_dropdown.set(calendar.month_name[datetime.datetime.now().month]) 
    
    def update_time_date():
        current_time_date = datetime.datetime.now().strftime("%b %d, %Y | %I:%M %p")  # Format time as "MMM DD, YYYY - HH:MM pm"
        date_time.configure(text=current_time_date)
        frame.after(1000, update_time_date)
    date_time = ctk.CTkLabel(frame, text="", text_color="#ffffff", font=("Sofia Pro Regular", 26/1.22), fg_color="#022372")
    date_time.place(relx=0.675, rely=0.032)
    update_time_date()
    plt.close("all")
    frame.after(60000,on_dashboard)

def bulb(frame,labellist,textlist,name):
    bulb_image=ctk.CTkImage(light_image=Image.open(".\\A3\\Bulb.png"),size=(170,201))
    bulb_label = ctk.CTkLabel(frame, image=bulb_image, text="" )  
    bulb_label.place(relx=labellist[0],rely=labellist[1],anchor="center")
    bulb_text=ctk.CTkLabel(frame, text=name, font=("Sofia Pro Regular", 22),text_color="#6c6fc0", bg_color="#022372")
    bulb_text.place(relx=textlist[0], rely=textlist[1],anchor="center")
    global bulb_state
    bulb_state = False

    def bulb_logic(event):
        global bulb_state
        if bulb_state==True:
            bulb_image.configure(light_image=Image.open(".\\A3\\Bulb.png"))
            bulb_text.configure(text_color="#6c6fc0")
            bulb_state = False
        else:
            bulb_image.configure(light_image=Image.open(".\\A3\\Bulb_enabled.png"))
            bulb_text.configure(text_color="#48d3ee")
            bulb_state = True
    def detailed_page(event):
        frame.destroy()
        frame1 = tk.Frame(app, bg="#030068")
        frame1.pack(fill=tk.BOTH, expand=True)
        my_image = ctk.CTkImage(light_image=Image.open(".\\A3\\image_5.png"),size=(1280,1024))
        image_label = ctk.CTkLabel(frame1, image=my_image, text="")  
        image_label.pack(fill=tk.BOTH, expand=True)
    bulb_label.bind('<Button>', bulb_logic)
    bulb_label.bind("<Double-Button-1>",detailed_page)

def electricity_info():
    #write the code to retrieve all information related to electricity
    
    global power_consumption_monthly
    power_consumption_monthly = {
    "January": "245",
    "February": "514",
    "March": "285",
    "April": "320",
    "May": "410",
    "June": "380",
    "July": "1290",
    "August": "345",
    "September": "375",
    "October": "430",
    "November": "490",
    "December": "1510"}
    
    global power_consumption_savings_monthly
    power_consumption_savings_monthly = {
    "January": "25",
    "February": "54",
    "March": "25",
    "April": "30",
    "May": "40",
    "June": "30",
    "July": "20",
    "August": "35",
    "September": "35",
    "October": "40",
    "November": "40",
    "December": "50"}
    global power_charge_monthly_breakdown
    power_charge_monthly_breakdown = {
    "January": [300, 415, 522, 255, 416, 545],
    "February": [310, 428, 532, 262, 428, 560],
    "March": [320, 442, 543, 269, 441, 575],
    "April": [330, 456, 554, 276, 454, 590],
    "May": [340, 470, 565, 283, 467, 605],
    "June": [350, 484, 576, 290, 480, 620],
    "July": [360, 498, 587, 297, 493, 1635],
    "August": [370, 512, 598, 304, 506, 650],
    "September": [380, 526, 609, 311, 519, 665],
    "October": [390, 540, 620, 318, 532, 680],
    "November": [400, 554, 631, 325, 545, 695],
    "December": [410, 568, 642, 332, 558, 858]}


    global power_unit_monthly_breakdown
    power_unit_monthly_breakdown = {
    "January": [25, 65, 51, 16, 41, 45],
    "February": [30, 60, 49, 18, 42, 48],
    "March": [28, 63, 52, 19, 44, 46],
    "April": [27, 61, 53, 17, 40, 47],
    "May": [29, 64, 50, 15, 43, 44],
    "June": [26, 66, 54, 16, 41, 45],
    "July": [24, 67, 55, 14, 42, 46],
    "August": [23, 68, 56, 13, 43, 47],
    "September": [22, 69, 57, 12, 44, 48],
    "October": [21, 70, 58, 11, 45, 49],
    "November": [20, 71, 59, 10, 46, 50],
    "December": [19, 72, 60, 9, 47, 51]
    }
    
    global voltage
    voltage="223.2"
    global current
    current="4.6"  
    
def sun_position_figure(frame,sunrise,sunset):         

    sunrise_text=ctk.CTkLabel(frame, text=sunrise, font=("Sofia Pro Regular", 48/1.22), bg_color="#022e81", corner_radius=35)
    sunrise_text.place(relx=0.096, rely=0.92, anchor="center")

    sunset_text=ctk.CTkLabel(frame, text=sunset, font=("Sofia Pro Regular", 48/1.22), bg_color="#022e81", corner_radius=35)
    sunset_text.place(relx=0.265, rely=0.92, anchor="center")
       
def weather_query(city_name):
    # write the code to  retrieve the city weather information and assign the values to these variables
     
    current_temperature_celsius="34"
    current_temperature_fahrenheit="77"
    precipitation="78%"
    humidity="85%"
    wind="15"+"km/h"
    hpa="1074"+"hPa"
    uv="8"
    visibility="10"+"km"
    feels_like="25"
    status="sunny"
    status_label="Sunny"
    today=date.today()
    currentday=today.strftime("%A")
    next_five_days = []
    for i in range(5):
        next_day = today + timedelta(days=i+1)
        next_five_days.append(next_day.strftime("%A")[:3])
    aqi="150"
    pm25="52"
    pm10="51"
    co="2"
    ozone="14"
    so2="52"
    no2="52"
    global forecast
    forecast={'day1': {"day":next_five_days[0],'status': 'cloudy', 'min': '28', 'max': '34'},
              'day2': {"day":next_five_days[1],'status': 'sunny', 'min': '25', 'max': '33'},
              'day3': {"day":next_five_days[2],'status': 'thunderstorm', 'min': '21', 'max': '29'},
              'day4': {"day":next_five_days[3],'status': 'rainy', 'min': '24', 'max': '34'},
              'day5': {"day":next_five_days[4],'status': 'sunny', 'min': '21', 'max': '28'}}
    global weather
    weather={"feels_like":feels_like,
    "status_label":status_label,
    "current_temperature_celsius": current_temperature_celsius,
    "current_temperature_fahrenheit": current_temperature_fahrenheit,
    "precipitation": precipitation,
    "humidity": humidity,
    "wind": wind,
    "hpa": hpa,
    "uv":uv,
    "visibility": visibility,
    "feels_like": feels_like,
    "status": status}

    global air_quality
    air_quality={
    "aqi": aqi,
    "pm25": pm25,
    "pm10": pm10,
    "co":co,
    "ozone": ozone,
    "so2": so2,
    "no2": no2}
    global last_update
    last_update="23 March 2023: 09:12PM"
if os.path.exists("Validator.txt") is True:
    threading.Thread(target=off_dashboard).start()
    
else:
    threading.Thread(target=welcomepage).start()

app.mainloop()

