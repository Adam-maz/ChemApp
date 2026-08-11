# Summary of 26_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 4
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

34.7 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.369523 | nan           |
| auc       | 0.906937 | nan           |
| f1        | 0.782222 |   0.370074    |
| accuracy  | 0.836752 |   0.496993    |
| precision | 0.96     |   0.966174    |
| recall    | 1        |   0.000743039 |
| mcc       | 0.652218 |   0.370074    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.369523 |  nan        |
| auc       | 0.906937 |  nan        |
| f1        | 0.76733  |    0.496993 |
| accuracy  | 0.836752 |    0.496993 |
| precision | 0.782903 |    0.496993 |
| recall    | 0.752364 |    0.496993 |
| mcc       | 0.641975 |    0.496993 |


## Confusion matrix (at threshold=0.496993)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2684 |              353 |
| Labeled as 1 |              419 |             1273 |

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
