# Summary of 34_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 1.0
- **min_samples_split**: 30
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

18.3 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.456845 |  nan        |
| auc       | 0.811652 |  nan        |
| f1        | 0.659828 |    0.263559 |
| accuracy  | 0.810091 |    0.369393 |
| precision | 0.925926 |    0.794093 |
| recall    | 1        |    0.110578 |
| mcc       | 0.527723 |    0.369393 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.456845 |  nan        |
| auc       | 0.811652 |  nan        |
| f1        | 0.654874 |    0.369393 |
| accuracy  | 0.810091 |    0.369393 |
| precision | 0.708041 |    0.369393 |
| recall    | 0.609134 |    0.369393 |
| mcc       | 0.527723 |    0.369393 |


## Confusion matrix (at threshold=0.369393)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             3171 |              374 |
| Labeled as 1 |              582 |              907 |

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
