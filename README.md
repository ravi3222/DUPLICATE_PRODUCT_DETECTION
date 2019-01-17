# DUPLICATE  PRODUCT  DETECTION


![s](../master/images/Screenshot1.png)
      

## Problem definition:

The problem of detecting duplicate products listing from structured textual data from an e-commerce [website](https://huew.co).

### Duplicate Products:

- Products with similar characteristics, same productUrl. 
- Products with same appearance but differ in color
- Products with same images

### Approach:

1. Extracted data for **Tops** category from the large dataset.
2. Performed Data preprocessing:
   - Carefully removing irrelevant columns
   - Drop rows with incomplete data 
   - Imputing null values for some rows in Title column
3. This problem of duplicate product detection can be solved by measuring the similarity between product listings semantic description.
4. Combined product details into string using relevant columns.
5. Product listing string conversion into vector using word2vec pretrained [Google's model](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit).
6. Cosine similarity is used to calculate score for two products at a time.
7. Export output score with required  JSON file format.



## Contents

- parse.py: Script to extract product category specific attributes based on product subcategory
- processing.py: Script to clean and impute missing or NA values
- model.py: Script for pretrained gesim model
- duplicates.py: Script to identify duplicates based on product details
- json_output.json: Output json file contains duplicate product IDs with similarity score for each product members
- Image_Similarity/image_extractor.ipynb: Starter script to extract image details, convert into json and download 200x200 images
- imageData.json: JSON data contains product ids with image url links 



### Future Work:

> Use siamese neural network (One shot learning) to find similarity between product images.



#### References:

- https://arxiv.org/pdf/1310.4546
- https://machinelearningmastery.com/develop-word-embeddings-python-gensim/
- https://www.machinelearningplus.com/nlp/cosine-similarity/
