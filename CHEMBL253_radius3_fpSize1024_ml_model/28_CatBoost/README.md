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

20.9 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.380548 | nan          |
| auc       | 0.9039   | nan          |
| f1        | 0.787699 |   0.342963   |
| accuracy  | 0.831229 |   0.489604   |
| precision | 0.983051 |   0.9688     |
| recall    | 1        |   0.00128058 |
| mcc       | 0.646611 |   0.342963   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.380548 |  nan        |
| auc       | 0.9039   |  nan        |
| f1        | 0.775354 |    0.489604 |
| accuracy  | 0.831229 |    0.489604 |
| precision | 0.783204 |    0.489604 |
| recall    | 0.767659 |    0.489604 |
| mcc       | 0.640304 |    0.489604 |


## Confusion matrix (at threshold=0.489604)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2438 |              364 |
| Labeled as 1 |              398 |             1315 |

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
