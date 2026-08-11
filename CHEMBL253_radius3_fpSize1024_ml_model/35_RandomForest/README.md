# Summary of 35_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.8
- **min_samples_split**: 50
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

33.0 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.514067 | nan         |
| auc       | 0.809302 | nan         |
| f1        | 0.658451 |   0.346817  |
| accuracy  | 0.75259  |   0.41511   |
| precision | 0.884298 |   0.755333  |
| recall    | 1        |   0.0339055 |
| mcc       | 0.457155 |   0.41511   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.514067 |   nan       |
| auc       | 0.809302 |   nan       |
| f1        | 0.647378 |     0.41511 |
| accuracy  | 0.75259  |     0.41511 |
| precision | 0.660517 |     0.41511 |
| recall    | 0.634752 |     0.41511 |
| mcc       | 0.457155 |     0.41511 |


## Confusion matrix (at threshold=0.41511)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             2485 |              552 |
| Labeled as 1 |              618 |             1074 |

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
