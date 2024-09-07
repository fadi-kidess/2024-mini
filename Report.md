Exercise 1: For this exercise, we read the print value of `adc.read_u16()` while covering and shining a light on the sensor to estimate the max and min brightness. After we input the estimate max/min_bright, then we used 1 to subtract from the `duty_cycle` and print the value. Hence, when it's at max brightness, it reads as 1 and when it's min brightness, it reads as 0.
1. max_bright = 45000, min_bright = 5500

Exercise 2: In this exercise, we input a series of frequencies and durations that match the tones of twinkle twinkle little star using the note frequency chart provided.

Exercise 3: In exercise 3, we decided to upload our data to thingspeak. We first connected the button to the according pins then changes the pin number to 12 in our code. We connected to wifi and added the code to upload to cloud according to thingspeak's tutorial. Finally, after executing the code, maximum, minimum, average, and score is uploaded to thingspeak cloud. 
