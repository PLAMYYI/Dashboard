6810110203 ปาลินี เหล่าติวานนท์

Customer Churn ML Dashboard
    โปรเจคนี้เป็นเว็บ Dashboard สำหรับวิเคราะห์และทำนายว่า ลูกค้าจะยกเลิกบริการ (Churn) หรือไม่ ซึ่งสร้างด้วย Python โดยใช้ AutoGluon (ทำ Machine Learning) Streamlit (ทำเว็บ) และ Plotly (ทำกราฟ) โดยทำเพื่อวิเคราะห์ข้อมูลลูกค้า ดูแนวโน้มการยกเลิกบริการ ทำนายลูกค้าใหม่ว่าจะ churn หรือไม่ แล้วแสดงผลแบบ Dashboard บนเว็บ

Data structure
- ml-dashboard/
    - app.py                
    - train.py             
    - data.csv            
    - feature_importance.csv
    - models/             
    - README.md

Dashboard แสดง
- กราฟการกระจายของ Churn
- กราฟความสัมพันธ์ระหว่าง Age และ Monthly Charge
- Feature Importance จากโมเดล
- สามารถเลือก Contract Type เพื่อกรองข้อมูลได้
- สามารถกรอกข้อมูลลูกค้าใหม่และกด Predict ได้

วิธีรันโปรแกรม
1. ติดตั้ง Library
    pip install -r requirements.txt

หรือ

    pip install streamlit pandas plotly autogluon

2. เทรนโมเดล (ถ้ายังไม่มี)
    python train_model.py

3. รัน Dashboard
    streamlit run app.py
