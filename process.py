import pandas as pd
import parse
import time

parse.filter_data()
start = time.time()
df = pd.read_csv("./data/tops.csv")
print("==========================================================")
print("Here is the data:\n\n",df[:4])
print("[INFO} Data Shape: ",df.shape)
print("==========================================================")

columns = ['description','inStock', 'codAvailable', 'offers','deliveryTime', 'sizeUnit', 'storage', 'displaySize',
       'specificationList', 'sellerAverageRating',
       'sellerNoOfRatings', 'sellerNoOfReviews', 'idealFor']

df.drop(columns,axis=1,inplace=True)
print("[INFO} Some Columns removed (not required) | Data Shape:", df.shape)

#print(df.isnull().sum())

dropnaColumns= ['productId', 'imageUrlStr', 'mrp', 'sellingPrice',
       'specialPrice', 'productUrl', 'categories', 'productBrand',
       'productFamily', 'discount', 'shippingCharges', 'size', 'color',
       'keySpecsStr', 'detailedSpecsStr', 'sellerName', 'sleeve', 'neck']

df.dropna(axis=0,how='any',subset=dropnaColumns,inplace=True)
#df[df.neck.isnull()==True]
print("[INFO] Dropped missing values...")
#print("[INFO] New shape: ",df.shape)
df[df.title.isnull()==True] = 'None'
print("==========================================================")
print("[INFO] Missing values after processing:\n\t",df.isnull().sum())
print("==========================================================")

df.sort_values(by=['sellerName','productBrand','mrp'],inplace=True)
df.to_csv('./data/processedData.csv',sep=',',index=False)

end = time.time() - start
print("[INFO] New shape: ",df.shape)
print("[INFO] Processing done! Time Required {}".format(str(round(end,2))))