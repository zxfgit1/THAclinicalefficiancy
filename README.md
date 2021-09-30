# THAclinicalefficiancy
This is the selection model of _"A prediction model for prognosis of femoral neck fractures patients 6 months after total hip arthroplasty based on preoperative clinical characteristics and computed tomography characteristics"_ that is contribute with preoperative clinical characteristics and CT characteristics.
To use this model you need python 3 installs and prepare a 2D CT.
1. All packages you need is in the requirements
2. To use this model simply download everything to the same folder and run the main program
3. Note that only one CT example is provided. 
4. If you want to run your own data simple change the data and put the corresponding CT to the designated path
5. Variables in the test data:
    1. Age: patients/your age 
    2. Left right: which side need THA surgery(left or right femur neck fracture,) 1 indicate right and 0 indicate left
    3. Gender: your gender, 0 indicate male and 1 indicate female
    4. Location: sugery location (posterior upper part, posterior lateral part or anterior lateral part) 0 indicate anterior lateral part, 1 indicate posterior upper part and posterior lateral part
    5. HCT, PCT, PT, INR, APT, FIB, AT are the clinical characteristics 
    6. BMI is patients/your BMI
    7. CT1, CT2, CT3, are three CT characteristics that we used which can be contained in the main program.
6. Files: 
    1. What_you_need: the folder that contains example CT
    2. Getctfeatures: the function that can provide you CT1, CT2, CT3,
    3. Main_program.ipny: the main program that you need to run(The only file you need to run)
    4. Model_test_file.csv : example file that will provide you your harris score category after 6 month of THA
    5. Preoperative_model.pkl : the pretrained model
    6. Requirements.txt : all packages that you need and the version that we used
