# Summary of 3_Default_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 6
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

48.2 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.378032 | nan          |
| auc       | 0.905382 | nan          |
| f1        | 0.793094 |   0.336224   |
| accuracy  | 0.831008 |   0.42769    |
| precision | 0.983051 |   0.971588   |
| recall    | 1        |   0.00150809 |
| mcc       | 0.655803 |   0.336224   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.378032 |   nan       |
| auc       | 0.905382 |   nan       |
| f1        | 0.783669 |     0.42769 |
| accuracy  | 0.831008 |     0.42769 |
| precision | 0.761852 |     0.42769 |
| recall    | 0.806772 |     0.42769 |
| mcc       | 0.645916 |     0.42769 |


## Confusion matrix (at threshold=0.42769)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2370 |              432 |
| Labeled as 1 |              331 |             1382 |

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
