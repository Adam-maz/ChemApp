# Summary of 4_Default_RandomForest_Stacked

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

35.2 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.369994 | nan         |
| auc       | 0.90796  | nan         |
| f1        | 0.796331 |   0.408973  |
| accuracy  | 0.834551 |   0.555491  |
| precision | 0.981132 |   0.932544  |
| recall    | 1        |   0.0149866 |
| mcc       | 0.661318 |   0.408973  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.369994 |  nan        |
| auc       | 0.90796  |  nan        |
| f1        | 0.776815 |    0.555491 |
| accuracy  | 0.834551 |    0.555491 |
| precision | 0.795594 |    0.555491 |
| recall    | 0.758903 |    0.555491 |
| mcc       | 0.645941 |    0.555491 |


## Confusion matrix (at threshold=0.555491)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2468 |              334 |
| Labeled as 1 |              413 |             1300 |

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
