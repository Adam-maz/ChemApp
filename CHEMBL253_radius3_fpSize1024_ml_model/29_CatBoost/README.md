# Summary of 29_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.2
- **depth**: 7
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

37.1 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.365989 | nan           |
| auc       | 0.908751 | nan           |
| f1        | 0.777371 |   0.381855    |
| accuracy  | 0.838867 |   0.487838    |
| precision | 1        |   0.972187    |
| recall    | 1        |   0.000333036 |
| mcc       | 0.64887  |   0.438744    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.365989 |  nan        |
| auc       | 0.908751 |  nan        |
| f1        | 0.770344 |    0.487838 |
| accuracy  | 0.838867 |    0.487838 |
| precision | 0.785978 |    0.487838 |
| recall    | 0.755319 |    0.487838 |
| mcc       | 0.646618 |    0.487838 |


## Confusion matrix (at threshold=0.487838)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2689 |              348 |
| Labeled as 1 |              414 |             1278 |

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
