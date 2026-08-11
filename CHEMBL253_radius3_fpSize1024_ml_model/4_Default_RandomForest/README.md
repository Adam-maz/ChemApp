# Summary of 4_Default_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.9
- **min_samples_split**: 30
- **max_depth**: 4
- **eval_metric_name**: logloss
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

46.5 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.513478 |  nan        |
| auc       | 0.806884 |  nan        |
| f1        | 0.658276 |    0.315502 |
| accuracy  | 0.750053 |    0.442094 |
| precision | 0.909836 |    0.764174 |
| recall    | 1        |    0.035553 |
| mcc       | 0.449697 |    0.409495 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.513478 |  nan        |
| auc       | 0.806884 |  nan        |
| f1        | 0.622123 |    0.442094 |
| accuracy  | 0.750053 |    0.442094 |
| precision | 0.677577 |    0.442094 |
| recall    | 0.575059 |    0.442094 |
| mcc       | 0.44054  |    0.442094 |


## Confusion matrix (at threshold=0.442094)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2574 |              463 |
| Labeled as 1 |              719 |              973 |

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
