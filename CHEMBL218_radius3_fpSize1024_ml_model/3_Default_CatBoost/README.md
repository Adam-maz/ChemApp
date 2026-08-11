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

18.3 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.297063 | nan          |
| auc       | 0.931012 | nan          |
| f1        | 0.799744 |   0.333162   |
| accuracy  | 0.878427 |   0.424817   |
| precision | 0.982332 |   0.951004   |
| recall    | 1        |   0.00147659 |
| mcc       | 0.711618 |   0.333162   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.297063 |  nan        |
| auc       | 0.931012 |  nan        |
| f1        | 0.794078 |    0.424817 |
| accuracy  | 0.878427 |    0.424817 |
| precision | 0.795684 |    0.424817 |
| recall    | 0.792478 |    0.424817 |
| mcc       | 0.707836 |    0.424817 |


## Confusion matrix (at threshold=0.424817)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             3242 |              303 |
| Labeled as 1 |              309 |             1180 |

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
