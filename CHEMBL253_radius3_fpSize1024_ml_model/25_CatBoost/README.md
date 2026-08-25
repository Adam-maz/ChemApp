# Summary of 25_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.025
- **depth**: 9
- **rsm**: 0.9
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

337.5 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.371174 | nan          |
| auc       | 0.908868 | nan          |
| f1        | 0.796908 |   0.323789   |
| accuracy  | 0.836988 |   0.442369   |
| precision | 0.983051 |   0.962907   |
| recall    | 1        |   0.00192015 |
| mcc       | 0.661663 |   0.323789   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.371174 |  nan        |
| auc       | 0.908868 |  nan        |
| f1        | 0.788627 |    0.442369 |
| accuracy  | 0.836988 |    0.442369 |
| precision | 0.776145 |    0.442369 |
| recall    | 0.801518 |    0.442369 |
| mcc       | 0.656247 |    0.442369 |


## Confusion matrix (at threshold=0.442369)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2406 |              396 |
| Labeled as 1 |              340 |             1373 |

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
