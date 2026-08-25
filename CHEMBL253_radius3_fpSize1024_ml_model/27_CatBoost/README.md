# Summary of 27_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.025
- **depth**: 6
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

86.8 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.376601 | nan          |
| auc       | 0.905895 | nan          |
| f1        | 0.794102 |   0.361402   |
| accuracy  | 0.835437 |   0.433676   |
| precision | 1        |   0.964744   |
| recall    | 1        |   0.00222092 |
| mcc       | 0.658477 |   0.361402   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.376601 |  nan        |
| auc       | 0.905895 |  nan        |
| f1        | 0.789339 |    0.433676 |
| accuracy  | 0.835437 |    0.433676 |
| precision | 0.767365 |    0.433676 |
| recall    | 0.812609 |    0.433676 |
| mcc       | 0.655227 |    0.433676 |


## Confusion matrix (at threshold=0.433676)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2380 |              422 |
| Labeled as 1 |              321 |             1392 |

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
