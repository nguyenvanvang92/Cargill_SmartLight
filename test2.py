from firebase import firebase   

app = firebase.FirebaseApplication("https://datakivyapp.firebaseio.com/", None)

data = {
    "status": "",
    "sign_app": "",
    "time_run_per_day": "",
    "alarm": "",
    "old": "",
    "warmming_out_date": "",
}

for i in range(1,11,1):
    data1 = "led_" + str(i)
    app.patch("Phong Nhap Xa/" + data1, data)