import csv
import time

#Function to parse data and extract records based on subcategory
def filter_data():

    with open('./data/original_data.csv','r',encoding='utf8') as f_in, open('./data/tops.csv','w',encoding='utf8') as f_out:

        data = csv.reader(f_in,delimiter=',')
        writer = csv.writer(f_out, delimiter=',')

        # Skipping info line
        #next(data)

        print("[INFO] loading data successful...")
        i=0
        countTops=0
        skippedCount=0
        start = time.time()
        for row in data:
            #For Info Line
            if(i==0):
                writer.writerow(row)
            elif(len(row)<32):
                #pass
                #Skipping line 110231: expected 32 fields, saw 43\nSkipping line
                print('[Skipped Row] ====> {}: expected 32 fields, saw {}'.format(i,len(row)))
                skippedCount+=1
            elif(len(row)>32):
                #for i in range(len(row)):
                 #   print(row[i]+"\n")
                print('[Skipped Row] ====> {}: expected 32 fields, saw {}'.format(i,len(row)))
                skippedCount+=1
            else:

                sub_category = row[8].split('>')[-1]
                #print(type(row),sub_category)
                #print("\n")

                if(len(sub_category)>0 and sub_category=='Tops'):
                    #print(type(row), sub_category)
                    writer.writerow(row)
                    countTops+=1

                #pass
            i+=1

        end = time.time() - start


    print("==========================================================")
    print("                           SUMMARY")
    print("==========================================================")
    print("[INFO] Skipped {} records with insufficient columns".format(skippedCount))
    print("[INFO] Total Records: {} | Extraction Time: {}s".format(str(countTops),str(round(end,2))))
    print("==========================================================\n")

#filter_data()
