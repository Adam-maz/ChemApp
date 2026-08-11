# Summary of 67_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.05
- **depth**: 7
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

77.7 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.356371 | nan          |
| auc       | 0.913714 | nan          |
| f1        | 0.784515 |   0.317984   |
| accuracy  | 0.839924 |   0.599015   |
| precision | 0.986667 |   0.964652   |
| recall    | 1        |   0.00232939 |
| mcc       | 0.655706 |   0.377967   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.356371 |  nan        |
| auc       | 0.913714 |  nan        |
| f1        | 0.75446  |    0.599015 |
| accuracy  | 0.839924 |    0.599015 |
| precision | 0.836089 |    0.599015 |
| recall    | 0.687352 |    0.599015 |
| mcc       | 0.644117 |    0.599015 |


## Confusion matrix (at threshold=0.599015)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2809 |              228 |
| Labeled as 1 |              529 |             1163 |

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
