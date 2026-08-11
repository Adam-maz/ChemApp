# Summary of 36_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.7
- **min_samples_split**: 50
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

30.9 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.536334 |  nan        |
| auc       | 0.788255 |  nan        |
| f1        | 0.650446 |    0.342433 |
| accuracy  | 0.734405 |    0.500168 |
| precision | 0.880952 |    0.660454 |
| recall    | 1        |    0.04951  |
| mcc       | 0.415171 |    0.342433 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.536334 |  nan        |
| auc       | 0.788255 |  nan        |
| f1        | 0.535846 |    0.500168 |
| accuracy  | 0.734405 |    0.500168 |
| precision | 0.71499  |    0.500168 |
| recall    | 0.428487 |    0.500168 |
| mcc       | 0.38931  |    0.500168 |


## Confusion matrix (at threshold=0.500168)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2748 |              289 |
| Labeled as 1 |              967 |              725 |

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
