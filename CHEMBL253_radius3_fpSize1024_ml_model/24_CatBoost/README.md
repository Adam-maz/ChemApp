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

41.8 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.386922 | nan           |
| auc       | 0.901385 | nan           |
| f1        | 0.787464 |   0.299783    |
| accuracy  | 0.831008 |   0.510869    |
| precision | 0.949153 |   0.977929    |
| recall    | 1        |   0.000648569 |
| mcc       | 0.645153 |   0.315629    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.386922 |  nan        |
| auc       | 0.901385 |  nan        |
| f1        | 0.772035 |    0.510869 |
| accuracy  | 0.831008 |    0.510869 |
| precision | 0.790698 |    0.510869 |
| recall    | 0.754232 |    0.510869 |
| mcc       | 0.638342 |    0.510869 |


## Confusion matrix (at threshold=0.510869)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2460 |              342 |
| Labeled as 1 |              421 |             1292 |

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
