import pandas as pd

# Read the dataset using Pandas library
data = pd.read_excel("Data/data_italy.xlsx")
temp = pd.DataFrame(columns=['Hotel','Category'])

#Copy the names of the hotels to the temp dataframe for storing the results
temp['Hotel'] = data [ 'Name']

#Values defined
THRESHOLD = 0.6
W1 = 0.4
W2 = 0.2
W3 = 0.2
W4 = 0.2

def PessimisticmajoritySorting():
   #Limiting profile between Good and Very Good
    for index, row in data.iterrows():
      w = 0
      if data.iat[index,1] < 1000:
            w = w + W1
      if  data.iat[index,2] > 2500:
             w = w + W2
      if  data.iat[index,3] > 8:
             w = w + W3
      if  data.iat[index,4]  > 300:
             w = w + W4
      if w > THRESHOLD:
        temp.iloc[[index], [1]] = 'Very Good' #If the threshold is met then the Category is set to VeryGood
        w = 0
        if data.iat[index,1] < 500:
            w = w + W1
        if  data.iat[index,2] > 5000:
             w = w + W2
        if  data.iat[index,3] > 9:
             w = w + W3
        if  data.iat[index,4] > 500:
             w = w + W4
        if w > THRESHOLD:
            temp.iloc[[index], [1]] = 'Excellent' #If the threshold is met then Move to Supreme Category Excellent
        else :
            temp.iloc[[index], [1]] = 'Very Good' #Otherwise retain it to Very Good category
      else :
        temp.iloc[[index], [1]] = 'Good' #If none of the threshold is met then hotel is set to Good Category
    # Writing to csv file
    temp.to_csv("Data/PessimisticmajoritySorting.csv")
    print temp

def OptimisticmajoritySorting():
   #Limiting profile between Excellent and Very Good
    for index, row in data.iterrows():
      w = 0
      globe = False                #This variable is used to check if its in higher category or not
      if data.iat[index, 1] < 500:
          w = w + W1
      if data.iat[index, 2] > 5000:
          w = w + W2
      if data.iat[index, 3] > 9:
          w = w + W3
      if data.iat[index, 4] > 500:
          w = w + W4
      if w > THRESHOLD:
        globe = True            #Threshold is met hence we set the variable as True and
        temp.iloc[[index], [1]] = 'Excellent' #The hotel is set to the category of Excellent
        w = 0
        if data.iat[index, 1] < 1000:
            w = w + W1
        if data.iat[index, 2] > 2500:
            w = w + W2
        if data.iat[index, 3] > 8:
            w = w + W3
        if data.iat[index, 4] > 300:
            w = w + W4
        if w > THRESHOLD and not globe:
            temp.iloc[[index], [1]] = 'Very Good' #The hotel is set to Very good if it is not Excellent
        if not globe:
            temp.iloc[[index], [1]] = 'Good' #Assign Good
    temp.to_csv("Data/ OptimisticmajoritySorting.csv")
    print temp


if __name__ == '__main__':
    PessimisticmajoritySorting()
    OptimisticmajoritySorting()

    #As seen both Optimisitc and pessimistic work similar and the results are similar as well.
    #Though computationally the pessimistic appraoch is cost effective over the optimistic one. 