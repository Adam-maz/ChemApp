# Summary of 66_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.05
- **depth**: 9
- **rsm**: 1
- **loss_function**: Logloss
- **eval_metric**: Logloss
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

163.2 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.291079 |  nan        |
| auc       | 0.934377 |  nan        |
| f1        | 0.804036 |    0.350528 |
| accuracy  | 0.880413 |    0.350528 |
| precision | 0.983607 |    0.966384 |
| recall    | 1        |    0.00245  |
| mcc       | 0.7188   |    0.350528 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.291079 |  nan        |
| auc       | 0.934377 |  nan        |
| f1        | 0.804036 |    0.350528 |
| accuracy  | 0.880413 |    0.350528 |
| precision | 0.780164 |    0.350528 |
| recall    | 0.829416 |    0.350528 |
| mcc       | 0.7188   |    0.350528 |


## Confusion matrix (at threshold=0.350528)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             3197 |              348 |
| Labeled as 1 |              254 |             1235 |

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
