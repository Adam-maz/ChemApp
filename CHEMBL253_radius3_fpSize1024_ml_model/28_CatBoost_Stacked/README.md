# Summary of 28_CatBoost_Stacked

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

22.0 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.371597 |  nan        |
| auc       | 0.9086   |  nan        |
| f1        | 0.793009 |    0.40956  |
| accuracy  | 0.833001 |    0.46778  |
| precision | 0.983051 |    0.92372  |
| recall    | 1        |    0.014782 |
| mcc       | 0.656634 |    0.40956  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.371597 |   nan       |
| auc       | 0.9086   |   nan       |
| f1        | 0.788914 |     0.46778 |
| accuracy  | 0.833001 |     0.46778 |
| precision | 0.757934 |     0.46778 |
| recall    | 0.822534 |     0.46778 |
| mcc       | 0.65264  |     0.46778 |


## Confusion matrix (at threshold=0.46778)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2352 |              450 |
| Labeled as 1 |              304 |             1409 |

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
