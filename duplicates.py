import json
import time
from model import *
import pandas as pd
import numpy as np
from scipy import spatial

df = pd.read_csv("./data/processedData.csv")

start = time.time()
json_output = {}
def findDuplicates(df):
    k = {}
    for productId in df.productId.values:
        k[productId] = 0

    lCount = 0
    sCount = 0
    for data in df.values:
        lCount += 1
        productId = data[0]
        print("==============================")
        print("\t", lCount,".", productId)
        print("==============================")
        # print(productId)
        if k[productId] == 1:
            continue

        else:
            k[data[0]] = 1
            pId = data

            title = data[1]
            imageUrlStr = data[2]
            mrp = data[3]
            sellingPrice = data[4]
            specialPrice = data[5]
            productUrl = data[6]
            categories = data[7].split('>')
            categories = ' '.join(categories)

            productBrand = data[8]
            productFamily = data[9].split(',')
            discount = data[10]
            shippingCharges = data[11]
            size = data[12]
            color = data[13]
            keySpecsStr = data[14].split(';')
            detailedSpecsStr = data[15].split(';')
            sellerName = data[16]
            sleeve = data[17]
            neck = data[18]

            #### Processing ####

            if (len(keySpecsStr) > 1):
                fabric = keySpecsStr[1].split(':')
                if (fabric[0] == "Fabric"):
                    fabric = fabric[len(fabric) - 1]
                else:
                    fabric = "unknown"
            else:
                fabric = "unknown"

            if (len(keySpecsStr) > 2):

                pattern = keySpecsStr[2].split(':')
                if (pattern[0] == "Pattern"):
                    pattern = pattern[len(pattern) - 1]
                else:
                    pattern = "unknown"
            else:
                pattern = "unknown"

            if (len(detailedSpecsStr) > 2 and pattern == "unknown"):

                pattern = detailedSpecsStr[2]
                pattern = pattern.split(":")
                if (pattern[0] == "Pattern"):
                    pattern = pattern[len(pattern) - 1]
                else:
                    pattern = "unknown"

            if (len(keySpecsStr) > 3):

                specsType = keySpecsStr[3]
                specsType = specsType.split(":")
                if (specsType[0] == "Type"):
                    specsType = specsType[len(specsType) - 1]
                else:
                    specsType += "unknown"
            else:
                specsType += "unknown"

            if (len(detailedSpecsStr) > 3 and specsType == "unknown"):

                specsType = detailedSpecsStr[3]
                specsType = specsType.split(":")
                if (specsType[0] == "Type"):
                    specsType = specsType[len(specsType) - 1]
                else:
                    specsType = "unknown"

            """
            fabric = keySpecsStr[1].split(':')
            fabric = fabric[-1]
            pattern = keySpecsStr[2].split(':')
            pattern = pattern[-1]
            specsType = keySpecsStr[3].split(':')
            specsType = specsType[-1]
            """

            str1 = title + ' ' + str(mrp) + ' ' + str(sellingPrice) + ' ' + str(specialPrice) + ' ' + str(
                productUrl) + ' ' + str(categories) + ' ' \
                   + str(productBrand) + ' ' + str(discount) + ' ' + str(
                shippingCharges) + size + ' ' + color + ' ' + str(fabric) + ' ' \
                   + str(pattern) + ' ' + str(specsType) + ' ' + str(sleeve) + ' ' + str(neck)

            v1 = avg_feature_vector(str1, model=model, num_features=300, index2word_set=index2word_set)

            print('Total number of product members: ', len(productFamily), productId)
            # print(productFamily)
            # print("\n\n",str1)

            tempResult = []
            for p in productFamily:
                if (p in df.productId.values and p!=productId):
                    print("\nFound family member in record\n")
                    k[p] = 1
                    sCount += 1

                    product2 = df[df.productId.values == p]
                    title2 = ''.join(str(l) for l in product2['title'])  # product2['title'][e]

                    # imageUrlStr2 = product2['imageUrlStr'][0]
                    mrp2 = ''.join(str(l) for l in product2['mrp'])  # product2['mrp'][0]
                    sellingPrice2 = ''.join(str(l) for l in product2['sellingPrice'])  # product2['sellingPrice'][0]
                    specialPrice2 = ''.join(str(l) for l in product2['specialPrice'])  # product2['specialPrice'][0]
                    productUrl2 = ''.join(str(l) for l in product2['productUrl'])  # product2['productUrl'][0]
                    # print('\n',product2['categories'])
                    categories2 = ''.join(
                        str(e) for e in product2['categories'])  # product2['categories'][0].split('>')
                    categories2 = ' '.join(categories.split('>'))

                    productBrand2 = ''.join(str(e) for e in product2['productBrand'])  # product2['productBrand'][0]
                    # productFamily = product2['productFamily'].split(',')
                    discount2 = ''.join(str(e) for e in product2['discount'])  # product2['discount'][0]
                    shippingCharges2 = ''.join(
                        str(e) for e in product2['shippingCharges'])  # product2['shippingCharges'][0]
                    size2 = ''.join(str(e) for e in product2['size'])  # product2['size'][0]
                    color2 = ''.join(str(e) for e in product2['color'])  # product2['color'][0]
                    keySpecsStr2 = ''.join(
                        str(e) for e in product2['keySpecsStr'])  # product2['keySpecsStr'][0].split(';')
                    keySpecsStr2 = keySpecsStr2.split(';')  # [1].split(':')[-1]
                    detailedSpecsStr2 = ''.join(
                        str(e) for e in product2['keySpecsStr'])  # product2['detailedSpecsStr'][0].split(';')
                    detailedSpecsStr2 = detailedSpecsStr2.split(';')  # [1].split(':')[-1]
                    sellerName2 = ''.join(str(e) for e in product2['sellerName'])  # product2['sellerName'][0]
                    sleeve2 = ''.join(str(e) for e in product2['sleeve'])  # product2['sleeve'][0]
                    neck2 = ''.join(str(e) for e in product2['neck'])  # product2['neck'][0]

                    #### Processing ####

                    if (len(keySpecsStr2) > 1):
                        fabric2 = keySpecsStr2[1].split(':')
                        if (fabric2[0] == "Fabric"):
                            fabric2 = fabric2[len(fabric2) - 1]
                        else:
                            fabric2 = "unknown"
                    else:
                        fabric2 = "unknown"

                    if (len(keySpecsStr2) > 2):

                        pattern2 = keySpecsStr2[2].split(':')
                        if (pattern2[0] == "Pattern"):
                            pattern2 = pattern2[len(pattern2) - 1]
                        else:
                            pattern2 = "unknown"
                    else:
                        pattern2 = "unknown"

                    if (len(detailedSpecsStr2) > 2 and pattern2 == "unknown"):

                        pattern2 = detailedSpecsStr2[2]
                        pattern2 = pattern2.split(":")
                        if (pattern2[0] == "Pattern"):
                            pattern2 = pattern2[len(pattern2) - 1]
                        else:
                            pattern2 = "unknown"

                    if (len(keySpecsStr2) > 3):

                        specsType2 = keySpecsStr2[3]
                        specsType2 = specsType2.split(":")
                        if (specsType2[0] == "Type"):
                            specsType2 = specsType2[len(specsType2) - 1]
                        else:
                            specsType2 += "unknown"
                    else:
                        specsType2 += "unknown"

                    if (len(detailedSpecsStr2) > 3 and specsType2 == "unknown"):

                        specsType2 = detailedSpecsStr2[3]
                        specsType2 = specsType2.split(":")
                        if (specsType2[0] == "Type"):
                            specsType2 = specsType2[len(specsType2) - 1]
                        else:
                            specsType2 = "unknown"

                    """
                    fabric2 = keySpecsStr2[1].split(':')
                    fabric2 = fabric2[-1]
                    pattern2 = keySpecsStr2[2].split(':')
                    pattern2 = pattern2[-1]
                    specsType2 = keySpecsStr2[3].split(':')
                    specsType2 = specsType2[-1]
                    """

                    str2 = title2 + ' ' + str(mrp2) + ' ' + str(sellingPrice2) + ' ' + str(
                        specialPrice2) + ' ' + productUrl2 + ' ' + str(categories2) + ' ' \
                           + str(productBrand2) + ' ' + str(discount2) + ' ' + str(shippingCharges2) + str(
                        size2) + ' ' + color2 + ' ' + str(fabric2) + ' ' \
                           + str(pattern2) + ' ' + str(specsType2) + ' ' + str(sleeve2) + ' ' + str(neck2)

                    # print("\n\n",str(str2))

                    v2 = avg_feature_vector(str2, model=model, num_features=300, index2word_set=index2word_set)

                    print("\n" + str(productId) + " p1-string-" + str1 + "\n" + str(p) + "p2-string-" + str2)

                    # calculate similarity
                    similarity = 1 - spatial.distance.cosine(v1, v2)
                    similarity = similarity * 1000 / 1000
                    similarity = "%.6f" % similarity

                    print("====================================\n")
                    print("\t\t" + str(similarity) + "")
                    print("\n===================================\n\n\n")

                    if (float(similarity) > 0.5):
                        result = []
                        result.append(p)
                        result.append(str(similarity))
                        tempResult.append(result)
                else:
                    print("Product ID Not Found! Wait for next product..")

            if (len(tempResult) > 0):
                json_output[productId] = tempResult

    with open('final_output.json', 'w') as fp:
        json.dump(json_output, fp, sort_keys=True, indent=5)

    end = time.time()
    print("=========================================")
    print("\t",lCount,sCount)
    print("\tProcessing Time",str(round(end,2)))
    print("=========================================")


findDuplicates(df)