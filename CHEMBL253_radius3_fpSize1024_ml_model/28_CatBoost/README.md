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

37.2 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.363685 | nan           |
| auc       | 0.90992  | nan           |
| f1        | 0.788889 |   0.365484    |
| accuracy  | 0.839289 |   0.365484    |
| precision | 0.986667 |   0.969643    |
| recall    | 1        |   0.000682388 |
| mcc       | 0.663009 |   0.365484    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.363685 |  nan        |
| auc       | 0.90992  |  nan        |
| f1        | 0.788889 |    0.365484 |
| accuracy  | 0.839289 |    0.365484 |
| precision | 0.744235 |    0.365484 |
| recall    | 0.839243 |    0.365484 |
| mcc       | 0.663009 |    0.365484 |


## Confusion matrix (at threshold=0.365484)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2549 |              488 |
| Labeled as 1 |              272 |             1420 |

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
