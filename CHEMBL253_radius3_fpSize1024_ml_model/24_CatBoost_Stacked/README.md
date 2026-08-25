# Summary of 24_CatBoost_Stacked

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

24.0 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.378805 | nan          |
| auc       | 0.90373  | nan          |
| f1        | 0.790279 |   0.42051    |
| accuracy  | 0.831672 |   0.462365   |
| precision | 0.959732 |   0.921376   |
| recall    | 1        |   0.00772062 |
| mcc       | 0.652026 |   0.42051    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.378805 |  nan        |
| auc       | 0.90373  |  nan        |
| f1        | 0.787234 |    0.462365 |
| accuracy  | 0.831672 |    0.462365 |
| precision | 0.756321 |    0.462365 |
| recall    | 0.820782 |    0.462365 |
| mcc       | 0.649858 |    0.462365 |


## Confusion matrix (at threshold=0.462365)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2349 |              453 |
| Labeled as 1 |              307 |             1406 |

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
