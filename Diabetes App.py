import pandas as pd
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from pandas import set_option,DataFrame

filename = r'Diabetes Death Dataset.csv'
names = ['age','anaemia','creatinine_phosphokinase','gender','ejection_fraction','high_blood_pressure','platelets','serum_creatinine','serum_sodium','smoking','smokesperday','diabetes']
dataframe = read_csv(filename, names=names, delimiter=';')
array = dataframe.values
X = array[:,0:11]
Y = array[:,11]
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size,random_state=seed)
model = LogisticRegression()
model.fit(X_train, Y_train)
result = model.score(X_test, Y_test)

def user_report(age,anaemia,creatinine_phosphokinase,gender,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,serum_sodium,smoking,smokesperday):
     age_data = float(age)
     anaemia_data = float(anaemia)
     creatinine_phosphokinase_data = float(creatinine_phosphokinase)
     gender_data = float(gender)
     ejection_fraction_data = float(ejection_fraction)
     high_blood_pressure_data = float(high_blood_pressure)
     platelets_data = float(platelets)
     serum_creatinine_data = float(serum_creatinine)
     serum_sodium_data = float(serum_sodium)
     smoking_data = float(smoking)
     smokesperday_data = float(smokesperday)
  
     user_report_data = {
        'age_data':age_data,
        'anaemia_data':anaemia_data,
        'creatinine_phosphokinase_data':creatinine_phosphokinase_data,
    	'gender_data':gender_data,
    	'ejection_fraction_data':ejection_fraction_data,
    	'high_blood_pressure_data':high_blood_pressure_data,
    	'platelets_data':platelets_data,
    	'serum_creatinine_data':serum_creatinine_data,
        'serum_sodium_data':serum_sodium_data,
        'smoking_data':smoking_data,
        'smokesperday_data':smokesperday_data
	 }
     report_data = pd.DataFrame(user_report_data, index=[0])
     return report_data

class Main(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Main(name='main'))


class MainApp(MDApp):
    def build(self):
        self.help_string = Builder.load_file('main.kv')
        return self.help_string

    def predict(self):
        input_1 = self.help_string.get_screen('main').ids.input_1.text
        input_2 = self.help_string.get_screen('main').ids.input_2.text
        input_3 = self.help_string.get_screen('main').ids.input_3.text
        input_4 = self.help_string.get_screen('main').ids.input_4.text
        input_5 = self.help_string.get_screen('main').ids.input_5.text
        input_6 = self.help_string.get_screen('main').ids.input_6.text
        input_7 = self.help_string.get_screen('main').ids.input_7.text
        input_8 = self.help_string.get_screen('main').ids.input_8.text
        input_9 = self.help_string.get_screen('main').ids.input_9.text
        input_10 = self.help_string.get_screen('main').ids.input_10.text
        input_11 = self.help_string.get_screen('main').ids.input_11.text
        
        user_result_input = user_report(input_1,input_2,input_3,input_4,input_5,input_6,input_7,input_8,input_9,input_10,input_11)
        
        user_result_model = model.predict(user_result_input)
        print(result)
        
        output=''
        self.help_string.get_screen('main').ids.output_text_not.text = ''
        self.help_string.get_screen('main').ids.output_text_sick.text = ''
        
        if user_result_model[0]==0:
            output = 'You are not Diabetic'
            self.help_string.get_screen('main').ids.output_text_not.text = output
            
        else:
            output = 'You are Diabetic'
            self.help_string.get_screen('main').ids.output_text_sick.text = output
 
MainApp().run()