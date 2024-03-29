print(getwd())
setwd("/Users/mes8/Desktop/Abhijith/23")
library(e1071)
symptoms = read.csv("symptoms.csv")
symptoms_train = symptoms[,1:4] 
symptoms_test = data.frame(Chills="Y",RunningNose="N", Headache="mild",Fever="Y")
classifier_cl <- naiveBayes(symptoms_train,symptoms$HasFlu)
classifier_cl
symptoms_test_pred <- predict(classifier_cl, symptoms_test) 
cat("Prediction of Flu:\n") 
symptoms_test_pred
