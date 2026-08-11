# Summary of 46_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.05
- **depth**: 8
- **rsm**: 1.0
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

88.2 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.292966 | nan          |
| auc       | 0.933098 | nan          |
| f1        | 0.802083 |   0.359025   |
| accuracy  | 0.880016 |   0.391465   |
| precision | 0.982833 |   0.96048    |
| recall    | 1        |   0.00252751 |
| mcc       | 0.715988 |   0.359025   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.292966 |  nan        |
| auc       | 0.933098 |  nan        |
| f1        | 0.800132 |    0.391465 |
| accuracy  | 0.880016 |    0.391465 |
| precision | 0.78865  |    0.391465 |
| recall    | 0.811954 |    0.391465 |
| mcc       | 0.714591 |    0.391465 |


## Confusion matrix (at threshold=0.391465)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             3221 |              324 |
| Labeled as 1 |              280 |             1209 |

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
