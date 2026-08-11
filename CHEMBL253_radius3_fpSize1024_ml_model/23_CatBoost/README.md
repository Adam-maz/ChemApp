# Summary of 23_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 7
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

57.3 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.362981 | nan          |
| auc       | 0.910173 | nan          |
| f1        | 0.780947 |   0.40767    |
| accuracy  | 0.842461 |   0.509924   |
| precision | 1        |   0.968762   |
| recall    | 1        |   0.00065316 |
| mcc       | 0.653455 |   0.443346   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.362981 |  nan        |
| auc       | 0.910173 |  nan        |
| f1        | 0.772241 |    0.509924 |
| accuracy  | 0.842461 |    0.509924 |
| precision | 0.799873 |    0.509924 |
| recall    | 0.746454 |    0.509924 |
| mcc       | 0.652957 |    0.509924 |


## Confusion matrix (at threshold=0.509924)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2721 |              316 |
| Labeled as 1 |              429 |             1263 |

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
