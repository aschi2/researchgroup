#Intro to Regular Expressions
attach(CA_Fire_History)
FFIRES = CA_Fire_History %>% filter(FOREST_NUM != 0)
FFIRES = FFIRES %>% filter(CAUSE != 30, CAUSE!= 14, CAUSE != 13, 
                           CAUSE != 15, CAUSE != 17,CAUSE != 16,  )
write.csv(FFIRES, file = "FIRES.csv")
