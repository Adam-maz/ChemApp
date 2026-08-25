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

103.5 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.373764 | nan          |
| auc       | 0.907532 | nan          |
| f1        | 0.793785 |   0.31699    |
| accuracy  | 0.837431 |   0.488124   |
| precision | 0.983051 |   0.960001   |
| recall    | 1        |   0.00215412 |
| mcc       | 0.657742 |   0.383493   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.373764 |  nan        |
| auc       | 0.907532 |  nan        |
| f1        | 0.783608 |    0.488124 |
| accuracy  | 0.837431 |    0.488124 |
| precision | 0.791543 |    0.488124 |
| recall    | 0.775832 |    0.488124 |
| mcc       | 0.653526 |    0.488124 |


## Confusion matrix (at threshold=0.488124)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2452 |              350 |
| Labeled as 1 |              384 |             1329 |

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
