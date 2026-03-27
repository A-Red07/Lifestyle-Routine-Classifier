import pandas as pd
from sklearn.tree import DecisionTreeClassifier
routinrcords = {
    "sleep": [10,6,5,8,7,9,8,8,5,6,7,3,7,8,4,7,8],
    "water": [8,2,1,6,5,7,9,2,3,8,7,5,6,8,7,2,4],
    "exercise": [0,30,15,5,90,30,60,50,90,60,25,90,60,45,45,30,30],
    "screentme": [9,8,5,6,4,3,6,1,2,7,9,8,6,4,5,4,7],
    "studyhors": [3,4,7,5,6,8,1,2,4,3,6,5,2,9,9,3,4],
    "mealsper_day": [3,2,3,2,3,3,3,1,3,3,2,3,2,3,1,4,5],
    "wakeearly": [1,0,1,0,1,1,0,0,1,1,0,1,0,1,0,0,1],
    "routinelabel": [
        "Good", "Poor", "Good", "Poor", "Average",
        "Good", "Average", "Poor", "Good", "Average",
        "Poor", "Good", "Poor", "Good", "Poor","Average","Good"
    ]
}
routindf=pd.DataFrame(routinrcords)
routinfeatures=routindf.drop("routinelabel", axis=1)
routintarget=routindf["routinelabel"]
routinemodel=DecisionTreeClassifier(max_depth=4, random_state=42)
routinemodel.fit(routinfeatures, routintarget)
print("Daily Routine Analyzer")
print("Enter your routine details below.")
# Replaced input() calls with hardcoded values for demonstration
sleep = 7
water = 6
exercise = 30
screentme = 5
studyhors = 4
mealsper_day = 3
wakeearly = 1
if not (0 <=sleep<=12):
    print("Sleep hours should be between 0 and 12.")
if not (0 <=water<=15):
    print("Water glasses should be between 0 and 15.")
if not (0<=exercise<= 180):
    print("Exercise minutes should be between 0 and 180.")
if not (0<=screentme<= 18):
    print("Screen time should be between 0 and 18.")
if not (0<= studyhors<= 16):
    print("Study hours should be between 0 and 16.")
if not (1<=mealsper_day<= 5):
    print("Meals per day should be between 1 and 5.")
if wakeearly not in [0, 1]:
    print("Wake early must be 1 or 0.")
userow = pd.DataFrame([{
    "sleep": sleep,
    "water": water,
    "exercise": exercise,
    "screentme": screentme,
    "studyhors": studyhors,
    "mealsper_day": mealsper_day,
    "wakeearly": wakeearly
}])

prediction = routinemodel.predict(userow)[0]
print("Predicted Routine", prediction)
print("Suggestions")
if sleep< 7:
    print("Try to sleep at lest 7 hours")
if water< 6:
    print("Increse water intake")
if exercise< 15:
    print("Add some exercise to yor day")
if screentme> 6:
    print("Reduce scren time a little")
if mealsper_day< 3:
    print("Try to eat 3 propr meals")
if wakeearly== 0:
    print("Waking up erly may help keep your routine structured")
if prediction=="Good":
    print("Your routine looks balnced overall")
elif prediction == "Average":
    print("Your routine is okay, but there is rom for improvement")
else:
    print("Your routine needs improvment in a few areas")
