# Summary of 33_RandomForest_Stacked

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: entropy
- **max_features**: 1.0
- **min_samples_split**: 20
- **max_depth**: 3
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

24.2 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.36667  | nan          |
| auc       | 0.909951 | nan          |
| f1        | 0.79741  |   0.426901   |
| accuracy  | 0.836545 |   0.560669   |
| precision | 0.986486 |   0.943344   |
| recall    | 1        |   0.00799804 |
| mcc       | 0.663156 |   0.426901   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.36667  |  nan        |
| auc       | 0.909951 |  nan        |
| f1        | 0.776499 |    0.560669 |
| accuracy  | 0.836545 |    0.560669 |
| precision | 0.806797 |    0.560669 |
| recall    | 0.748395 |    0.560669 |
| mcc       | 0.649081 |    0.560669 |


## Confusion matrix (at threshold=0.560669)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2495 |              307 |
| Labeled as 1 |              431 |             1282 |

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
