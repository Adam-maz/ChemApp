# Summary of 28_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 5
- **rsm**: 0.8
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

18.9 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.297593 | nan          |
| auc       | 0.930512 | nan          |
| f1        | 0.801409 |   0.32611    |
| accuracy  | 0.878427 |   0.390918   |
| precision | 0.982332 |   0.951367   |
| recall    | 1        |   0.00065061 |
| mcc       | 0.714019 |   0.32611    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.297593 |  nan        |
| auc       | 0.930512 |  nan        |
| f1        | 0.797485 |    0.390918 |
| accuracy  | 0.878427 |    0.390918 |
| precision | 0.78604  |    0.390918 |
| recall    | 0.809268 |    0.390918 |
| mcc       | 0.710807 |    0.390918 |


## Confusion matrix (at threshold=0.390918)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             3217 |              328 |
| Labeled as 1 |              284 |             1205 |

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
