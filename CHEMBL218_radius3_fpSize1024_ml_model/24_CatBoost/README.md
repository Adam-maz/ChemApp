# Summary of 24_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.2
- **depth**: 6
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

13.8 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.301282 | nan           |
| auc       | 0.929531 | nan           |
| f1        | 0.796343 |   0.295579    |
| accuracy  | 0.875248 |   0.386266    |
| precision | 0.978541 |   0.96615     |
| recall    | 1        |   0.000805643 |
| mcc       | 0.705987 |   0.295579    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.301282 |  nan        |
| auc       | 0.929531 |  nan        |
| f1        | 0.792191 |    0.386266 |
| accuracy  | 0.875248 |    0.386266 |
| precision | 0.780822 |    0.386266 |
| recall    | 0.803895 |    0.386266 |
| mcc       | 0.703241 |    0.386266 |


## Confusion matrix (at threshold=0.386266)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             3209 |              336 |
| Labeled as 1 |              292 |             1197 |

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
