# Summary of 54_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.8
- **min_samples_split**: 50
- **max_depth**: 7
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

43.5 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.466048 | nan         |
| auc       | 0.855622 | nan         |
| f1        | 0.714392 |   0.3197    |
| accuracy  | 0.786636 |   0.479886  |
| precision | 0.916129 |   0.752877  |
| recall    | 1        |   0.0152355 |
| mcc       | 0.536713 |   0.355735  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.466048 |  nan        |
| auc       | 0.855622 |  nan        |
| f1        | 0.672721 |    0.479886 |
| accuracy  | 0.786636 |    0.479886 |
| precision | 0.745507 |    0.479886 |
| recall    | 0.612884 |    0.479886 |
| mcc       | 0.522131 |    0.479886 |


## Confusion matrix (at threshold=0.479886)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2683 |              354 |
| Labeled as 1 |              655 |             1037 |

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
