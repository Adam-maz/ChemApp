# Summary of 40_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: entropy
- **max_features**: 0.7
- **min_samples_split**: 30
- **max_depth**: 4
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

29.3 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.517902 | nan         |
| auc       | 0.813767 | nan         |
| f1        | 0.678141 |   0.377277  |
| accuracy  | 0.745958 |   0.480933  |
| precision | 0.903846 |   0.792616  |
| recall    | 1        |   0.0228105 |
| mcc       | 0.453308 |   0.447721  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.517902 |  nan        |
| auc       | 0.813767 |  nan        |
| f1        | 0.626506 |    0.480933 |
| accuracy  | 0.745958 |    0.480933 |
| precision | 0.708395 |    0.480933 |
| recall    | 0.561588 |    0.480933 |
| mcc       | 0.444676 |    0.480933 |


## Confusion matrix (at threshold=0.480933)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2406 |              396 |
| Labeled as 1 |              751 |              962 |

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
