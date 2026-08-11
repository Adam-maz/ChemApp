# Summary of 31_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.025
- **depth**: 6
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

62.9 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.294731 | nan          |
| auc       | 0.93183  | nan          |
| f1        | 0.80205  |   0.32589    |
| accuracy  | 0.878824 |   0.391467   |
| precision | 0.987124 |   0.951415   |
| recall    | 1        |   0.00288899 |
| mcc       | 0.714949 |   0.32589    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.294731 |  nan        |
| auc       | 0.93183  |  nan        |
| f1        | 0.798147 |    0.391467 |
| accuracy  | 0.878824 |    0.391467 |
| precision | 0.786693 |    0.391467 |
| recall    | 0.80994  |    0.391467 |
| mcc       | 0.711753 |    0.391467 |


## Confusion matrix (at threshold=0.391467)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             3218 |              327 |
| Labeled as 1 |              283 |             1206 |

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
