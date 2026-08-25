# Summary of 34_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 1.0
- **min_samples_split**: 30
- **max_depth**: 3
- **eval_metric_name**: logloss
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **stratify**: True
 - **k_folds**: 5
 - **shuffle**: True
 - **random_seed**: 42

## Optimized metric
logloss

## Training time

17.1 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.542028 | nan         |
| auc       | 0.787119 | nan         |
| f1        | 0.666979 |   0.35055   |
| accuracy  | 0.723145 |   0.540011  |
| precision | 0.862745 |   0.7304    |
| recall    | 1        |   0.0561193 |
| mcc       | 0.418027 |   0.35055   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.542028 |  nan        |
| auc       | 0.787119 |  nan        |
| f1        | 0.546115 |    0.540011 |
| accuracy  | 0.723145 |    0.540011 |
| precision | 0.722382 |    0.540011 |
| recall    | 0.438996 |    0.540011 |
| mcc       | 0.386923 |    0.540011 |


## Confusion matrix (at threshold=0.540011)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2513 |              289 |
| Labeled as 1 |              961 |              752 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)


## Calibration Curve

![Calibration Curve](calibration_curve_curve.png)


## Cumulative Gains Curve

![Cumulative Gains Curve](cumulative_gains_curve.png)


## Lift Curve

![Lift Curve](lift_curve.png)



[<< Go back](../README.md)
