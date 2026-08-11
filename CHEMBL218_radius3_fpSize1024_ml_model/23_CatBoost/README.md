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

28.7 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.295341 | nan          |
| auc       | 0.931956 | nan          |
| f1        | 0.796925 |   0.31843    |
| accuracy  | 0.878824 |   0.495301   |
| precision | 0.978142 |   0.967996   |
| recall    | 1        |   0.00109507 |
| mcc       | 0.707551 |   0.353143   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.295341 |  nan        |
| auc       | 0.931956 |  nan        |
| f1        | 0.787604 |    0.495301 |
| accuracy  | 0.878824 |    0.495301 |
| precision | 0.817787 |    0.495301 |
| recall    | 0.75957  |    0.495301 |
| mcc       | 0.703935 |    0.495301 |


## Confusion matrix (at threshold=0.495301)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             3293 |              252 |
| Labeled as 1 |              358 |             1131 |

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
