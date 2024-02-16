import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from scipy.stats import spearmanr

def fill_missing_with_average(df):
    # Iterate over each column in the DataFrame
    for col in df.columns:
        # Iterate over each row in the column
        for i in range(len(df[col])):
            # Check if the value is missing
            if pd.isnull(df.iloc[i][col]):
                # Find the nearest non-missing value by moving backward
                j = i - 1
                while j >= 0 and pd.isnull(df.iloc[j][col]):
                    j -= 1
                
                # Find the nearest non-missing value by moving forward
                k = i + 1
                while k < len(df[col]) and pd.isnull(df.iloc[k][col]):
                    k += 1

                # Calculate the average of the nearest non-missing values
                if j >= 0 and k < len(df[col]):
                    average_value = (df.iloc[j][col] + df.iloc[k][col]) / 2
                elif j >= 0:
                    average_value = df.iloc[j][col]
                elif k < len(df[col]):
                    average_value = df.iloc[k][col]
                else:
                    # If no non-missing values are found, set to 0 (or any default value)
                    average_value = 0
                
                # Fill the missing value with the calculated average
                df.iloc[i, df.columns.get_loc(col)] = average_value
    
    return df


# Fill_NA, NORMALIZATION, PCA
def preprocessing(df, norm = False, pca = True):
    fill_df = fill_missing_with_average(df)

    if norm == True:
        scaler = StandardScaler()
        df_normalized = scaler.fit_transform(fill_df)
    else:
        df_normalized = fill_df

    if pca == True:
        p = PCA(n_components=0.95)
        df_pca = p.fit_transform(df_normalized)
        return df_pca
    else:
        return df_normalized
    
# Print out Spearman correlation for the train set    
def metric_train(output, Y):

    metric = spearmanr(output, Y).correlation

    print('Spearman correlation for the train set: {:.1f}%'.format(100 * metric ))

    return metric 

# Generate submission file
def submission(X_test, X_test_clean, model=None, name=''):
    Y_test_submission = X_test[['ID']].copy()
    Y_test_submission['TARGET'] = model.predict(X_test_clean)
    Y_test_submission.to_csv('./Submission/' + name + '.csv', index=False)


