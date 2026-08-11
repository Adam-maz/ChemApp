# Summary of 25_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.025
- **depth**: 9
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

302.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.356393 | nan         |
| auc       | 0.913678 | nan         |
| f1        | 0.787792 |   0.398055  |
| accuracy  | 0.84373  |   0.421572  |
| precision | 0.986667 |   0.96536   |
| recall    | 1        |   0.0018562 |
| mcc       | 0.664047 |   0.398055  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.356393 |  nan        |
| auc       | 0.913678 |  nan        |
| f1        | 0.786354 |    0.421572 |
| accuracy  | 0.84373  |    0.421572 |
| precision | 0.769666 |    0.421572 |
| recall    | 0.803783 |    0.421572 |
| mcc       | 0.663646 |    0.421572 |


## Confusion matrix (at threshold=0.421572)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2630 |              407 |
| Labeled as 1 |              332 |             1360 |

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
