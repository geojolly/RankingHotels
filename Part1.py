import pandas as pd
from scipy import stats

# Read the dataset using Pandas library
data = pd.read_excel("Data/data_italy.xlsx")
temp = pd.DataFrame(columns=['Hotel','Rating','Rank'])
ratings_normal_1 = pd.DataFrame(columns=['Rating'])
ratings_normal_2 = pd.DataFrame(columns=['Rating'])

def normalizedpeformancematrix1(w1,w2,w3,w4):

    max_col = data['Total of positive words'].max()
    min_col = data['Total of positive words'].min()
    for index, row in data.iterrows():
        numerator = data['Total of positive words'] - min_col
        val = w2 * (numerator / (max_col - min_col))
        data.iloc[[index],[2]]=val

    max_col = data['Average given by Reviewers'].max()
    min_col = data['Average given by Reviewers'].min()
    for index, row in data.iterrows():
      val = data['Average given by Reviewers'] - min_col
      val = w3 * (val / (max_col - min_col))
      data.iloc[[index],[3]] = val

    max_col = data['Total of Reviews'].max()
    min_col = data['Total of Reviews'].min()
    for index, row in data.iterrows():
        val = data['Total of Reviews'] - min_col
        val = w4 * (val / (max_col - min_col))
        data.iloc[[index],[4]] = val

    max_col = data['Total of negative words'].max()
    min_col = data['Total of negative words'].min()
    for index, row in data.iterrows():
        val = data['Total of negative words'] - max_col
        val = w1 * (val / (min_col - max_col))
        data.iloc[[index], [1]] = val
    w_sum=0

    #Computing the wieghted sum
    w_sum = data['Total of positive words'] + data['Average given by Reviewers'] + data['Total of Reviews'] + data['Total of negative words']
    temp['Hotel'] = data['Name']
    temp['Rating'] =  w_sum

    #Preapring the rankings

    result = temp.sort_values(['Rating'])
    result['Rank']= temp.index
    temp['Rank'] = result['Rank']

    #Writing to csv file
    result.to_csv("Data/normalizedperformancematrix1.csv")

def normalizedpeformancematrix2(w1,w2,w3,w4):

    max_col = data['Total of positive words'].max()
    for index, row in data.iterrows():
        val = w2 * (data['Total of positive words'] / max_col)
        data.iloc[[index],[2]]=val

    max_col = data['Average given by Reviewers'].max()
    for index, row in data.iterrows():
      val = w3 * (data['Average given by Reviewers'] / max_col)
      data.iloc[[index],[3]] = val

    max_col = data['Total of Reviews'].max()
    for index, row in data.iterrows():
        val = w4 * (data['Total of Reviews'] / max_col)
        data.iloc[[index],[4]] = val

    max_col = data['Total of negative words'].max()
    for index, row in data.iterrows():
        val = data['Total of negative words'] / max_col
        val = w1 * (1 - val)
        data.iloc[[index], [1]] = val
    w_sum=0

    #Computing the wieghted sum
    w_sum = data['Total of positive words'] + data['Average given by Reviewers'] + data['Total of Reviews'] + data['Total of negative words']
    temp['Hotel'] = data['Name']
    temp['Rating'] =  w_sum

    #Preapring the rankings
    result = temp.sort_values(['Rating'])
    result['Rank']= temp.index
    temp['Rank'] = result['Rank']

    #Writing to csv file
    result.to_csv("Data/normalizedperformancematrix2.csv")


def kendall():
    ratings = pd.DataFrame(columns=['Hotel', 'Booking', 'Rank'])
    ratings['Hotel'] = data['Name']
    ratings['Booking'] = data['Bookings score']
    ratings = ratings.sort_values('Booking')
    ratings['Rank'] = temp.index
    result = ratings.sort_values(['Hotel'])
    tau, p_value = stats.kendalltau(temp['Rank'], ratings['Rank'])
    print ("tau value :", tau, "p value :", p_value)

if __name__ == '__main__':

    #For each wieghts
    print("\nFor wieghts w1=0.25,w2=0.25,w3=0.25,w4=0.25")

    print("\n Normalized Performance Matrix 1 ")
    normalizedpeformancematrix1(0.25,0.25,0.25,0.25)
    kendall()

    print("\n Normalized Performance Matrix 2 ")
    normalizedpeformancematrix2(0.25, 0.25, 0.25, 0.25)
    kendall()

    print("\nFor wieghts w1=0.4,w2=0.2,w3=0.2,w4=0.2")

    print("\n Normalized Performance Matrix 1 ")
    normalizedpeformancematrix1(0.25, 0.25, 0.25, 0.25)
    kendall()

    print("\n Normalized Performance Matrix 2 ")
    normalizedpeformancematrix2(0.25, 0.25, 0.25, 0.25)
    kendall()

    print("\nFor wieghts w1=0.1,w2=0.3,w3=0.4,w4=0.3")

    print("\n Normalized Performance Matrix 1 ")
    normalizedpeformancematrix1(0.25, 0.25, 0.25, 0.25)
    kendall()

    print("\n Normalized Performance Matrix 2 ")
    normalizedpeformancematrix2(0.25, 0.25, 0.25, 0.25)
    kendall()



