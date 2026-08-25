# Summary of 30_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 8
- **rsm**: 1.0
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

48.6 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.374297 | nan          |
| auc       | 0.906917 | nan          |
| f1        | 0.791476 |   0.347178   |
| accuracy  | 0.830786 |   0.490506   |
| precision | 1        |   0.968586   |
| recall    | 1        |   0.00152886 |
| mcc       | 0.653045 |   0.347178   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.374297 |  nan        |
| auc       | 0.906917 |  nan        |
| f1        | 0.774764 |    0.490506 |
| accuracy  | 0.830786 |    0.490506 |
| precision | 0.782609 |    0.490506 |
| recall    | 0.767075 |    0.490506 |
| mcc       | 0.639359 |    0.490506 |


## Confusion matrix (at threshold=0.490506)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2437 |              365 |
| Labeled as 1 |              399 |             1314 |

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
